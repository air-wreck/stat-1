# here, we compute the summative statistics for the data
# output: LaTeX table written to stdout
#
# it is advised to pipe to a *.tex file, like:
#   python stat_calc.py > plots/summative.tex
# which can then be automatically included in the big LaTeX file like:
#   \input{plots/summative.tex}

import numpy as np
from collections import Counter
from data import heights

# calculate summative statistics
# to accomodate various precisions, each element is a tuple: (val, fmt_str)
stats = {
  'Mean':               (np.average(heights), '%.2f'),
  'Median':             (np.median(heights), '%.1f'),
  'Mode': (lambda modes: (tuple(modes), ', '.join(['%.1f'] * len(modes))))
          ((lambda l: filter(lambda k: l[k] == max(l.values()), l))
           (Counter(heights))),
  'Midrange':           (np.average([max(heights), min(heights)]), '%.1f'),
  'Range':              (np.ptp(heights), '%.1f'),
  'Standard Deviation': (np.std(heights, ddof=1), '%.2f'),
  'Variance':           (np.var(heights, ddof=1), '%.2f')
}

# we print in LaTeX so that the output can easily be piped to another process
print '\n'.join([
  r'\begin{tabular}{l c}',
  r'  \hline',
  r'  Statistic & Value \\',
  r'  \hline',
] + [r'  %s & %s \\' % (k, stats[k][1] % stats[k][0]) for k in sorted(stats)]
  + [r'  \hline', r'\end{tabular}'])
