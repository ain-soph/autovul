> This project is a minimized runnable project cut from [trojanzoo](https://github.com/ain-soph/trojanzoo), which contains more datasets, models, attacks and defenses. This repo will not be maintained. 

This is a minimum code implementation of our USENIX'22 paper [`On the Security Risks of AutoML`](https://arxiv.org/abs/2110.06018). 

![python>=3.9](https://img.shields.io/badge/python->=3.9.2-informational.svg)
[![License](https://img.shields.io/github/license/ain-soph/autovul)](https://opensource.org/licenses/GPL-3.0)

[![pypi](https://img.shields.io/pypi/v/autovul)](https://pypi.org/project/autovul/)
[![docker](https://img.shields.io/pypi/v/autovul?label=docker)](https://hub.docker.com/r/local0state/autovul)

# Abstract
The artifact discovers the vulnerability gap between manual models and automl models against various kinds of attacks (adversarial, poison, backdoor, extraction and membership) in image classification domain. It implements all datasets, models, and attacks used in our paper.    
We expect the artifact could support the paper's claim that automl models are more vulnerable than manual models against various kinds of attacks, which could be explained by their small gradient variance.

# Checklist
* **Binary:** on [pypi](https://pypi.org/project/autovul/) with any platform.
* **Model:** Our pretrained models are available on Google Drive ([link](https://drive.google.com/drive/folders/1GrjEO89hYrdLhDMkBLC26jp1C7BwIKwm?usp=sharing)). Follow the model path style `{model_dir}/image/{dataset}/{model}.pth` to place them in correct location.
* **Data set:** CIFAR10, CIFAR100 and ImageNet32.  
Use `--download` flag to download them automatically at first running.  
ImageNet32 requires manual set-up at their [website](https://image-net.org/download-images.php) due to legality.
* **Run-time environment:**  
    At any platform (Windows and Ubuntu tested).  
    `Pytorch` and `torchvision` required. (CUDA 11.3 recommended)  
    `adversarial-robustness-toolbox` required for extraction attack and membership attack.
* **Hardware:** GPU with CUDA support is recommended.
* **Execution:** Model training and backdoor attack would be time-consuming. It would cost more than half day on a Nvidia Quodro RTX6000.
* **Metrics:** Model accuracy, attack success rate, clean accuracy drop and cross entropy.
* **Output:** console output and saved model files (.pth).
* **Experiments:** OS scripts. Recommend to run scripts 3-5 times to reduce the randomness of experiments.
* **How much disk space is required (approximately):**  
less than 5GB.
* **How much time is needed to prepare workflow (approximately):** within 1 hour.
* **How much time is needed to complete experiments (approximately):** 3-4 days.
* **Publicly available:** on GitHub.
* **Code licenses:** GPL-3.
* **Archived:** GitHub commit [ff315234561602203615d11166f8f346b4f29dd4](https://github.com/ain-soph/autovul/tree/ff315234561602203615d11166f8f346b4f29dd4).

# Description
## How to access
* [**GitHub**](https://github.com/ain-soph/autovul)  
    `pip install -e .`
* [**PYPI**](https://pypi.org/project/autovul/)  
    `pip install autovul`
* [**Docker Hub**](https://hub.docker.com/r/local0state/autovul)  
    `docker pull local0state/autovul`
* [**GitHub Packages**](https://github.com/ain-soph/autovul/pkgs/container/autovul)  
    `docker pull ghcr.io/ain-soph/autovul`

## Hardware Dependencies
Recommend to use GPU with CUDA 11.3 and CUDNN 8.0.  
Less than 5GB disk space is needed.


## Software Dependencies
You need to install `python==3.9, pytorch==1.10.x, torchvision==0.11.x` manually.

ART (IBM) is required for extraction attack and membership attack.  
`pip install adversarial-robustness-toolbox`

## Data set
We use CIFAR10, CIFAR100 and ImageNet32 datasets.  
Use `--download` flag to download them automatically at first running.  
ImageNet32 requires manual set-up at their [website](https://image-net.org/download-images.php) due to legality.
## Models
Our pretrained models are available on Google Drive ([link](https://drive.google.com/drive/folders/1GrjEO89hYrdLhDMkBLC26jp1C7BwIKwm?usp=sharing)). Follow the model path style `{model_dir}/image/{dataset}/{model}.pth` to place them in correct location. 
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
#### Train Models
You need to first run `/bash/train.sh` to get pretrained models.  
If you run it for the first time, please run with `--download` flag to download the dataset:  
`bash ./bash/train.sh "--download"`

It takes a relatively long time to train all models, here we provide our pretrained models on Google Drive ([link](https://drive.google.com/drive/folders/1GrjEO89hYrdLhDMkBLC26jp1C7BwIKwm?usp=sharing)). Follow the model path style `{model_dir}/image/{dataset}/{model}.pth` to place them in correct location.
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
* **darts-i:**   diy_deep
* **darts-ii:**  diy_no_skip
* **darts-iii:** diy_deep_noskip

These are the 3 options for `--model_arch {arch}` (with `--model darts`)


## Evaluation and Expected Result
Our paper claims that automl models are more vulnerable than manual models against various kinds of attacks, which could be explained by low gradient variance.
### Training
(Table 1) Most models around 96%-97% accuracy on CIFAR10.
### Attack
For automl models on CIFAR10,
* **adversarial**  
    (Figure 2) higher success rate around 10% (±4%).
* **poison**  
    (Figure 6) lower accuracy drop around 5% (±2%).
* **backdoor**  
    (Figure 7) 
    higher success rate around 2% (±1%)
    lower accuracy drop around 1% (±1%).
* **extraction**  
    (Figure 9) lower inference cross entropy around 0.3 (±0.1).
* **membership**  
    (Figure 10) higher auc around 0.04 (±0.01).
### Others
* **gradient variance**  
    (Figure 12) automl with lower gradient variance (around 2.2).
* **mitigation architecture**  
    (Table 4, Figure 16, 17) deep architectures (`darts-i, darts-iii`) have larger cross entropy for extraction attack (around 0.5), and higher accuracy drop for poisoning attack (around 7%).

## Experiment Customization
Use `-h` or `--help` flag for example python files to check available arguments.
