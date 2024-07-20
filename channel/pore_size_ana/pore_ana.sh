source /SFS/product/miniforge3/23.3.1-1/centos7_x86_64/etc/profile.d/conda.sh
conda activate comp

# align and extract the second half of the trajectory
cpptraj -i extract_SH_prod1.in &> junk &
cpptraj -i extract_SH_prod2.in &> junk &
cpptraj -i extract_SH_prod3.in &> junk &
wait

# get protein prmtop and pdb
cpptraj -i get_pro_pdb_parm.in &> junk &
wait

# get aligned system 
cpptraj -i align_eq.in &> junk &
wait

# merge all second halfs
cpptraj -i merge.in &> junk &
wait

# pore analysis using mdanalysis
conda activate smi
python hole_ana.py 7_eq_pro.pdb secondhalf_merged.nc pore_ana &> junk &
wait

# replot with nicer features
python hole_plt.py

# clean dir
rm -rf hole*.out
rm -rf hole*.sph
