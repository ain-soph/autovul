#!/usr/bin/env python3

from autovul.vision.datasets.imagefolder import ImageFolder

from torchvision.datasets import ImageNet as PytorchImageNet
import os

from autovul.vision import __file__ as root_file
root_dir = os.path.dirname(root_file)


class ImageNet(ImageFolder):

    name = 'imagenet'
    data_shape = [3, 224, 224]
    url = {
        'train': 'http://www.image-net.org/challenges/LSVRC/2012/nnoupb/ILSVRC2012_img_train.tar',
        'valid': 'http://www.image-net.org/challenges/LSVRC/2012/nnoupb/ILSVRC2012_img_val.tar',
        'test': 'http://www.image-net.org/challenges/LSVRC/2012/nnoupb/ILSVRC2012_img_test.tar',
    }
    md5 = {
        'train': '1d675b47d978889d74fa0da5fadfb00e',
        'valid': '29b22e2961454d5413ddabcf34fc5622',
    }

    def __init__(self, norm_par: dict[str, list[float]] = {'mean': [0.485, 0.456, 0.406],
                                                           'std': [0.229, 0.224, 0.225], },
                 **kwargs):
        super().__init__(norm_par=norm_par, **kwargs)

    def initialize_folder(self):
        PytorchImageNet(root=self.folder_path, split='train', download=True)
        PytorchImageNet(root=self.folder_path, split='val', download=True)
        os.rename(os.path.join(self.folder_path, 'imagenet', 'val'),
                  os.path.join(self.folder_path, 'imagenet', 'valid'))
