source /SFS/product/miniforge3/23.3.1-1/centos7_x86_64/etc/profile.d/conda.sh
conda activate comp

prmtop=$1
traj=$2
frame=$3
dist=$4

# frame2=$(($frame+1))

cat > get_frame.in << EOF
parm $prmtop [sys]
trajin $traj $frame $frame  1 parm [sys]

trajout frame_${frame}_${dist}.rst restart
EOF

cpptraj -i get_frame.in &> junk &
wait
