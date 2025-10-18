import matplotlib.pyplot as plt
import numpy as np
import csv

time = []
altitude = []
velocity = []
acceleration = []
temperature = []

with open("telemetry_sample.csv", newline="") as csvfile:
    CSV_reader = csv.DictReader(csvfile)  
    for row in CSV_reader:
        time.append(int(row["time"]))
        altitude.append(int(row["alititude"]))
        velocity.append(int(row["velocity"]))
        acceleration.append(row["acceleration"])
        temperature.append(int(row["temperature"]))




