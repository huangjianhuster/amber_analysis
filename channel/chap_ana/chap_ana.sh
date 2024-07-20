source /SFS/product/miniforge3/23.3.1-1/centos7_x86_64/etc/profile.d/conda.sh
conda activate comp

# align TM and output xtc files (the whole system)
cpptraj -i convert2xtc_prod1.in &> junk &
cpptraj -i convert2xtc_prod2.in &> junk &
cpptraj -i convert2xtc_prod3.in &> junk &
wait

# generate gromacs files
python convert2gmx.py final.prmtop 8_prod1.rst system

# merge all second halfs
cpptraj -i merge.in &> junk &
wait

# generate ndx and gro file for chap
module load gromacs/5.1.4
echo -e "r 514-518 & 1 & 4 \n q" | gmx_mpi make_ndx -f 7_eq.pdb -o index.ndx
sed s/HIE/HIS/g system_gmx.gro > for_chap.gro
sed -i s/ACE/ALA/g for_chap.gro
sed -i s/NME/ALA/g for_chap.gro
sed -i s/CYX/CYS/g for_chap.gro

# run CHAP; check README
