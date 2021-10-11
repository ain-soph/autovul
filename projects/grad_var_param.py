#!/usr/bin/env python3

import autovul.vision
from autovul.vision.utils import summary

import torch
import numpy as np
import argparse

seed = 40

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    autovul.vision.environ.add_argument(parser)
    autovul.vision.datasets.add_argument(parser)
    autovul.vision.models.add_argument(parser)
    args = parser.parse_args()

    env = autovul.vision.environ.create(**args.__dict__)
    dataset = autovul.vision.datasets.create(**args.__dict__)
    model = autovul.vision.models.create(dataset=dataset, **args.__dict__)

    if env['verbose']:
        summary(env=env, dataset=dataset, model=model)
    # loss, acc1 = model._validate()

    import random
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)

    # model.train()
    model.activate_params(model.parameters())
    model.zero_grad()

    grad_list = []
    for i, data in enumerate(dataset.get_dataloader('valid', shuffle=True, batch_size=1, drop_last=True)):
        if i >= 1000:
            break
        _input, _label = model.get_data(data)
        loss = model.loss(_input, _label)
        loss.backward()
        grad_temp_list = []
        for param in model.parameters():
            grad_temp_list.append(param.grad.flatten())
        grad = torch.cat(grad_temp_list)
        norm = grad.norm(p=2)
        if norm >= 5.0:
            grad = grad * 5.0 / norm
        grad_list.append(grad.detach().cpu().clone())
        model.zero_grad()
    model.eval()
    model.activate_params([])
    grad_tensor = torch.stack(grad_list)
    std = float(grad_tensor.std(0).square().sum())
    print(f'{model.name:20}  {str(grad_tensor.shape[-1]):10}    {std:f}')
