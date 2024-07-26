#!/bin/bash
#PBS -V
#PBS -N myMDsim
#PBS -o job.out
#PBS -e error.out
#PBS -q craycs
#PBS -l select=1:ncpus=2:mem=16gb:ngpus=1:gputype=V100
#PBS -M jian.huang2@merck.com

# load modules
module load amber/amber22
module load openmpi/4.1.5
export CUDA_VISIBLE_DEVICES="0"

# run md scripts
# cd $PBS_O_WORKDIR
pmemd.cuda \
    -O \
    -i pull_smd.in \
    -o pull_smd.out \
    -p final.prmtop \
    -c 100ns.rst \
    -r pull_smd.rst \
    -x pull_smd.nc \
    -ref 100ns.rst \
    -inf pull_smd.mdinfo
wait
