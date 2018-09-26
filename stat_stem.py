# here, we generate a stem and leaf plot for the data
# output: LaTeX table written to stdout
#
# it is advised to pipe to a *.tex file, like:
#   python stat_stem.py > plots/stem.tex
# which can then be automatically included in the big LaTeX file like:
#   \input{plots/stem.tex}

import numpy as np
from data import heights

bins = dict([('%d' % n, []) for n in
             range(int(np.floor(min(heights))), int(np.ceil(max(heights))))])
for h in heights:
    prefix = np.floor(h)
    bins['%d' % prefix] += ['%d' % round((h - prefix) * 10)]
    bins['%d' % prefix] = sorted(bins['%d' % prefix])

# generate and print a LaTeX-formatted table
ncols = max(map(len, bins.values()))
print '\n'.join([
  r'\begin{tabular}{r|%s}' % ('c' * ncols),
  r'  \hline',
  r'  Stem & \multicolumn{%d}{l}{Leaf} \\' % ncols,
  r'  \hline',
] + [r'  %s. & %s \\' %
     (k, ' & '.join(bins[k] + [' '] * (ncols - len(bins[k]))))
     for k in sorted(bins)]
  + [r'  \hline', r'\end{tabular}'])
