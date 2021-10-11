#!/usr/bin/env python3

# CUDA_VISIBLE_DEVICES=0 python examples/train.py --verbose 1 --color --epoch 200 --batch_size 96 --cutout --grad_clip 5.0 --lr 0.025 --lr_scheduler --save --dataset cifar10 --model resnet18_comp

# CUDA_VISIBLE_DEVICES=0 python examples/train.py --verbose 1 --color --dataset cifar10 --adv_train --adv_train_random_init --validate_interval 1 --epoch 15 --lr 0.1 --lr_scheduler --model resnet18_comp

# CUDA_VISIBLE_DEVICES=0 python examples/train.py --verbose 1 --color --dataset cifar10 --adv_train --adv_train_random_init --adv_train_iter 1 --adv_train_alpha 0.0392156862745 --adv_train_eval_iter 7 --adv_train_eval_alpha 0.0078431372549 --validate_interval 1 --epoch 15 --lr 0.1 --lr_scheduler --model resnet18_comp

# CUDA_VISIBLE_DEVICES=0 python examples/train.py --verbose 1 --color --dataset mnist --adv_train --adv_train_random_init --adv_train_iter 1 --adv_train_alpha 0.375 --adv_train_eps 0.3 --adv_train_eval_iter 7 --adv_train_eval_alpha 0.1 --adv_train_eval_eps 0.3 --validate_interval 1 --epoch 15 --lr 0.1 --lr_scheduler --model net

import autovul.vision
from autovul.vision.utils import summary
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    autovul.vision.environ.add_argument(parser)
    autovul.vision.datasets.add_argument(parser)
    autovul.vision.models.add_argument(parser)
    autovul.vision.trainer.add_argument(parser)
    args = parser.parse_args()

    env = autovul.vision.environ.create(**args.__dict__)
    dataset = autovul.vision.datasets.create(**args.__dict__)
    model = autovul.vision.models.create(dataset=dataset, **args.__dict__)
    trainer = autovul.vision.trainer.create(dataset=dataset, model=model, **args.__dict__)

    if env['verbose']:
        summary(env=env, dataset=dataset, model=model, trainer=trainer)
    model._train(**trainer)
