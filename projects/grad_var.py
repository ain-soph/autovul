#!/usr/bin/env python3

import autovul.vision
from autovul.vision.utils import summary, to_numpy

import torch
import numpy as np
import argparse

import time

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

    model.activate_params(model.parameters())
    model.zero_grad()

    torch.random.manual_seed(int(time.time()))
    grad_x = None
    grad_xx = None
    n_sample = 512

    for i, data in enumerate(dataset.get_dataloader('valid', shuffle=True, batch_size=1, drop_last=True)):
        if i >= n_sample:
            break
        _input, _label = model.get_data(data)
        loss = model.loss(_input, _label)
        loss.backward()
        grad_temp_list = []
        for param in model.parameters():
            grad_temp_list.append(param.grad.flatten())
        grad = torch.cat(grad_temp_list)
        grad = grad if grad.norm(p=2) <= 5.0 else grad / grad.norm(p=2) * 5.0
        grad_temp = grad.detach().cpu().clone()
        if grad_x is None:
            grad_x = grad_temp / n_sample
            grad_xx = grad_temp.square() / n_sample
        else:
            grad_x += grad_temp / n_sample
            grad_xx += grad_temp.square() / n_sample
        model.zero_grad()

    model.eval()
    model.activate_params([])

    grad_tensor = to_numpy(grad_xx - grad_x.square())
    grad_tensor[grad_tensor < 0] = 0
    var = float(np.sum(np.sqrt(grad_tensor)))

    print(f'{model.name:20}  {var:f}')
