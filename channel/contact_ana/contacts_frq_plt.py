# Author: Jian Huang
# TODO:
# base on given contact file, plot contact frequencies separately
# Usage: python contacts_frq_plt.py contact_frq.tsv
#       <-- contact_frq.tsv is from get_contact_frequencies.py calculation

import pandas as pd
import matplotlib.pyplot as plt
import sys

contact_datafile = sys.argv[1]
# print(len(sys.argv))
if len(sys.argv) == 3:
    savefig = sys.argv[2]

# load 
df = pd.read_csv(contact_datafile, comment="#", header=None, names=['Res1', 'Res2', 'Freq'], sep='\s+')
df_A = df[df['Res1'].str.startswith('A')]
df_A_sorted = df_A.sort_values(by='Freq', ascending=False, ignore_index=True)
df_B = df[df['Res1'].str.startswith('B')]
df_B_sorted = df_B.sort_values(by='Freq', ascending=False, ignore_index=True)
df_C = df[df['Res1'].str.startswith('C')]
df_C_sorted = df_C.sort_values(by='Freq', ascending=False, ignore_index=True)
df_D = df[df['Res1'].str.startswith('D')]
df_D_sorted = df_D.sort_values(by='Freq', ascending=False, ignore_index=True)


# plot
fig, ax = plt.subplots(2,2,figsize=(12, 8))
# Set color thresholds
def get_colors(df):
    cutoffs = [0.6, 0.3]
    cmap = plt.get_cmap('RdYlGn')
    colors = [cmap((v - min(df['Freq'])) / (max(df['Freq']) - min(df['Freq']))) for v in df['Freq']]
    for i, v in enumerate(df['Freq']):
        if v >= cutoffs[0]:
            colors[i] = 'g'
        elif v >= cutoffs[1]:
            colors[i] = 'orange'
        else:
            colors[i] = 'r'
    return colors

# only plot Freq > 0.1
cutoff_frq = 0.1

df_A_screened = df_A_sorted[df_A_sorted['Freq']>cutoff_frq]
A_colors = get_colors(df_A_screened)
df_A_screened.plot(kind='bar', x='Res2', y='Freq', ax=ax[0][0], color=A_colors, legend=False, rot=45)
ax[0][0].set_xlabel('LIG(A)', fontsize=10, fontweight='bold')
ax[0][0].set_ylabel('Contact frq', fontsize=10, fontweight='bold')


df_B_screened = df_B_sorted[df_B_sorted['Freq']>cutoff_frq]
B_colors = get_colors(df_B_screened)
df_B_screened.plot(kind='bar', x='Res2', y='Freq', ax=ax[0][1], color=B_colors, legend=False, rot=45)
ax[0][1].set_xlabel('LIG(B)', fontsize=10, fontweight='bold')
ax[0][1].set_ylabel('Contact frq', fontsize=10, fontweight='bold')

df_C_screened = df_C_sorted[df_C_sorted['Freq']>cutoff_frq]
C_colors = get_colors(df_C_screened)
df_C_screened.plot(kind='bar', x='Res2', y='Freq', ax=ax[1][0], color=C_colors, legend=False, rot=45)
ax[1][0].set_xlabel('LIG(C)', fontsize=10, fontweight='bold')
ax[1][0].set_ylabel('Contact frq', fontsize=10, fontweight='bold')

df_D_screened = df_D_sorted[df_D_sorted['Freq']>cutoff_frq]
L_colors = get_colors(df_D_screened)
df_D_screened.plot(kind='bar', x='Res2', y='Freq', ax=ax[1][1], color=L_colors, legend=False, rot=45)
ax[1][1].set_xlabel('LIG(D)', fontsize=10, fontweight='bold')
ax[1][1].set_ylabel('Contact frq', fontsize=10, fontweight='bold')

# annotate each bar
for i in ax.flatten():
#     for p in i.patches:
#         i.annotate('{:.2f}'.format(p.get_height()), (p.get_x() + p.get_width() / 2., p.get_height()), \
#                     ha='center', va='center', xytext=(0, 5), textcoords='offset points', fontsize=5, fontweight='bold')
        i.tick_params(axis='both', which='major', labelsize=12)



plt.tight_layout()
if len(sys.argv) == 3:
    plt.savefig(savefig)
plt.show()
