#!/usr/bin/env python3

import autovul.base.configs
from autovul.base.configs import Config

import os

config_path: dict[str, str] = {
    'package': os.path.dirname(__file__),
    'user': os.path.normpath(os.path.expanduser('~/.autovul/configs/vision')),
    'project': os.path.normpath('./configs/vision'),
}
config = Config(_base=autovul.base.configs.config, **config_path)
