import numpy as np
import matplotlib.pyplot as plt

# Simulation settings
num_steps = 4096  # Time steps
threshold_4x = 1023  # Maximum value for 4X (10 bits)
threshold_1x = 4095  # Maximum value for 1X (12 bits)

# Offset angle settings
offset_degrees = 1 # +:lead, -:lag  
offset_1x = int(threshold_1x * (offset_degrees / 360))
if offset_1x < 0:
    offset_1x = 4096 + offset_1x 

# Initial values
theta_4x = []  # 4X
theta_1x = []  # 1X
combined = []  # 12-bit combined value

current_4x = 0
current_1x = offset_1x

# Simulation loop
for step in range(num_steps):
    # Count up for 4X
    current_4x += 1
    current_1x += 1

    if current_4x > threshold_4x:
        current_4x = 0
        
    if current_1x > threshold_1x:
        current_1x = 0
    current_1xa = int(current_1x / 1024) * 1024
    
    # Record data
    theta_4x.append(current_4x)
    theta_1x.append(current_1xa)

    combined_value = current_4x + current_1xa
    combined.append(combined_value)

# Plotting
plt.figure(figsize=(10, 5))
plt.plot(theta_4x, label="4X (10bit)", linestyle='-', marker='o', markersize=1)
plt.plot(theta_1x, label="1X (12bit)", linestyle='--', marker='s', markersize=1)
plt.plot(combined, label="Combined (12bit)", linestyle='-', marker='d', markersize=1, color='g')

plt.axhline(y=threshold_4x, color='gray', linestyle='dotted', label="90° (1023)")
plt.xlabel("Time (Steps)")
plt.ylabel("Angle (Unit: LSB)")
plt.legend()
plt.title(f"1X Phase Offset ({offset_degrees}° offset)")
plt.grid()
plt.show()
