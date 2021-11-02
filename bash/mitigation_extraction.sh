# CUDA_VISIBLE_DEVICES=0 bash bash/mitigation_extraction.sh > results/mitigation_extraction.txt 2>&1

declare -a rates=("1000" "2000" "4000" "8000" "16000")
declare -a archs=("diy_deep" "diy_noskip" "diy_deep_noskip")

dataset="cifar10"

for arch in "${archs[@]}"; do
    echo $arch
    for rate in "${rates[@]}"; do
        echo $rate
        python projects/automl/extraction_attack.py --pretrain --dataset $dataset --model darts --model_arch $arch --nb_stolen $rate
    done
done
