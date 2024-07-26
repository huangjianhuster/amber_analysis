import MDAnalysis as mda
from MDAnalysis.analysis.density import DensityAnalysis
import sys

tpr = sys.argv[1]
xtc = sys.argv[2]

u = mda.Universe(tpr, xtc)
ow = u.select_atoms("resname TIP3 WAT and name OW O OH and around 12 protein",\
                    updating=True)

D = DensityAnalysis(ow, delta=1.0)
D.run()

D.density.convert_density('TIP3P')
D.density.export("water_density.dx", type="double")
