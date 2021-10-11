#!/usr/bin/env python3

from .magnet import MagNet
from autovul.vision.models.imagemodel import ImageModel

__all__ = ['MagNet']

class_dict: dict[str, type[ImageModel]] = {
    'magnet': MagNet,
}
