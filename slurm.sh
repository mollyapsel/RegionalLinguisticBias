#!/bin/bash

#SBATCH -J train_regions-ft
#SBATCH -p general
#SBATCH -o train_regions-ft_%j.txt
#SBATCH -e train_regions-ft_%j.err
#SBATCH --mail-type=ALL
#SBATCH --mail-user=mapsel@iu.edu
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=64
#SBATCH --time=20:00:00
#SBATCH --mem=30G
#SBATCH -A r00682

#Run your program
python train_models_grouped.py