import os
import MDAnalysis as mda
from MDAnalysis.analysis import distances
import numpy as np
import matplotlib.pyplot as plt
import math
import sys

# gloable variables
# pdb = "../step6.6.center.pdb"
# xtc = "../s1_TMalign.xtc"   # based on the TM aligned trajectory
pdb = sys.argv[1]

# define positions: center at gate (z=0)
u = mda.Universe(pdb)
gate_residue_514 = u.select_atoms("protein and resid 514 and name CA")
gate_residue_518 = u.select_atoms("protein and resid 518 and name CA")
gate_residue_514to518 = u.select_atoms("protein and resid 514:518 and backbone")
selectivity_filter_469 = u.select_atoms("protein and resid 469 and name CA")
selectivity_filter = u.select_atoms("protein and resid 469:472 and name CA")
selectivity_filter_472 = u.select_atoms("protein and resid 472 and name CA")
upper_memb = u.select_atoms("resname PC and name P31 and prop z > 50")
lower_memb = u.select_atoms("resname PC and name P31 and prop z < 50")


print("### Origin System ###")
print("upper_memb_pos (A): ", upper_memb.center_of_mass()[2])
print("lower_memb_pos (A): ", lower_memb.center_of_mass()[2])
print("selectivity filter (A): ", selectivity_filter.center_of_mass()[2])
print("SF 469 (A): ", selectivity_filter_469.center_of_mass()[2])
print("SF 472 (A): ", selectivity_filter_472.center_of_mass()[2] )
print("Gate (514-518 backbone; A): ", gate_residue_514to518.center_of_mass()[2])


upper_memb_pos = upper_memb.center_of_mass()[2] - gate_residue_514to518.center_of_mass()[2]
lower_memb_pos = lower_memb.center_of_mass()[2] - gate_residue_514to518.center_of_mass()[2]
SF_pos = selectivity_filter.center_of_mass()[2] - gate_residue_514to518.center_of_mass()[2]
SF_lower_469_pos = selectivity_filter_469.center_of_mass()[2] - gate_residue_514to518.center_of_mass()[2]
SF_upper_472_pos = selectivity_filter_472.center_of_mass()[2] - gate_residue_514to518.center_of_mass()[2]

print("### Shifted by the Gate (Z=0) ###")
print("upper_memb_pos (A): ", upper_memb_pos)
print("lower_memb_pos (A): ", lower_memb_pos)
print("selectivity filter (A): ", SF_pos)
print("SF 469 (A): ", SF_lower_469_pos)
print("SF 472 (A): ", SF_upper_472_pos)
