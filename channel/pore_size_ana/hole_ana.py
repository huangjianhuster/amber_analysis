# Author: Jian Huang
# Email: jianhuang@umass.edu

# TODO
# 1. perform HOLE analysis to a trajectory;
# 2. generate pore size datafile;
# 3. plot pore size along pore axis and standard deviation.

# Usage
# python hole_ana.py [TOPOLOGY] [TRAJ] [OUTFILE_prefix]
#   of note, this script assumes: the channel is aligned with pore axis being Z-axis (or roughly);
#           also, the protein should be centered in the box center

# Dependencies
import MDAnalysis as mda
from MDAnalysis.analysis import hole2
import matplotlib.pyplot as plt
import numpy as np
import sys
import warnings
warnings.filterwarnings('ignore')

# User-defined variables
top = sys.argv[1]
trj = sys.argv[2]
out_prefix = sys.argv[3]

# Load trajectory
u = mda.Universe(top, trj) 
total_frames = len(u.trajectory)
starting_frame = int(total_frames/2)
u_secondhalf = mda.Universe(top, trj, start=starting_frame)

# functions
def get_cpoint(u):
    pass

# Hole calculation
ha = hole2.HoleAnalysis(u, select='protein',
                        cpoint='center_of_geometry',
                        cvect=[0,0,1],
                        end_radius=15.0,
                        # executable='~/programs/hole2/exe/hole',
                        )
ha.run()

# get radii and edges
radii, edges = ha.bin_radii(bins=100, range=None)

# get mean and std
radii_mean = np.array([i.mean() for i in radii])
radii_std = np.array([i.std() for i in radii])
midpoints = 0.5*(edges[1:]+edges[:-1])

out_data = np.vstack([midpoints, radii_mean, radii_std]).T
np.savetxt(f"{out_prefix}.dat", out_data, fmt='%.3f',\
            header="Z-coor\tRadii_mean\tRadii_std",\
            delimiter="\t" )


# plot using built-in function
ax = ha.plot_mean_profile(bins=100,  # how much to chunk rxn_coord
                     n_std=1,  # how many standard deviations from mean
                     color='blue',  # color of plot
                     fill_alpha=0.2,  # opacity of standard deviation
                     legend=True)

plt.savefig(f"{out_prefix}.svg")

# vmd surface view <-- this will take a long time if you have many frames
# ha.create_vmd_surface(f"{out_prefix}.vmd")
