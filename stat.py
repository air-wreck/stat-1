import numpy as np
import matplotlib.pyplot as plt

# data set: women's heights, in inches
heights = [68.5, 57.4, 53.2, 58.6, 65.6, 59.3, 56.7, 63.3, 62.4, 70.4, 63.1,
           62.1, 59.3, 70.5, 62.1, 50.2, 57.9, 62.4, 67.7, 65.4, 59.0, 58.9,
           63.1, 68.5, 61.4]

# histogram parameters
bin_width = 2.5

fig_hist, ax_hist = plt.subplots()
ax_hist.hist(heights,
    np.arange(min(heights), max(heights) + bin_width, bin_width))
ax_hist.set_xlabel('Height (in.)')
ax_hist.set_ylabel('Frequency')

fig_box, ax_box = plt.subplots()
ax_box.boxplot(heights, vert=False)
# for now, let's just print
print 'Q1:',  np.percentile(heights, 25)
print 'Med:', np.median(heights)
print 'Q3:',  np.percentile(heights, 75)
print 'Stdev:', np.std(heights)
plt.show()
