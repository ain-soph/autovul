#!/usr/bin/env python3

from autovul.vision.datasets.imageset import ImageSet

from .cifar import CIFAR10, CIFAR100
from .downsampled_imagenet import ImageNet16, ImageNet32
from .mnist import MNIST

__all__ = ['MNIST', 'CIFAR10', 'CIFAR100', 'ImageNet16', 'ImageNet32']

class_dict: dict[str, ImageSet] = {
    'mnist': MNIST,
    'cifar10': CIFAR10,
    'cifar100': CIFAR100,
    'imagenet16': ImageNet16,
    'imagenet32': ImageNet32,
}
