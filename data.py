# this file is just a centralized place for the data

import numpy as np

# data set: women's heights, in inches
heights = [68.5, 57.4, 53.2, 58.6, 65.6, 59.3, 56.7, 63.3, 62.4, 70.4, 63.1,
           62.1, 59.3, 70.5, 62.1, 50.2, 57.9, 62.4, 67.7, 65.4, 59.0, 58.9,
           63.1, 68.5, 61.4]

# generate classes for data
bin_width = 2.5
bins = np.arange(min(heights), max(heights) + bin_width, bin_width)
bin_data, _ = np.histogram(heights, bins)
bin_labels = map(lambda lo: '[%.1f, %.1f)' % (lo, lo + bin_width), bins[:-1])
