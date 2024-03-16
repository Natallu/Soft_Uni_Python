country = input()
apparatus = input()

difficulty_score = 0
performance_score = 0

if country == "Russia":
    if apparatus == "ribbon":
        difficulty_score = 9.100
        performance_score = 9.400
    elif apparatus == "hoop":
        difficulty_score = 9.300
        performance_score = 9.800
    elif apparatus == "rope":
        difficulty_score = 9.600
        performance_score = 9.000
elif country == "Bulgaria":
    if apparatus == "ribbon":
        difficulty_score = 9.600
        performance_score = 9.400
    elif apparatus == "hoop":
        difficulty_score = 9.550
        performance_score = 9.750
    elif apparatus == "rope":
        difficulty_score = 9.500
        performance_score = 9.400
elif country == "Italy":
    if apparatus == "ribbon":
        difficulty_score = 9.200
        performance_score = 9.500
    elif apparatus == "hoop":
        difficulty_score = 9.450
        performance_score = 9.350
    elif apparatus == "rope":
        difficulty_score = 9.700
        performance_score = 9.150

total_score = difficulty_score + performance_score
percentage_needed = ((20 - total_score) / 20) * 100

print(f"The team of {country} get {total_score:.3f} on {apparatus}.")
print(f"{percentage_needed:.2f}%")
