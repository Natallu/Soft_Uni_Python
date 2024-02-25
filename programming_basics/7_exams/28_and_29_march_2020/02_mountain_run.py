import math

record_seconds = float(input())
distance_meters = float(input())
time_per_meter_seconds = float(input())

total_time = distance_meters * time_per_meter_seconds
additional_time = math.floor(distance_meters / 50) * 30
total_time += additional_time

if total_time < record_seconds:
    print(f"Yes! The new record is {total_time:.2f} seconds.")
else:
    missing_seconds = total_time - record_seconds
    print(f"No! He was {missing_seconds:.2f} seconds slower.")
