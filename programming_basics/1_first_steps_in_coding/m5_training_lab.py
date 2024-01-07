w_length_meters = float(input())
h_width_meters = float(input())

w_length_centimeters = w_length_meters * 100
h_width_centimeters = h_width_meters * 100

corridor_centimeters = 100

h_width_centimeters_available = h_width_centimeters - corridor_centimeters

h_width = h_width_centimeters_available // 70
w_length = w_length_centimeters // 120

total_slots = h_width * w_length - 3

print(f"{total_slots:.0f}")
