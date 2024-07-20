source /SFS/product/miniforge3/23.3.1-1/centos7_x86_64/etc/profile.d/conda.sh

conda activate comp
# align trajectory
cpptraj -i align_prod1.in &> junk &
cpptraj -i align_prod2.in &> junk &
cpptraj -i align_prod3.in &> junk &
wait

conda activate smi
python ion_water_pmf_bin2A.py 7_eq.pdb 8_prod1_aligned.nc prod1 &> junk &
python ion_water_pmf_bin2A.py 7_eq.pdb 8_prod2_aligned.nc prod2 &> junk &
python ion_water_pmf_bin2A.py 7_eq.pdb 8_prod3_aligned.nc prod3 &> junk &
wait

# plot 
python ion_water_ave_plt.py &> junk &

wait
