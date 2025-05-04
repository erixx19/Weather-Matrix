# Weather-Matrix ☁️🌡️

With the help of my new project, you no more have to worry about the following when you're out there on a random walk —  
**"Damn, I should've brought my umbrella!"** ☔

😶‍🌫️ *For now, there's no visualization because of the obvious reason that I haven't learned that yet!*  
But **future updates will include visualizations using `matplotlib`** — so **STAY TUNED!**
------------
### 💡 Overview
A beginner-friendly Python project that simulates weather data for 10 global cities using NumPy, analyzes it, and exports it to a CSV file.  
The data includes temperature, humidity, and wind speed, along with simple analytics to identify trends.
-------
### 📌 Features

- ✅ Randomly generates realistic weather data (temperature, humidity, wind)
- ✅ Displays data in a clean table format using `tabulate`
- ✅ Computes average temperature, humidity, and wind speed
- ✅ Identifies the hottest and most humid city
- ✅ Exports the data to a `.csv` file for future use
------
### 🌍 Simulated Example of the Weather Report:

```
╒════════════╤═══════════════════╤═══════════════╤══════════════╕
│ City       │ Temperature (°C)  │ Humidity (%)  │ Wind (km/h)  │
╞════════════╪═══════════════════╪═══════════════╪══════════════╡
│ Delhi      │ 69.2              │ 67            │ 17.3         │
│ London     │ 22.4              │ 55            │ 8.1          │
│ ...        │ ...               │ ...           │ ...          │
╘════════════╧═══════════════════╧═══════════════╧══════════════╛
```
------
### 🔍 Analytics

- 🔥 **Hottest City**: Delhi (69.2°C 💀)  
- 💧 **Most Humid**: Rio (85%)  
- 📊 **Averages**: Temp = 29.4°C | Humidity = 64% | Wind = 13.8 km/h
-------
### 🧠 Concepts Used

- 🧮 `NumPy` for generating random data  
- 📋 `Tabulate` for clean CLI table formatting  
- 🧱 Python dictionaries and lists  
- 📁 File I/O using the `csv` module  
- 📈 Basic data analytics & sorting
-------
### 🛠️ How to Run?🤔

1. Install dependencies:
   ```bash
   pip install tabulate
   ```

2. Run the script:
   ```bash
   python weather_matrix.py
   ```
3. Check `weather_data.csv` for exported results.

---

### 🔗 Stay tuned for updates with pie charts and line graphs soon!
