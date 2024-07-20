source /SFS/product/miniforge3/23.3.1-1/centos7_x86_64/etc/profile.d/conda.sh

conda activate comp

cpptraj -i TM_com.in &> junk &
wait

conda activate smi
python hist_2d.py &> contour.dat

wait
