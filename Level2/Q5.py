temperature_readings = [25, 28, 21, 24, 27]

average_temperature = sum(temperature_readings) / len(temperature_readings)

highest_temperature = max(temperature_readings)
lowest_temperature = min(temperature_readings)

print(f"Average Temperature: {average_temperature}\nHighest Temperature: {highest_temperature}\nLowest Temperature: {lowest_temperature}")