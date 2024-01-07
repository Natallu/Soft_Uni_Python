side_a = int(input())
side_b = int(input())
side_c = int(input())
accessories = float(input())

volume_aquarium = side_a * side_b * side_c

volume_aquarium_liters = volume_aquarium * 0.001
volume_accessories = accessories / 100

necessary_liters = volume_aquarium_liters * (1 - volume_accessories)

print(necessary_liters)
