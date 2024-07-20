import numpy as np
import matplotlib.pyplot as plt
import MDAnalysis as mda
import sys

# load style
plt.style.use("/home/huanjia9/projects/configure/mystyle.mplstyle")

# Global variable
datafile = "./pore_ana.dat"
pdb_file = "./7_eq.pdb"

# get positions
u = mda.Universe(pdb_file)
gate_residue_514to518 = u.select_atoms("protein and resid 514:518 and backbone").center_of_mass()[2]
upper_memb = u.select_atoms("resname PC and name P31 and prop z > 50").center_of_mass()[2] - gate_residue_514to518
lower_memb = u.select_atoms("resname PC and name P31 and prop z < 50").center_of_mass()[2] - gate_residue_514to518
selectivity_filter_469 = u.select_atoms("protein and resid 469 and name CA").center_of_mass()[2] - gate_residue_514to518
selectivity_filter_472 = u.select_atoms("protein and resid 472 and name CA").center_of_mass()[2] - gate_residue_514to518

# Read in
data = np.loadtxt(datafile, comments="#")

# three columns: Z-coor; Mean Radii; Std Radii
z_coor = data[:,0]
radii_mean = data[:, 1]
radii_std = data[:, 2]

plt.figure(figsize=(6,10))
plt.plot(radii_mean, z_coor-gate_residue_514to518, 'b-')

# shift by the gate position
plt.fill_betweenx(z_coor-gate_residue_514to518, radii_mean-radii_std, radii_mean+radii_std, alpha=0.3)

# set labels
plt.xlim(0, 16)
plt.xticks([0,4,8,12,16])
plt.ylim(-35, 80)
plt.yticks([-35, -20, 0, 20, 40, 60, 80])
plt.xlabel(r"Pore radius (${\AA}$)")
plt.ylabel("Z-position (${\AA}$)")

# annotation
plt.axhline(upper_memb, color='orange', linestyle="--")
plt.axhline(lower_memb, color='orange', linestyle="--")
plt.axhline(0, color='red', linestyle="--")
plt.axhspan(ymin=selectivity_filter_469, ymax=selectivity_filter_472, color='gray', alpha=0.3, linestyle="--")

plt.tight_layout()
plt.savefig("pore_size_plt.svg")
# plt.show()
