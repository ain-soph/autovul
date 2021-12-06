# CUDA_VISIBLE_DEVICES=0 bash bash/mitigation_train.sh > results/mitigation_train.txt 2>&1

declare -a archs=("diy_deep" "diy_noskip" "diy_deep_noskip")

dataset="cifar10"
args=$1

for arch in "${archs[@]}"; do
    echo $arch
    python examples/train.py --verbose 1 --epoch 200 --batch_size 96 --cutout --grad_clip 5.0 --lr 0.025 --lr_scheduler --save --dataset $dataset --model darts --model_arch $arch $args
    echo ""
done
