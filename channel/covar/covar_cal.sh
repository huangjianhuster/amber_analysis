source /SFS/product/miniforge3/23.3.1-1/centos7_x86_64/etc/profile.d/conda.sh

conda activate comp

cpptraj -i get_correl_prod1.in &  junk &
cpptraj -i get_correl_prod2.in &  junk &
cpptraj -i get_correl_prod3.in &  junk &

wait

# plot
gnuplot -c plot.gnu covar_AE_prod1.dat   AE_prod1.svg
gnuplot -c plot.gnu covar_BF_prod1.dat   BF_prod1.svg
gnuplot -c plot.gnu covar_CG_prod1.dat   CG_prod1.svg
gnuplot -c plot.gnu covar_DH_prod1.dat   DH_prod1.svg

gnuplot -c plot.gnu covar_AE_BF_prod1.dat   AE_BF_prod1.svg
gnuplot -c plot.gnu covar_AE_CG_prod1.dat   AE_CG_prod1.svg
gnuplot -c plot.gnu covar_AE_DH_prod1.dat   AE_DH_prod1.svg
gnuplot -c plot.gnu covar_BF_CG_prod1.dat   BF_CG_prod1.svg
gnuplot -c plot.gnu covar_BF_DH_prod1.dat   BF_DH_prod1.svg
gnuplot -c plot.gnu covar_CG_DH_prod1.dat   CG_DH_prod1.svg


gnuplot -c plot.gnu covar_AE_prod2.dat   AE_prod2.svg
gnuplot -c plot.gnu covar_BF_prod2.dat   BF_prod2.svg
gnuplot -c plot.gnu covar_CG_prod2.dat   CG_prod2.svg
gnuplot -c plot.gnu covar_DH_prod2.dat   DG_prod2.svg

gnuplot -c plot.gnu covar_AE_BF_prod2.dat   AE_BF_prod2.svg
gnuplot -c plot.gnu covar_AE_CG_prod2.dat   AE_CG_prod2.svg
gnuplot -c plot.gnu covar_AE_DH_prod2.dat   AE_DH_prod2.svg
gnuplot -c plot.gnu covar_BF_CG_prod2.dat   BF_CG_prod2.svg
gnuplot -c plot.gnu covar_BF_DH_prod2.dat   BF_DH_prod2.svg
gnuplot -c plot.gnu covar_CG_DH_prod2.dat   CG_DH_prod2.svg



gnuplot -c plot.gnu covar_AE_prod3.dat   AE_prod3.svg
gnuplot -c plot.gnu covar_BF_prod3.dat   BF_prod3.svg
gnuplot -c plot.gnu covar_CG_prod3.dat   CG_prod3.svg
gnuplot -c plot.gnu covar_DH_prod3.dat   DH_prod3.svg

gnuplot -c plot.gnu covar_AE_BF_prod3.dat   AE_BF_prod3.svg
gnuplot -c plot.gnu covar_AE_CG_prod3.dat   AE_CG_prod3.svg
gnuplot -c plot.gnu covar_AE_DH_prod3.dat   AE_DH_prod3.svg
gnuplot -c plot.gnu covar_BF_CG_prod3.dat   BF_CG_prod3.svg
gnuplot -c plot.gnu covar_BF_DH_prod3.dat   BF_DH_prod3.svg
gnuplot -c plot.gnu covar_CG_DH_prod3.dat   CG_DH_prod3.svg
