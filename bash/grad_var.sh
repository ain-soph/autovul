declare -a archs=("amoebanet" "darts" "drnas" "enas" "nasnet" "pc_darts" "pdarts" "sgas" "snas_mild" "random")
declare -a models=("bit_comp" "densenet_comp" "dla34_comp" "resnet18_comp" "resnext50_32x4d_comp" "vgg13_bn_comp" "wide_resnet50_2_comp")

dataset="cifar10"
args=$1

for model in "${models[@]}"
do
    python projects/measure_covariance.py --pretrain --dataset $dataset --model $model $args
done

for arch in "${archs[@]}"
do
    python projects/measure_covariance.py --pretrain --dataset $dataset --model darts --model_arch $arch $args
done