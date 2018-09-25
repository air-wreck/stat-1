# here, we generate a histogram, pie chart, and box plot for the height data
# output: files 'histogram.pdf', 'pie.pdf', and 'box.pdf' in `plots/`

import numpy as np
import matplotlib.pyplot as plt
from data import heights, bins, bin_data, bin_labels

# set font consistent with LaTeX, although it takes much longer to render
plt.rc('text', usetex=True)
plt.rc('font', family='serif')

# histogram
fig_hist, ax_hist = plt.subplots()
ax_hist.set_title('Frequencies of Women\'s Heights (in.)')
ax_hist.hist(heights, bins, edgeColor='black')
ax_hist.set_xlabel('Height (in.)')
ax_hist.set_ylabel('Frequency')
fig_hist.savefig('plots/histogram.pdf', bbox_inches='tight')

# pie chart
fig_pie, ax_pie = plt.subplots()
ax_pie.set_title('Pie Chart of Women\'s Heights (in.)', y=1.08)
ax_pie.pie(bin_data, colors=plt.cm.viridis(np.linspace(0, 1, len(bins))),
    labels=bin_labels, autopct='%.0f\\%%', wedgeprops=dict(edgeColor='black'))
ax_pie.set_xlim(-1, 1)
ax_pie.set_ylim(-1, 1)
ax_pie.set_aspect('equal', adjustable='box')
fig_pie.savefig('plots/pie.pdf', bbox_inches='tight')

# box plot
fig_box, ax_box = plt.subplots()
ax_box.set_title('Box Plot of Women\'s Heights (in.)')
boxplot = ax_box.boxplot(heights, vert=False, patch_artist=True)
boxplot['boxes'][0].set(facecolor=(1, 0.78, 0.52))
ax_box.set_xlabel('Height (in.)')
ax_box.get_yaxis().set_visible(False)
box_label = '\n'.join([
    'Min = %.2f' % min(heights),
    'Q1 = %.2f' % np.percentile(heights, 25),
    'Med = %.2f' % np.median(heights),
    'Q3 = %.2f' % np.percentile(heights, 75),
    'Max = %.2f' % max(heights)
])
box_style = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
ax_box.text(0.05, 0.95, box_label, transform=ax_box.transAxes, fontsize=12,
    va='top', bbox=box_style)
ax_box.xaxis.grid(linestyle='--')
fig_box.savefig('plots/box.pdf', bbox_inches='tight')

plt.show()
