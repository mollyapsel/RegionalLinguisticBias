#!/bin/bash

#SBATCH -J trainpol
#SBATCH -p general
#SBATCH -o trainpol2_%j.txt
#SBATCH -e trainpol2_%j.err
#SBATCH --mail-type=ALL
#SBATCH --mail-user=mapsel@iu.edu
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=64
#SBATCH --time=20:00:00
#SBATCH --mem=130G
#SBATCH -A r00682

#Run your program
python train_models_pol.py