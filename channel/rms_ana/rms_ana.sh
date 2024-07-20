source /SFS/product/miniforge3/23.3.1-1/centos7_x86_64/etc/profile.d/conda.sh

conda activate comp

# generate 7_eq.pdb
cpptraj -i rst2pdb.in &> junk &
wait

# rmsd and rmsf calculation
cpptraj -i rms_prod1.in &> junk &
cpptraj -i rms_prod2.in &> junk &
cpptraj -i rms_prod3.in &> junk &
wait

conda activate smi
# plot
python rmsd_pro_plt.py rmsd_TM_bb_prod1.dat rmsd_pro_bb_prod1.dat rmsd_cap_bb_prod1.dat rmsd_pro_prod1.svg &> junk &
python rmsd_lig_plt.py rms_lig_A_prod1.dat rms_lig_B_prod1.dat rms_lig_C_prod1.dat rms_lig_D_prod1.dat rmsd_lig_prod1.svg &> junk &

python rmsd_pro_plt.py rmsd_TM_bb_prod2.dat rmsd_pro_bb_prod2.dat rmsd_cap_bb_prod2.dat rmsd_pro_prod1.svg &> junk &
python rmsd_lig_plt.py rms_lig_A_prod2.dat rms_lig_B_prod2.dat rms_lig_C_prod2.dat rms_lig_D_prod2.dat rmsd_lig_prod1.svg &> junk &

python rmsd_pro_plt.py rmsd_TM_bb_prod3.dat rmsd_pro_bb_prod3.dat rmsd_cap_bb_prod3.dat rmsd_pro_prod1.svg &> junk &
python rmsd_lig_plt.py rms_lig_A_prod3.dat rms_lig_B_prod3.dat rms_lig_C_prod3.dat rms_lig_D_prod3.dat rmsd_lig_prod1.svg &> junk &

wait
