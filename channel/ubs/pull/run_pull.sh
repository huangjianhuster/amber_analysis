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
    -i pull_jar.in \
    -o pull.out \
    -p final.prmtop \
    -c 100ns.rst \
    -r pull.rst \
    -x pull.nc \
    -ref 100ns.rst \
    -inf pull.mdinfo
wait
