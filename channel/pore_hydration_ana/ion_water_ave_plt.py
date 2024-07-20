import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import MDAnalysis as mda
import sys

# matplotlib.rcParams['font.family'] = 'Arial'

# global variables
ion_pmfs = ["./prod1_ion_dG.dat",
            "./prod2_ion_dG.dat",
            "./prod3_ion_dG.dat"]

ion_densities = ["./prod1_ion_den_b2A_cf4.dat",
                "./prod2_ion_den_b2A_cf4.dat",
                "./prod3_ion_den_b2A_cf4.dat"]

water_densities = ["./prod1_wat_den_b2A_cf4.dat",
                "./prod1_wat_den_b2A_cf4.dat",
                "./prod1_wat_den_b2A_cf4.dat",
                    ]

pdb_file = "./7_eq.pdb"

# get position
u = mda.Universe(pdb_file)
gate_residue_514to518 = u.select_atoms("protein and resid 514:518 and backbone").center_of_mass()[2]
upper_memb_pos = u.select_atoms("resname PC and name P31 and prop z > 50").center_of_mass()[2] - gate_residue_514to518
lower_memb_pos = u.select_atoms("resname PC and name P31 and prop z < 50").center_of_mass()[2] - gate_residue_514to518
selectivity_filter_469 = u.select_atoms("protein and resid 469 and name CA").center_of_mass()[2] - gate_residue_514to518
selectivity_filter_472 = u.select_atoms("protein and resid 472 and name CA").center_of_mass()[2] - gate_residue_514to518
SF_pos = (selectivity_filter_469, selectivity_filter_472)


# get ion pmf average and std
def get_ave_std(file_list):
    data_list = []
    for i in file_list:
        tmp = np.loadtxt(i, skiprows=1)
        data_list.append(tmp)
    data_array = np.concatenate(data_list, axis=1)
    data_array = data_array[:,[0,1,3,5]]
    x = data_array[:,0]
    ave = data_array[:,1:].mean(axis=1)
    std = data_array[:,1:].std(axis=1)
    return x, ave, std

x_pmf, ion_pmf_ave, ion_pmf_std = get_ave_std(ion_pmfs)
x_ion_density, ion_density_ave, ion_density_std = get_ave_std(ion_densities)
x_water_density, water_density_ave, water_density_std = get_ave_std(water_densities)


fig, ax = plt.subplots(1,3,figsize=(10,6))
ax[0].errorbar(ion_pmf_ave-ion_pmf_ave.min(), x_pmf, xerr=ion_pmf_std, capsize=2, elinewidth=1, fmt="g-", lw=2)
ax[0].set_xlabel("PMF(kcal/mol)", fontsize=16)
ax[0].set_xlim([-2,5])
ax[0].set_title("Ion PMF") #, fontname="Arial")

ax[1].errorbar(ion_density_ave, x_ion_density, xerr=ion_density_std, capsize=2, elinewidth=1, fmt="b-", lw=2)
ax[1].set_xlabel("Density", fontsize=14)
ax[1].set_title("Ion Density")

ax[2].errorbar(water_density_ave/0.1, x_water_density, xerr=water_density_std/0.1, capsize=2, elinewidth=1, fmt="c-", lw=2)
ax[2].set_xlabel("Density", fontsize=14) #, fontname="Arial")
ax[2].set_title("Water Density") #, fontname="Arial")
ax[2].set_xlim([0, 1.2])

for i in ax.flatten():
    i.set_ylabel("Z-axis", fontsize=14) #, fontname="Arial")
    i.tick_params(axis='both', which='major', labelsize=14)
    i.grid()
    # annotations
    i.set_ylim([-35, 80])
    i.axhline(upper_memb_pos, color='orange', linestyle="--")
    i.axhline(lower_memb_pos, color='orange', linestyle="--")
    i.axhline(0, color='red', linestyle="--")
    i.axhspan(ymin=SF_pos[0], ymax=SF_pos[1], color='gray', alpha=0.5, linestyle="--")

plt.tight_layout()
plt.savefig("./pmf.svg")
# plt.show()
