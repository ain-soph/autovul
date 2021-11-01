#!/usr/bin/env python3

# python projects/membership.py --model densenet121_comp --dataset cifar100 --pretrain

from autovul.base.utils.tensor import to_numpy
import autovul.vision.environ
import autovul.vision.datasets
import autovul.vision.models
import autovul.vision.trainer
import autovul.vision.attacks
from autovul.vision.utils import summary
import argparse
import warnings
import time
warnings.filterwarnings("ignore")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    autovul.vision.environ.add_argument(parser)
    autovul.vision.datasets.add_argument(parser)
    autovul.vision.models.add_argument(parser)
    args = parser.parse_args()
    env = autovul.vision.environ.create(**args.__dict__)
    dataset = autovul.vision.datasets.create(**args.__dict__)
    model = autovul.vision.models.create(dataset=dataset, **args.__dict__)

    if env['verbose']:
        summary(env=env, dataset=dataset, model=model)
        verbose = True
    else:
        verbose = False
    import torch
    import numpy as np
    from sklearn import metrics
    from autovul.base.utils.data import dataset_to_list
    from art.estimators.classification import PyTorchClassifier  # type: ignore
    classifier = PyTorchClassifier(
        model=model._model,
        loss=model.criterion,
        input_shape=dataset.data_shape,
        nb_classes=model.num_classes,
        clip_values=(0, 1)
    )
    # model._validate()
    max_iter = 10
    max_eval = 100
    sample_size = 32
    init_size = 50
    init_eval = 25

    from art.attacks.evasion.hop_skip_jump import HopSkipJump

    x_train, y_train = dataset_to_list(dataset.get_dataset('train'))
    x_train, y_train = to_numpy(torch.stack(x_train)), to_numpy(y_train)
    # preds = np.argmax(classifier.predict(x_train), axis=1)
    # y_train = np.argsort(classifier.predict(x_train), axis=1)[:,-2]
    # t_idx = np.arange(len(x_train))[preds == y_train]
    x_valid, y_valid = dataset_to_list(dataset.get_dataset('valid'))
    x_valid, y_valid = to_numpy(torch.stack(x_valid)), to_numpy(y_valid)
    # y_valid = np.argsort(classifier.predict(x_valid), axis=1)[:,-2]

    # preds = np.argmax(classifier.predict(x_valid), axis=1)
    # v_idx = np.arange(len(x_valid))[preds == y_valid]

    t_idx = np.arange(len(x_train))
    v_idx = np.arange(len(x_valid))
    # print(t_idx.shape, v_idx.shape)

    np.random.seed(int(time.time()))
    np.random.shuffle(t_idx)
    np.random.shuffle(v_idx)
    train_idx = t_idx[:sample_size]
    valid_idx = v_idx[:sample_size]

    x = np.concatenate((x_train[train_idx], x_valid[valid_idx]))
    y = np.concatenate((y_train[train_idx], y_valid[valid_idx]))
    y_truth = np.concatenate(([0] * sample_size, [1] * sample_size))

    hsj = HopSkipJump(classifier=classifier, targeted=False, norm=2, max_iter=max_iter, init_size=init_size, init_eval=init_eval, max_eval=max_eval, verbose=verbose)
    x_adv = hsj.generate(x=x, y=None)
    distance = np.linalg.norm((x_adv - x).reshape((x.shape[0], -1)), ord=np.inf, axis=1)

    # print(distance)
    # print(y_truth)

    fpr, tpr, _ = metrics.roc_curve(y_truth, distance)
    auc = metrics.auc(fpr, tpr)
    auc = auc if auc >= 0.5 else 1 - auc
    print('AUC:\t' + str(auc))
