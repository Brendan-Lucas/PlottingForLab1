import csv
import matplotlib.pyplot as plt 

csv_file = open("Data\\1KHzSquareWave20pDutyCycle_output.csv", "r")
reader = csv.reader(csv_file)
time = []
voltage = []
i = 0
for row in reader:
    if "Time" in str(row[0]):
        continue
    else:
        if i == 0:
            time.append(row[0].split("\t")[0])
            voltage.append(row[0].split("\t")[1])
            i += 1
        elif i <= 4:
            i += 1
        else:
            i = 0
time_float = [float(i) for i in time]
voltage_float = [float(i) for i in voltage]
plt.plot(time_float, voltage_float)
plt.xlabel("Time (s)")
plt.ylabel("Voltage (V)")
plt.title("Voltage vs. Time (20% Duty Cycle Square Wave)")
plt.show() 

