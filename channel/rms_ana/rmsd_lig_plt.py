import numpy as np
import matplotlib.pyplot as plt
import sys

# load style
plt.style.use('/home/huanjia9/projects/configure/mystyle.mplstyle')

# Load datafile
datafiles = sys.argv[1:-1]
outfile = sys.argv[-1]
data_arrays = []
for datafile in datafiles:
    data = np.loadtxt(datafile, comments=['@', '#'])
    # data[:, 1] *= 10    # gromcas nm --> ang
    data_arrays.append(data)


# plot
fig, ax = plt.subplots(figsize=(10,6))
for data,name in zip(data_arrays, datafiles):
    ax.plot(data[:, 0]/20, data[:, 1], lw=2, label=f"{name}")

ax.set_xlabel("Simulation time (ns)", fontsize=14)
ax.set_yticks([0,2,4,6,8,10,12])
ax.set_ylabel(r"RMSD ($\AA$)", fontsize=14)
ax.set_ylim([0,12])
ax.tick_params(axis='both', which='major', labelsize=14)

plt.legend(frameon=False)
plt.tight_layout()
plt.savefig(outfile)
# plt.show()
