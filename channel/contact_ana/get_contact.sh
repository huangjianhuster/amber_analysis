source  /SFS/product/miniforge3/23.3.1-1/centos7_x86_64/etc/profile.d/conda.sh

conda activate comp
cpptraj -i align2eq_prod1.in &> junk &
cpptraj -i align2eq_prod2.in &> junk &
cpptraj -i align2eq_prod3.in &> junk &
wait
# get protein + ligand PDB and prmtop
cpptraj -i get_pro_pdb_parm.in &> junk &

# calculate all contacts
conda activate smi
nohup get_dynamic_contacts.py --topology 7_eq_pro.pdb --trajectory 8_prod1_pro.nc --sele resname AQV --sele2 protein --itypes all --output contacts_prod1.tsv &> log &
nohup get_dynamic_contacts.py --topology 7_eq_pro.pdb --trajectory 8_prod2_pro.nc --sele resname AQV --sele2 protein --itypes all --output contacts_prod2.tsv &> log &
nohup get_dynamic_contacts.py --topology 7_eq_pro.pdb --trajectory 8_prod3_pro.nc --sele resname AQV --sele2 protein --itypes all --output contacts_prod3.tsv &> log &
wait
get_contact_frequencies.py --input_files contacts_prod1.tsv --output_file contacts_prod1_frq.tsv --itypes sb pc ps ts vdw hbbb hbsb hbss hbls hblb &> log &
get_contact_frequencies.py --input_files contacts_prod3.tsv --output_file contacts_prod3_frq.tsv --itypes sb pc ps ts vdw hbbb hbsb hbss hbls hblb &> log &
get_contact_frequencies.py --input_files contacts_prod2.tsv --output_file contacts_prod2_frq.tsv --itypes sb pc ps ts vdw hbbb hbsb hbss hbls hblb &> log &
wait
