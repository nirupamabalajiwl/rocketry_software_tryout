#Imported libraries for dataset
import math 
import csv
import random 

def create_data (filename="data/telemetry_sample.csv"):
    with open (filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["time","altitude", "velocity","acceleration","temperature"]) #assuming this is the format of the data
        altitude, velocity  = 0,0

    #based on acceleration stages/flight phases in this case Launch = (0-9s), Coast (10-59s), and Descent (60-119s)
        for t in range (0,120):
            if t < 10:
                acceleration = 30 - t*2
            elif t<60:
                acceleration = -9.8 + random.uniform (-1,1)
            else:
                acceleration = -9.8 + (t-60) * 0.1

        velocity += acceleration * 0.1
        altitude += velocity *0.1
        if altitude < 0:
            altitude = 0

        temperature = 20 - 0.02 * altitude + random.uniform(-0.5,0.5)
        writer.writerow([t, altitude, velocity, acceleration, temperature])


if __name__ == "__main__":
    create_data()