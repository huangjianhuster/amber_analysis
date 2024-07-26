source /SFS/product/miniforge3/23.3.1-1/centos7_x86_64/etc/profile.d/conda.sh
conda activate smi

module load gromacs/5.1.4
# system_gmx.gro,system_gmx.top and index.ndx are from CHAP analysis folder
gmx_mpi grompp -f prod.mdp -c system_gmx.gro -p system_gmx.top -o prod.tpr

# all_merged_TMaligned.xtc: from CHAP
python water_den_ana.py prod.tpr all_merged_TMaligned.xtc &> junk &
python PA_den_ana.py prod.tpr all_merged_TMaligned.xtc &> junk &
python PC_den_ana.py prod.tpr all_merged_TMaligned.xtc &> junk &
python OL_den_ana.py prod.tpr all_merged_TMaligned.xtc &> junk &

wait
