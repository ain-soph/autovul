#!/usr/bin/env python3

from .adv import *
from .poison import *
from .backdoor import *

from autovul.vision.configs import Config, config
from autovul.vision.datasets import ImageSet
import autovul.base.attacks
from autovul.base.attacks import Attack
import argparse
from typing import Union

class_dict = {
    # adversarial attack
    'pgd': PGD,

    # poisoning attack
    'poison_basic': PoisonBasic,
    'poison_random': PoisonRandom,

    # backdoor attack
    'badnet': BadNet,
    'trojannn': TrojanNN,
    'latent_backdoor': LatentBackdoor,
    'imc': IMC,
}


def add_argument(parser: argparse.ArgumentParser, attack_name: str = None, attack: Union[str, Attack] = None,
                 class_dict: dict[str, type[Attack]] = class_dict):
    return autovul.base.attacks.add_argument(parser=parser, attack_name=attack_name, attack=attack,
                                             class_dict=class_dict)


def create(attack_name: str = None, attack: Union[str, Attack] = None,
           dataset_name: str = None, dataset: Union[str, ImageSet] = None,
           config: Config = config, class_dict: dict[str, type[Attack]] = class_dict, **kwargs):
    return autovul.base.attacks.create(attack_name=attack_name, attack=attack,
                                       dataset_name=dataset_name, dataset=dataset,
                                       config=config, class_dict=class_dict, **kwargs)
