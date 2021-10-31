#!/usr/bin/env python3

# CUDA_VISIBLE_DEVICES=0 python examples/validate.py --color --verbose 1 --dataset cifar10 --pretrain --model resnet18_comp

import autovul.vision
from autovul.vision.utils import summary
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    autovul.vision.environ.add_argument(parser)
    autovul.vision.datasets.add_argument(parser)
    autovul.vision.models.add_argument(parser)
    args = parser.parse_args()

    env = autovul.vision.environ.create(**args.__dict__)
    dataset = autovul.vision.datasets.create(**args.__dict__)
    model = autovul.vision.models.create(dataset=dataset, **args.__dict__)
