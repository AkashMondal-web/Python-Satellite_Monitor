import random
import time
import matplotlib.pyplot as plt

# Function to simulate telemetry data
def get_telemetry_data():
    temperature = random.uniform(-30, 50)  # Simulate temperature in Celsius
    battery_level = random.uniform(0, 100)  # Simulate battery level percentage
    return temperature, battery_level

# Function to visualize the data
def plot_data(temperature_data, battery_data):
    plt.subplot(2, 1, 1)
    plt.plot(temperature_data, label='Temperature (\u00b0C)')
    plt.title('Satellite Telemetry Data')
    plt.xlabel('Time')
    plt.ylabel('Temperature (\u00b0C)')
    plt.grid(True)
    plt.legend()

    plt.subplot(2, 1, 2)
    plt.plot(battery_data, label='Battery Level (%)', color='r')
    plt.xlabel('Time')
    plt.ylabel('Battery Level (%)')
    plt.grid(True)
    plt.legend()

    plt.tight_layout()
    plt.show()

# Main function
def monitor_satellite():
    temperature_data = []
    battery_data = []

    for i in range(100):  # Simulating 100 data points (e.g., 100 seconds)
        temperature, battery_level = get_telemetry_data()
        temperature_data.append(temperature)
        battery_data.append(battery_level)

        if temperature > 40:
            print(f"Alert: High temperature detected! {temperature:.2f}°C")
        if battery_level < 20:
            print(f"Alert: Low battery detected! {battery_level:.2f}%")

        time.sleep(1)  # Wait for 1 second before next data point

    # Plot the data after collecting it
    plot_data(temperature_data, battery_data)

# Corrected line: use __name__ == "__main__"
if __name__ == "__main__":
    monitor_satellite()
