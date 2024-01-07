x_house_height = float(input())
y_length_side_wall = float(input())
h_roof_height_triangle = float(input())

door_sqm = 1.2 * 2
window_sqm = 1.5 * 1.5

front_and_back_walls_sqm = 2 * (x_house_height * x_house_height) - door_sqm
side_walls_sqm = 2 * (x_house_height * y_length_side_wall) - 2 * window_sqm
total_green_area_sqm = front_and_back_walls_sqm + side_walls_sqm

green_paint_liters = total_green_area_sqm / 3.4

roof_triangles = 2 * (x_house_height * h_roof_height_triangle / 2)
roof_rectangles = 2 * (x_house_height * y_length_side_wall)
total_red_area = roof_rectangles + roof_triangles

red_paint_liters = total_red_area / 4.3

print(f"{green_paint_liters:.2f}")
print(f"{red_paint_liters:.2f}")
