#!/usr/bin/env python3

from autovul.vision.configs import Config, config
from autovul.base.trainer import Trainer
import autovul.base.trainer

from typing import TYPE_CHECKING
from autovul.vision.datasets import ImageSet    # TODO: python 3.10
from autovul.vision.models import ImageModel
import argparse
if TYPE_CHECKING:
    pass


def add_argument(parser: argparse.ArgumentParser, ClassType: type[Trainer] = Trainer) -> argparse._ArgumentGroup:
    return autovul.base.trainer.add_argument(parser=parser, ClassType=ClassType)


def create(dataset_name: str = None, dataset: ImageSet = None, model: ImageModel = None,
           config: Config = config, ClassType=Trainer, **kwargs):
    return autovul.base.trainer.create(dataset_name=dataset_name, dataset=dataset,
                                    ClassType=ClassType,
                                    model=model, config=config, **kwargs)
