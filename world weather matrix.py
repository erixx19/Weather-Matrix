import numpy as np
from tabulate import tabulate
import csv

# List of cities for simulation
cities = [
    "Delhi", "London", "Tokyo", "New York", "Sydney",
    "Berlin", "Moscow", "Cairo", "Rio", "Toronto"
]

# Generate simulated weather data
def generate_weather_data(cities):
    num_cities = len(cities)
    temps = np.round(np.random.uniform(10, 45, num_cities), 1)  # °C
    humidity = np.random.randint(20, 90, num_cities)            # %
    wind = np.round(np.random.uniform(5, 25, num_cities), 1)    # km/h
    
    weather_data = []
    for i in range(num_cities):
        weather_data.append({
            "City": cities[i],
            "Temperature": temps[i],
            "Humidity": humidity[i],
            "Wind": wind[i]
        })
    return weather_data

# Display in a tabular format
def display_weather_table(weather_data):
    headers = ["City", "Temperature (°C)", "Humidity (%)", "Wind (km/h)"]
    table = [[
        entry["City"], entry["Temperature"], entry["Humidity"], entry["Wind"]
    ] for entry in weather_data]
    print("\n🌍 Simulated Weather Report\n")
    print(tabulate(table, headers=headers, tablefmt="fancy_grid"))

# Compute basic analytics
def compute_analytics(weather_data):
    hottest = max(weather_data, key=lambda x: x['Temperature'])
    humid = max(weather_data, key=lambda x: x['Humidity'])
    
    avg_temp = round(np.mean([d['Temperature'] for d in weather_data]), 2)
    avg_humid = round(np.mean([d['Humidity'] for d in weather_data]), 2)
    avg_wind = round(np.mean([d['Wind'] for d in weather_data]), 2)

    print("\n🔍 Analytics:")
    print(f"- Hottest City: {hottest['City']} ({hottest['Temperature']}°C)")
    print(f"- Most Humid: {humid['City']} ({humid['Humidity']}%)")
    print(f"- Avg Temp: {avg_temp}°C | Avg Humidity: {avg_humid}% | Avg Wind: {avg_wind} km/h")

# Export to CSV
def export_to_csv(weather_data, filename="weather_data.csv"):
    keys = weather_data[0].keys()
    with open(filename, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(weather_data)
    print(f"\n✅ Data exported to {filename}")

# Main function to run all
if __name__ == "__main__":
    data = generate_weather_data(cities)
    display_weather_table(data)
    compute_analytics(data)
    export_to_csv(data)
