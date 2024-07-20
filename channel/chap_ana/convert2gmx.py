import parmed as pmd
import sys                                                                                                              

# Global variables
top = sys.argv[1]
crd = sys.argv[2]
out_prefix = sys.argv[3]

parm = pmd.load_file(top, crd)
parm.save(f"{out_prefix}_gmx.top")
parm.save(f"{out_prefix}_gmx.gro")
