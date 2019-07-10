import sys
import os
from bokeh.plotting import figure, output_file, show

x = []
y = [[]]


with open(sys.argv[1], 'r') as f:
    lines = f.readlines()

x_label = lines[0].split('\t')[0]
y_label = lines[0].split('\t')[1]

for line in lines[1:]:
    value_arr = line.split('\t')
    x.append(value_arr[0])
    y.append(value_arr[1:])

output_file(os.path.join('outputs', (os.path.split(sys.argv[1])[-1] + ".html")))

p = figure(title="Scope Square",
           x_axis_label=x_label,
           y_axis_label=y_label)

p.line(x, y, legend="Temp.", line_width=2)

show(p)
