#! /bin/bash
#PBS -N TNB_IMG_valid
#PBS -o out.log
#PBS -e err.log
#PBS -l ncpus=104
#PBS -q gpu

module load compiler/anaconda3
source /home/aakash.rao_ug23/TNBC/gitrepo/tnbc/Image_Processing/imgsplit/env/bin/activate
python3 /home/aakash.rao_ug23/TNBC/gitrepo/tnbc/Image_Processing/imgvalidation/code.py