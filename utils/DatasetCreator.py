from faker import Faker
import csv
import random

faker = Faker()

num_data_points = 10000

sensor_numbers = list(range(1, 11))
temperature_ranges = [(0, 100), (-20, 60), (0, 50)]

def assign_fault_type(temperature):
    if temperature > 90:
        return 'Hard Fault'
    elif temperature > 70:
        return 'Spike and Bias Fault'
    elif temperature < 5:
        return 'Drift Fault'
    elif temperature < 20:
        return 'Soft Fault'
    else:
        return 'No Fault'
    
with open('Datasets/fake_temperature_data.csv', 'w', newline='') as csvfile:
    fieldnames = ['Sensor No.', 'Temperature', 'Fault Type']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    # Generate and write fake data points to the CSV file
    for _ in range(num_data_points):
        sensor_no = random.choice(sensor_numbers)
        temp_range = random.choice(temperature_ranges)
        temperature = faker.random_int(min=temp_range[0], max=temp_range[1], step=1)
        fault_type = assign_fault_type(temperature)

        writer.writerow({
            'Sensor No.': sensor_no,
            'Temperature': temperature,
            'Fault Type': fault_type
        })

print("Fake sensor data generated and saved to 'Datasets/fake_temperature_data.csv'")