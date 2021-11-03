# CUDA_VISIBLE_DEVICES=0 bash bash/poison.sh > results/poison.txt 2>&1

declare -a archs=("amoebanet" "darts" "drnas" "enas" "nasnet" "pc_darts" "pdarts" "snas_mild" "sgas" "random")
declare -a models=("bit_comp" "densenet121_comp" "dla34_comp" "resnet18_comp" "resnext50_32x4d_comp" "vgg13_bn_comp" "wide_resnet50_2_comp")
declare -a rates=("0.0" "0.1" "0.2" "0.4")

attack="poison_random"
dataset="cifar10"
args=$1

for model in "${models[@]}"; do
    echo $model
    for rate in "${rates[@]}"; do
        echo $rate
        python examples/adv_attack.py --epoch 50 --batch_size 96 --cutout --grad_clip 5.0 --lr 0.025 --lr_scheduler --validate_interval 1 \
            --attack $attack --dataset $dataset --poison_percent $rate --model $model --train_mode dataset $args
    done
done

for arch in "${archs[@]}"; do
    echo $arch
    for rate in "${rates[@]}"; do
        echo $rate
        python examples/adv_attack.py --epoch 50 --batch_size 96 --cutout --grad_clip 5.0 --lr 0.025 --lr_scheduler --validate_interval 1 \
            --attack $attack --dataset $dataset --poison_percent $rate --model darts --model_arch $arch --train_mode dataset $args
    done
done
