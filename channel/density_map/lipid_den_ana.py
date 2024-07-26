import MDAnalysis as mda
from MDAnalysis.analysis.density import DensityAnalysis
import sys

tpr = sys.argv[1]
xtc = sys.argv[2]

u = mda.Universe(tpr, xtc)
pa = u.select_atoms("resname PA and around 12 protein", updating=True)
pc = u.select_atoms("resname PC and around 12 protein", updating=True)
ol = u.select_atoms("resname OL and around 12 protein", updating=True)

D_pa = DensityAnalysis(pa, delta=1.0)
D_pa.run()
D_pc = DensityAnalysis(pc, delta=1.0)
D_pc.run()
D_ol = DensityAnalysis(ol, delta=1.0)
D_ol.run()

# D.density.convert_density('TIP3P')
D_pa.density.export("PA_density.dx", type="double")
D_pc.density.export("PC_density.dx", type="double")
D_ol.density.export("OL_density.dx", type="double")
