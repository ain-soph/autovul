#!/usr/bin/env python3

# CUDA_VISIBLE_DEVICES=1 python examples/adv_attack.py --verbose 1 --color --attack pgd --dataset cifar10 --model resnet18_comp --pretrain --stop_threshold 0.0 --target_idx 1 --require_class --grad_method nes --valid_batch_size 200

import autovul.vision
from autovul.vision.utils import summary
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    autovul.vision.environ.add_argument(parser)
    autovul.vision.datasets.add_argument(parser)
    autovul.vision.models.add_argument(parser)
    autovul.vision.trainer.add_argument(parser)
    autovul.vision.attacks.add_argument(parser)
    args = parser.parse_args()

    env = autovul.vision.environ.create(**args.__dict__)
    dataset = autovul.vision.datasets.create(**args.__dict__)
    model = autovul.vision.models.create(dataset=dataset, **args.__dict__)
    trainer = autovul.vision.trainer.create(dataset=dataset, model=model, **args.__dict__)
    attack = autovul.vision.attacks.create(dataset=dataset, model=model, **args.__dict__)

    if env['verbose']:
        summary(env=env, dataset=dataset, model=model, train=trainer, attack=attack)
    attack.attack(**trainer)
