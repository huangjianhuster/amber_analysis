import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.colors import LinearSegmentedColormap


def contour_plot(dat, bins=200, colormap=None, color="#00BFFF", contour_levels=None, save_path=None):
    """
    to plot 2d histogram distribution with contours
        by default, 2d histogram density will be calculated and use the "color" parameter to highlight the most dense reion.
        colors will decay linearly from the "color" parameter to "white", i.e., from "#00BFFF" decays to "white"
    dat: shape of (2, dim_y)
    color: the color for the most dense region; the #00BFFF is the color skyblue
    return None
    """
    if not colormap:
        # By default, use linear decay color scheme
        custom_cmap = LinearSegmentedColormap.from_list('custom_cmap', [(0, 'white'), (1, color)])
    else:
        custom_cmap = colormap

    # processing raw data
    heatmap, xedges, yedges = np.histogram2d(dat[0,:], dat[1,:], bins=[bins, bins], density=True)

    fig, axs = plt.subplots(1, 1, figsize=(6, 6) ) #  subplot_kw=dict(aspect='equal'))
    extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]
    im = axs.imshow(heatmap.T, origin='lower', extent=extent, cmap=custom_cmap, norm=mpl.colors.LogNorm(),\
                    zorder=2, alpha=0.8)
    
    axs.set_xlim(-60, 60)
    axs.set_ylim(-60, 60)
    
    cax = fig.add_axes([axs.get_position().x1+0.01, axs.get_position().y0, 0.02, axs.get_position().height])
    colorbar = fig.colorbar(im, cax=cax) 
    # colorbar.ax.set_ylabel('Density')
    # colorbar.ax.yaxis.set_label_position('left')
    colorbar.ax.tick_params(labelsize=8)

    # add contour
    # mask the heatmap since there are lots of zeros
    heatmap = np.ma.masked_where(heatmap == 0, heatmap)
    if not contour_levels:
        contour_levels = np.logspace(np.log10(np.min(heatmap)), np.log10(np.max(heatmap)), 5)
    else:
        contour_levels = contour_levels
    print("contour_levels: ", contour_levels)

    # exponential decay of the linewidth
    linewidths = np.logspace(np.log10(0.1), np.log10(3), len(contour_levels))
    contours = axs.contour(heatmap.T, extent=extent, levels=contour_levels, \
                            colors='k', linewidths=linewidths, zorder=5)

    # Add contour levels as lines on colorbar
    # cb_ticks = colorbar.ax.get_yticks()
    # for tick,thickiness in zip(contour_levels, linewidths):
    #     colorbar.ax.axhline(tick, color=color, linestyle='-', linewidth=thickiness)
    #     colorbar.ax.text(3.5, tick, f'{tick:.1e}', color='b', ha='right', va='center', fontsize=8)
    
    axs.grid(zorder=0)
    # plt.tight_layout()
    if save_path:
        plt.savefig(save_path)
    else:
        plt.show()



if __name__ == "__main__":
    TM1_datafile = "./TM1_com_prod1.dat"
    TM2_datafile = "./TM2_com_prod1.dat"
    TM3_datafile = "./TM3_com_prod1.dat"
    TM4_datafile = "./TM4_com_prod1.dat"
    TM5_datafile = "./TM5_com_prod1.dat"
    TM6_datafile = "./TM6_com_prod1.dat"

    TM1_data = np.loadtxt(TM1_datafile, comments="#")
    TM2_data = np.loadtxt(TM2_datafile, comments="#")
    TM3_data = np.loadtxt(TM3_datafile, comments="#")
    TM4_data = np.loadtxt(TM4_datafile, comments="#")
    TM5_data = np.loadtxt(TM5_datafile, comments="#")
    TM6_data = np.loadtxt(TM6_datafile, comments="#")
    
    TM1_A = TM1_data[:, 1:3].T
    TM1_B = TM1_data[:,7:9].T
    TM1_C = TM1_data[:,13:15].T
    TM1_D = TM1_data[:,19:21].T
    TM1 = np.hstack([TM1_A, TM1_B, TM1_C, TM1_D])
    
    TM2_A = TM2_data[:, 1:3].T
    TM2_B = TM2_data[:,7:9].T
    TM2_C = TM2_data[:,13:15].T
    TM2_D = TM2_data[:,19:21].T
    TM2 = np.hstack([TM2_A, TM2_B, TM2_C, TM2_D])
    
    TM3_A = TM3_data[:, 1:3].T
    TM3_B = TM3_data[:,7:9].T
    TM3_C = TM3_data[:,13:15].T
    TM3_D = TM3_data[:,19:21].T
    TM3 = np.hstack([TM3_A, TM3_B, TM3_C, TM3_D])
    
    TM4_A = TM4_data[:, 1:3].T
    TM4_B = TM4_data[:,7:9].T
    TM4_C = TM4_data[:,13:15].T
    TM4_D = TM4_data[:,19:21].T
    TM4 = np.hstack([TM4_A, TM4_B, TM4_C, TM4_D])
    
    TM5_A = TM5_data[:, 1:3].T
    TM5_B = TM5_data[:,7:9].T
    TM5_C = TM5_data[:,13:15].T
    TM5_D = TM5_data[:,19:21].T
    TM5 = np.hstack([TM5_A, TM5_B, TM5_C, TM5_D])
    
    TM6_A = TM6_data[:, 1:3].T
    TM6_B = TM6_data[:,7:9].T
    TM6_C = TM6_data[:,13:15].T
    TM6_D = TM6_data[:,19:21].T
    TM6 = np.hstack([TM6_A, TM6_B, TM6_C, TM6_D])
    
    TM_all = np.hstack([TM1, TM2, TM3, TM4, TM5, TM6])
    # contour_plot(TM_all, bins=100, colormap="GnBu")
    contour_plot(TM_all, bins=200, save_path="TM_com_dist.svg")
