#!/usr/bin/env python3

import autovul.vision
from autovul.vision.attacks import BadNet

from autovul.vision.utils import summary
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    autovul.vision.environ.add_argument(parser)
    autovul.vision.datasets.add_argument(parser)
    autovul.vision.models.add_argument(parser)
    autovul.vision.marks.add_argument(parser)
    autovul.vision.attacks.add_argument(parser)
    args = parser.parse_args()

    env = autovul.vision.environ.create(**args.__dict__)
    dataset = autovul.vision.datasets.create(**args.__dict__)
    model = autovul.vision.models.create(dataset=dataset, **args.__dict__)
    mark = autovul.vision.marks.create(dataset=dataset, **args.__dict__)
    attack: BadNet = autovul.vision.attacks.create(dataset=dataset, model=model, mark=mark, **args.__dict__)

    if env['verbose']:
        summary(env=env, dataset=dataset, model=model, mark=mark, attack=attack)
    attack.load()
    attack.validate_fn()
