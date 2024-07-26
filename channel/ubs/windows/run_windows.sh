#!/bin/bash

module load amber/amber22
module load openmpi/4.1.5

export prmtop=final.prmtop

MAX_THREAD=6
counter=1

# for i in $(seq 0.0 2.0 6.0)
for i in $(seq 1.0 1.0 40.0)
do
    cuda_num=$(((${i%.*}-1)%6))
    export CUDA_VISIBLE_DEVICES="${cuda_num}"
    
    mkdir dist_${i}
    cd dist_${i}

    cp ../com_res.rst .
    ln -s ../frame_*_${i}.rst ./frame_${i}.rst
    sed -i "s/DIST/${i}/g" com_res.rst

    # echo "pmemd.cuda -O -i ../ubs_prod.in -o window_${i}.out -p ../$prmtop -c frame_${i}.rst -r window_${i}.rst -x window_${i}.nc -inf window_${i}.mdinfo -ref ../100ns.rst &> junk &"
    pmemd.cuda -O -i ../ubs_prod.in -o window_${i}.out -p ../$prmtop -c frame_${i}.rst -r window_${i}.rst -x window_${i}.nc -inf window_${i}.mdinfo -ref ../100ns.rst &> junk &

    core=$(echo "$counter % $MAX_THREAD" | bc)

    cd ..
    
    if [ $core -eq 0 ];then
        wait
    fi
    counter=$(expr $counter + 1)
done
