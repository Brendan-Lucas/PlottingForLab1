import sys
import os
from bokeh.plotting import figure, output_file, show

x = []
y = [[]]

if len(sys.argv) < 3:
    print("ERROR: This script accepts a minimum of 2 arguments, one for the ",
          "filename of the csv, and another for the title of the graph")
    exit(1)

with open(sys.argv[1], 'r') as f:
    lines = f.readlines()

x_label = lines[0].split('\t')[0]
y_label = lines[0].split('\t')[1]

for line in lines[1:]:
    value_arr = line.split('\t')
    x.append(value_arr[0])
    y.append(value_arr[1:])

output_file(os.path.join('outputs', (os.path.split(sys.argv[1])[-1] + ".html")))
# sample Title: "Scope Square, Voltage Vs Time (50% Duty Cycle)"
p = figure(title=sys.argv[2],
           x_axis_label=x_label+ ' (v)',
           y_axis_label=y_label+ ' (s)')

p.line(x, y, legend=y_label, line_width=2)

show(p)
