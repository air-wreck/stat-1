import numpy as np
import matplotlib.pyplot as plt

# set font consistent with LaTeX, although it takes much longer to render
plt.rc('text', usetex=True)
plt.rc('font', family='serif')

# data set: women's heights, in inches
heights = [68.5, 57.4, 53.2, 58.6, 65.6, 59.3, 56.7, 63.3, 62.4, 70.4, 63.1,
           62.1, 59.3, 70.5, 62.1, 50.2, 57.9, 62.4, 67.7, 65.4, 59.0, 58.9,
           63.1, 68.5, 61.4]
bin_width = 2.5
bins = np.arange(min(heights), max(heights) + bin_width, bin_width)
bin_data, _ = np.histogram(heights, bins)
bin_labels = map(lambda lo: '[%.1f, %.1f)' % (lo, lo + bin_width), bins[:-1])

# histogram
fig_hist, ax_hist = plt.subplots()
ax_hist.hist(heights, bins, edgeColor='black')
ax_hist.set_xlabel('Height (in.)')
ax_hist.set_ylabel('Frequency')
fig_hist.savefig('histogram.pdf', bbox_inches='tight')

# pie chart
fig_pie, ax_pie = plt.subplots()
ax_pie.pie(bin_data, colors=plt.cm.viridis(np.linspace(0, 1, len(bins))),
    labels=bin_labels, autopct='%.0f\\%%', wedgeprops=dict(edgeColor='black'))
ax_pie.set_xlim(-1, 1)
ax_pie.set_ylim(-1, 1)
ax_pie.set_aspect('equal', adjustable='box')
fig_pie.savefig('pie.pdf', bbox_inches='tight')

# box plot
fig_box, ax_box = plt.subplots()
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
fig_box.savefig('box.pdf', bbox_inches='tight')

# summative statistics
print 'Mean: %.2f' % np.average(heights)
print 'Median: %.1f' % np.median(heights)
print 'Stdev: %.2f' % np.std(heights, ddof=1)
print 'Var: %.2f' % np.var(heights, ddof=1)

plt.show()
