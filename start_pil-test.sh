#!/bin/bash -l

#SBATCH --gres=gpu:2
#SBATCH --time=20-00:00:00
#SBATCH --partition=p.hpcl91
#SBATCH --mem-per-cpu=20G
#SBATCH --ntasks-per-core=2
#SBATCH --output=pil-test.out
#SBATCH --ntasks=1
#SBATCH --ntasks-per-node=2
#SBATCH --exclude=hpcl9101

cd /fs/pool/pool-lambacher/Cluster_Projects/pil-test

if ! [ "$CONDA_DEFAULT_ENV" == "pil-test" ];
then
    echo 'pil-test already activated'
    mamba activate deformable_detr_pil
fi

python -u main.py --device=cpu
