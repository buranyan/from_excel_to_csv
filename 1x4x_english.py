import numpy as np
import matplotlib.pyplot as plt

# Simulation settings
num_steps = 5000  # Time steps
threshold_4x = 1023  # Maximum value for 4X (10 bits)
threshold_1x = 4  # Maximum value for 1X (2 bits, 0-3)

# Lag angle settings
lag_degrees = 45  
lag_4x = int(threshold_4x * (lag_degrees / 90))  # Set lag in terms of 4X counts (approx. 512)

# Initial values
theta_4x = []
theta_1x = []  # 1X (Reference)
lagged_1x = []  # Lagged 1X
combined = []  # 12-bit combined value

current_4x = 0
current_1x = 0
delayed_1x = 0  # Delayed 1X
lag_buffer = 0  # Buffer for 1X delay processing

# Simulation loop
for step in range(num_steps):
    # Count up for 4X
    current_4x += 1
    lag_buffer += 1  # Accumulate delay count

    if current_4x > threshold_4x:
        current_4x = 0
        current_1x = (current_1x + 1) % threshold_1x  # Increment 1X when 1023 is exceeded

    # Handle delayed 1X
    if lag_buffer >= lag_4x:
        delayed_1x = current_1x  # Reflect 1X value with delay
        lag_buffer = 0  # Reset lag count

    # Record data
    theta_4x.append(current_4x)
    theta_1x.append(current_1x)
    lagged_1x.append(delayed_1x)

    # Correctly combine 4X and delayed 1X to create 12-bit value
    # Combine the 2 bits of 1X (MSB) and 10 bits of 4X
    combined_value = (delayed_1x << 10) | current_4x  # 1X's MSB shifted to MSB of 12-bit combined, 4X in the rest of 10 bits
    combined.append(combined_value)

# Plotting
plt.figure(figsize=(10, 5))
plt.plot(theta_4x, label="4X (10bit)", linestyle='-', marker='o', markersize=1)
plt.plot(np.array(theta_1x) * (threshold_4x / threshold_1x), label="1X (Reference)", linestyle='--', marker='s', markersize=1)
plt.plot(np.array(lagged_1x) * (threshold_4x / threshold_1x), label=f"1X (Lag {lag_degrees}°)", linestyle='-', marker='x', markersize=1, color='r')
plt.plot(combined, label="Combined (12bit)", linestyle='-', marker='d', markersize=1, color='g')

plt.axhline(y=threshold_4x, color='gray', linestyle='dotted', label="90° (1023)")
plt.xlabel("Time (Steps)")
plt.ylabel("Angle (Unit: 4X)")
plt.legend()
plt.title(f"1X Phase Lag Simulation ({lag_degrees}° lag)")
plt.grid()
plt.show()
