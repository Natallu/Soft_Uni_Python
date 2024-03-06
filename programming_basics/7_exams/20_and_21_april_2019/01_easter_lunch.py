easter_bread_num = int(input())
eggs_num = int(input())
cookies_num = int(input())

color_eggs = eggs_num * 12 * 0.15
products = easter_bread_num * 3.20 + eggs_num * 4.35 + cookies_num * 5.40 + color_eggs

print(f"{products:.2f}")
