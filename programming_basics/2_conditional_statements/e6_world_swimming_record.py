from math import floor

w_record_seconds = float(input())
distance_meters = float(input())
meter_per_seconds = float(input())

total_time_secs = distance_meters * meter_per_seconds
delay = floor(distance_meters / 15) * 12.5

final_time_secs = total_time_secs + delay

if final_time_secs < w_record_seconds:
    final = final_time_secs
    print(f"Yes, he succeeded! The new world record is {final:.2f} seconds.")
else:
    final = final_time_secs - w_record_seconds
    print(f'No, he failed! He was {final:.2f} seconds slower.')
