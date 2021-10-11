> This project is a minimized runnable project cut from [trojanzoo](https://github.com/ain-soph/trojanzoo), which contains more datasets, models, attacks and defenses. This repo will not be maintained. 

This is a minimum code implementation of our USENIX'22 paper `On the Security Risks of AutoML`. 

# Abstract
## Brief Description
The paper discovers the vulnerability gap between manual models and automl models against various kinds of attacks (adversarial, poison, backdoor, extraction and membership) in image classification domain.  
We expect automl models to be more vulnerable than manual models.

## Requirements
* **Software**: You need to install `pytorch==1.9.x` and `torchvision==0.10.x` manually.  
* **Hardware**: GPU with `CUDA` and `CUDNN` recommended to run experiments.

## Usage
### Install
* [**pypi**](https://pypi.org/project/autovul/)  
    `pip install autovul`
* [**docker**](https://hub.docker.com/r/local0state/autovul)
* source on GitHub
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
### Run Experiments
#### Bash Files
Check the bash files under `/bash` to reproduce our paper results.
#### Train Models
You need to first run `/bash/train.sh` to get pretrained models.
> If you run it for the first time, please run `bash ./bash/train.sh "--download"` to download the dataset.
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
* 


## Expected Results
### Train
Most models around 96-97% accuracy on CIFAR10.
### Attack
For automl models,
* **adversarial**  
    higher success rate.
* **poison**  
    higher success rate  
    lower accuracy drop.
* **backdoor**  
    higher success rate
    lower accuracy drop.
* **extraction**  
    lower inference cross entropy.
* **membership**  
    higher auc.
### Others
* **gradient variance**  
    automl with lower gradient variance.

* **mitigation architecture**  
    automl with lower gradient variance.

