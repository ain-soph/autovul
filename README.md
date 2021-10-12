> This project is a minimized runnable project cut from [trojanzoo](https://github.com/ain-soph/trojanzoo), which contains more datasets, models, attacks and defenses. This repo will not be maintained. 

This is a minimum code implementation of our USENIX'22 paper `On the Security Risks of AutoML`. 

# Abstract
## Brief Description
The paper discovers the vulnerability gap between manual models and automl models against various kinds of attacks (adversarial, poison, backdoor, extraction and membership) in image classification domain.  
We expect automl models to be more vulnerable than manual models.

# Checklist
* **Binary**: on [pypi](https://pypi.org/project/autovul/) with any platform.
* **Model**: ResNet and other model pretrained weights are available with `--official` flag to download them automatically at first running.
* **Data set**: CIFAR10, CIFAR100 and ImageNet32. Use `--download` flag to download them automatically at first running. 
* **Run-time environment**:  
    At any platform (Windows and Ubuntu tested).  
    `Pytorch` and `torchvision` required. (CUDA recommended)  
    `adversarial-robustness-toolbox` required for extraction attack and membership attack.
* **Hardware**: GPU with CUDA support is recommended.
* **Execution**: Model training and backdoor attack would be time-consuming. It would cost more than half day on a Nvidia Quodro RTX6000.
* **Metrics**: Model accuracy, attack success rate, clean accuracy drop, cross entropy, f1 score, and auc.
* **Output**: console output and saved model files (.pth).
* **Experiments**: OS scripts.
* **How much disk space is required (approximately)**:  
less than 5GB.
* **How much time is needed to prepare workflow (approximately)**: within 1 hour.
* **How much time is needed to complete experiments (approximately)**: 3-4 days.
* **Publicly available**: on GitHub.
* **Code licenses**: GPL-3.
* **Archived**: GitHub commit #XXXXXXX (todo).

# Description
## How to access
* [**GitHub**](https://github.com/ain-soph/autovul)
* [**PYPI**](https://pypi.org/project/autovul/)  
    `pip install autovul`
* [**Docker Hub**](https://hub.docker.com/r/local0state/autovul)
* [**GitHub Packages**](https://github.com/ain-soph/autovul/pkgs/container/autovul)

## Hardware Dependencies
Recommend to use GPU with CUDA and CUDNN.  
Less than 5GB disk space is needed.


## Software Dependencies
You need to install `python==3.9, pytorch==1.9.x, torchvision==0.10.x` manually.

ART (IBM) required for extraction attack and membership attack.  
`pip install adversarial-robustness-toolbox`

## Data set
CIFAR10, CIFAR100 and ImageNet32. Use `--download` flag to download them automatically at first running. 
## Models
ResNet and other model pretrained weights are available with `--official` flag to download them automatically at first running.
## Installation
* [**GitHub**](https://github.com/ain-soph/autovul)
* [**PYPI**](https://pypi.org/project/autovul/)  
    `pip install autovul`
* [**Docker Hub**](https://hub.docker.com/r/local0state/autovul)
* [**GitHub Packages**](https://github.com/ain-soph/autovul/pkgs/container/autovul)
### (optional) Config Path
You can set the config files to customize data storage location and many other default settings. View `/configs_example` as an example config setting.  
We support 3 configs (priority ascend):
* package:  
    **(DO NOT MODIFY)**  
    `autovul/base/configs/*.yml`  
    `autovul/vision/configs/*.yml`
* user:  
    `~/.autovul/configs/base/*.yml`  
    `~/.autovul/configs/vision/*.yml`
* workspace:  
    `./configs/base/*.yml`  
    `./configs/vision/*.yml`
## Experiment Workflow
#### Bash Files
Check the bash files under `/bash` to reproduce our paper results.
#### Download Datasets
If you run it for the first time, please run `bash ./bash/train.sh "--download"` to download the dataset.
#### Train Models
You need to first run `/bash/train.sh` to get pretrained models.
#### Run Attacks
```
/bash/adv_attack.sh
/bash/poison.sh
/bash/backdoor.sh
/bash/extraction.sh
/bash/membership.sh
```
#### Run Other Exps
```
/bash/grad_var.sh
/bash/mitigation_backdoor.sh
/bash/mitigation_extraction.sh
```
For mitigation experiments, the architecture names in our paper map to:
* **darts-i**  : diy_deep
* **darts-ii** : diy_no_skip
* **darts-iii**: diy_deep_noskip

These are the 3 options for `--model_arch {arch}` (with `--model darts`)


## Evaluation and Expected Result
Our paper claims that automl models are more vulnerable than manual models against various kinds of attacks, which could be explained by low gradient variance. Therefore, for each attack, we expect automl models to have: 
### Train
Most models around 96%-97% accuracy on CIFAR10.
### Attack
For automl models on CIFAR10,
* **adversarial**  
    higher success rate (around 10%).
* **poison**  
    lower accuracy drop (around 5%).
* **backdoor**  
    higher success rate (around 2%)
    lower accuracy drop (around 1%).
* **extraction**  
    lower inference cross entropy (around 0.3).
* **membership**  
    higher auc (around 0.04).
### Others
* **gradient variance**  
    automl with lower gradient variance (around 2.2).
* **mitigation architecture**  
    deep architectures (`darts-i, darts-iii`) have larger cross entropy for extraction attack (around 0.5), and higher accuracy drop for poisoning attack (around 7%).

## Experiment Customization
Use `-h` or `--help` flag for python files to check available arguments.
