#!/bin/bash
#$ -cwd
#$ -j y
#$ -pe smp 8 #core request
#$ -l h_rt=8:0:0 #runtime
#$ -l h_vmem=8G #RAM
#$ -m bea

#load python
module load python
module load cudnn/8.1.1-cuda11.2

# Activate virtualenv
source imagene_env/bin/activate

python -c 'import tensorflow as tf; print(tf.__version__)'
#run binary python script
python binary.py


