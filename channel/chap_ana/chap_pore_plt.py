import json
import matplotlib.pyplot as plt
import sys
import numpy as np

# load input json
filelist = sys.argv[1:-1]
outfile = sys.argv[-1]
data_list = []
for file in filelist:
    with open(file, "r") as f:
        data = json.load(f)
        data_list.append(data)


def extract_pore(data):
    # extract pore profile information
    pore_profile = data['pathwayProfile']
    pore_axis = np.array(pore_profile['s'])*10
    pore_radius_mean = np.array(pore_profile['radiusMean'])*10
    pore_radius_std = np.array(pore_profile['radiusSd'])*10
    return pore_axis, pore_radius_mean, pore_radius_std

def extract_res_hydrophobicity(data):
    # hydrophobicity 
    pore_facing = np.array(data['residueSummary']['poreLining']['mean']) > 0.5
    pore_resi_axis = np.array(data['residueSummary']['s']['mean'])[pore_facing]*10
    pore_resi_com = np.array(data["residueSummary"]["rho"]["mean"])[pore_facing]*10
    pore_hydropho = np.array(data["residueSummary"]["hydrophobicity"])[pore_facing]
    return pore_resi_axis, pore_resi_com, pore_hydropho
    
def extract_pore_hydrophobicity(data):
    pore_profile = data['pathwayProfile']
    pore_axis = np.array(pore_profile['s'])*10
    pore_hydrophobicity_mean = np.array(pore_profile['plHydrophobicityMean'])
    pore_hydrophobicity_std = np.array(pore_profile['plHydrophobicitySd'])
    return pore_axis, pore_hydrophobicity_mean, pore_hydrophobicity_std

def extract_solvent(data):
    pore_profile = data['pathwayProfile']
    pore_axis = np.array(pore_profile['s'])*10
    pore_solvent_density_mean = np.array(pore_profile['densityMean'])
    pore_solvent_density_std = np.array(pore_profile['densitySd'])
    return pore_axis, pore_solvent_density_mean, pore_solvent_density_std

# get pore data list
pore_data_list = []
pore_res_hydrophobicity_list = []
pore_hydrophobicity_list = []
pore_solvent_density_list = []
for data in data_list:
    pore_data_list.append(extract_pore(data))
    pore_res_hydrophobicity_list.append(extract_res_hydrophobicity(data))
    pore_hydrophobicity_list.append(extract_pore_hydrophobicity(data))
    pore_solvent_density_list.append(extract_solvent(data))

# plot
fig, axs = plt.subplots(1, 3, figsize=(14,10))
axs = axs.ravel()
for pore_data, pore_resi_hydropho, hydropho, solv_density in zip(pore_data_list, pore_res_hydrophobicity_list,\
                                                            pore_hydrophobicity_list, pore_solvent_density_list):
    pore_axis, pore_radius_mean, pore_radius_std = pore_data[0], pore_data[1], pore_data[2]
    pore_resi_axis, pore_resi_com, pore_resi_hydropho = pore_resi_hydropho[0], pore_resi_hydropho[1], pore_resi_hydropho[2]
    pore_axis, pore_hydropho_mean, pore_hydropho_std = hydropho[0], hydropho[1], hydropho[2]
    pore_axis, pore_solv_den_mean, pore_solv_den_std = solv_density[0], solv_density[1], solv_density[2]
    
    # ax.errorbar(pore_radius_mean, -1*pore_axis, xerr=pore_radius_std, fmt="-", capsize=2, lw=2, elinewidth=1, errorevery=10)

    axs[0].plot(pore_radius_mean, -1*pore_axis, c="#1f77b4")
    axs[0].fill_betweenx(-1*pore_axis, pore_radius_mean-pore_radius_std, pore_radius_mean+pore_radius_std, alpha=0.3, color="#1f77b4")
    # add pore resi hydrophobicity here
    axs[0].set_xlim([0,16])
    axs[0].set_xticks([0,4,8,12,16])
    axs[0].set_xlabel(r"Pore radius ($\AA$)", fontsize=14)


    axs[1].plot(pore_hydropho_mean, -1*pore_axis, c="#ff7f0e")
    axs[1].fill_betweenx(-1*pore_axis, pore_hydropho_mean-pore_hydropho_std, pore_hydropho_mean+pore_hydropho_std, alpha=0.3, color="#ff7f0e")
    axs[1].set_xlabel(r"Pore hydrophobicity", fontsize=14)
    axs[1].set_xlim([-1, 1])
    axs[1].set_xticks([-1,-0.5,0,0.5,1])

    # density data is weird...
    # axs[2].plot(pore_solv_den_mean, -1*pore_axis)
    # axs[2].fill_betweenx(-1*pore_axis, pore_solv_den_mean-pore_solv_den_std, pore_solv_den_mean+pore_solv_den_std, alpha=0.3)
    # axs[2].set_xlabel(r"Pore solvent density", fontsize=14)
    
    scatter = axs[2].scatter(pore_resi_com, -1*pore_resi_axis, c=pore_resi_hydropho, marker='o', cmap="coolwarm", vmin=-1, vmax=1)
    axs[2].set_xlabel(r"Residue COM dist to pore-axis", fontsize=14)
    axs[2].set_xlim([0,16])
    axs[2].set_xticks([0,4,8,12,16])
    cbar = fig.colorbar(scatter, ax=axs[2], fraction=0.05,\
                        ticks=[-1,-0.5,0,0.5,1], pad=0.04, aspect=60)


for ax in axs:
    ax.set_ylim([-35, 80])
    ax.set_ylabel(r"Z-axis ($\AA$)", fontsize=14)
    ax.tick_params(axis='both', which='major', labelsize=14)
    ax.grid()
plt.tight_layout()
plt.savefig(f"{outfile}.svg")
plt.show()
