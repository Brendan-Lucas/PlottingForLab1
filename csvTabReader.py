import sys
import os
from bokeh.plotting import figure, output_file, show

x = []
y = [[]]


with open(sys.argv[1], 'r') as f:
    lines = f.readlines()

for line in lines:
    value_arr = line.split('\t')
    x.append(value_arr[0])
    y.append(value_arr[1:])

output_file(sys.argv[1], ".html")

p = figure(title="simple line example",
           x_axis_label='x',
           y_axis_label='y')

p.line(x, y, legend="Temp.", line_width=2)

show(p)
