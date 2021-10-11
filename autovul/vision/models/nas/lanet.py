#!/usr/bin/env python3

from .darts import _DARTS, DARTS
from autovul.vision.datasets import ImageSet
from autovul.vision.utils.model_archs.lanet import gen_code_from_list, translator

import torch
import torch.hub
from torchvision.datasets.utils import download_file_from_google_drive

import os
import zipfile
from collections import OrderedDict


cifar_arch = [2, 2, 0, 2, 1, 2, 0, 2, 2, 3, 2, 1, 2, 0, 0, 1, 1, 1, 2, 1, 1, 0, 3, 4, 3, 0, 3, 1]


class LaNet(DARTS):
    available_models = ['lanet']
    model_urls = {'cifar10': '1bZsEoG-sroVyYR4F_2ozGLA5W50CT84P', }

    def __init__(self, name: str = 'lanet', layers: int = 24, C: int = 128,
                 arch: list[int] = cifar_arch, model: type[_DARTS] = _DARTS, **kwargs):
        genotype = translator(gen_code_from_list(arch))
        self.arch = arch
        super().__init__(name=name, layers=layers, C=C, genotype=genotype, model=model, std_conv=True, **kwargs)
        self.param_list['lanet'] = ['arch']

    def get_official_weights(self, dataset: str = None, **kwargs) -> OrderedDict[str, torch.Tensor]:
        if dataset is None and isinstance(self.dataset, ImageSet):
            dataset = self.dataset.name
        folder_path = os.path.join(torch.hub.get_dir(), 'lanet')
        file_path = os.path.join(folder_path, f'lanet_{dataset}.pt')
        if not os.path.exists(file_path):
            zip_file_name = 'temp.zip'
            zip_path = os.path.join(folder_path, zip_file_name)
            download_file_from_google_drive(file_id=self.model_urls[dataset], root=folder_path, filename=zip_file_name)
            with zipfile.ZipFile(zip_path, 'r') as zf:
                data = zf.read('lanas_128_99.03/top1.pt')
            with open(file_path, 'wb') as f:
                f.write(data)
            os.remove(zip_path)
        print('get official model weights from Google Drive: ', self.model_urls[dataset])
        _dict: OrderedDict[str, torch.Tensor] = torch.load(file_path, map_location='cpu')
        if 'model_state_dict' in _dict.keys():
            _dict = _dict['model_state_dict']
        new_dict: OrderedDict[str, torch.Tensor] = self.state_dict()
        old_keys = list(_dict.keys())
        new_keys = list(new_dict.keys())
        new2old: dict[str, str] = {}
        i = 0
        j = 0
        while(i < len(new_keys) and j < len(old_keys)):
            if 'auxiliary_head' not in new_keys[i] and 'auxiliary_head' in old_keys[j]:
                j += 1
                continue
            new2old[new_keys[i]] = old_keys[j]
            i += 1
            j += 1
        for i, key in enumerate(new_keys):
            new_dict[key] = _dict[new2old[key]]
        return new_dict
