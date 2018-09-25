# here, we generate a frequency table for the data
# output: LaTeX table written to stdout
#
# it is advised to pipe to a *.tex file, like:
#   python stat_freq.py > plots/freq.tex
# which can then be automatically included in the big LaTeX file like:
#   \input{plots/freq.tex}

from data import heights, bin_data, bin_labels

print '\n'.join([
  r'\begin{tabular}{c c}',
  r'  \hline',
  r'  Interval & Frequency \\',
  r'  \hline'
] + map(lambda x: r'  $%s$ & %d \\' % x, zip(bin_labels, bin_data))
  + [r'  \hline', r'\end{tabular}'])
