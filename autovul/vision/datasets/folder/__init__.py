#!/usr/bin/env python3

from autovul.vision.datasets.imagefolder import ImageFolder

from .imagenet import ImageNet


__all__ = ['ImageNet']

class_dict: dict[str, ImageFolder] = {
    'imagenet': ImageNet,
}
