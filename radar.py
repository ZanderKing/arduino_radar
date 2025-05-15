import serial
import matplotlib.pyplot as plt
import numpy as np

PORT = 'COM9'
BAUD = 9600
MAX_DIST = 100
THRESHOLD = 20
SWEEP_MIN = 0
SWEEP_MAX = 120

ser = serial.Serial(PORT, BAUD)
print(ser.readline().decode())
plt.ion()
fig = plt.figure()
ax = fig.add_subplot(111, polar=True)
ax.set_theta_zero_location("N")
ax.set_theta_direction(-1)
ax.set_ylim(0, MAX_DIST)
ax.set_xlim(np.deg2rad(SWEEP_MIN), np.deg2rad(SWEEP_MAX))

sweep_data = {}

while True:
    line = ser.readline().decode().strip()
    print(line)
    if "Angle:" in line and "Distance:" in line:
        parts = line.split(",")
        angle = int(parts[0].split(":")[1].strip())
        distance = float(parts[1].split(":")[1].replace("cm", "").strip())
        if distance > MAX_DIST:
            distance = MAX_DIST
        if SWEEP_MIN <= angle <= SWEEP_MAX:
            color = 'red' if distance < THRESHOLD else 'green'
            sweep_data[angle] = (distance, color)
            ax.clear()
            ax.set_theta_zero_location("N")
            ax.set_theta_direction(-1)
            ax.set_ylim(0, MAX_DIST)
            ax.set_xlim(np.deg2rad(SWEEP_MIN), np.deg2rad(SWEEP_MAX))
            ax.set_title("Live Radar Sweep")
            for ang, (dist, col) in sweep_data.items():
                ax.plot(np.deg2rad(ang), dist, 'o', color=col, markersize=8)
            ax.plot([np.deg2rad(angle), np.deg2rad(angle)], [0, MAX_DIST], 'y-', alpha=0.3)
            plt.pause(0.01)

ser.close()
