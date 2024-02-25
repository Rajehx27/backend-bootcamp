class Plant:
    def __init__(self, likes_sun, water_need, likes_wind, deadly_snow):
        self.likes_sun = likes_sun
        self.water_need = water_need
        self.likes_wind = likes_wind
        self.deadly_snow = deadly_snow


plant1 = Plant(True, 25, False, 90)
plant2 = Plant(True, 60, True, 40)
plant3 = Plant(False, 4, True, 1750)
plants = [plant1, plant2, plant3]

print("describe the weather today please:")
is_sun = int(input("is it sun? (True/False): "))
precipitation_num = int(input("what is the precipitation number: "))
is_wind = int(input("is it wind? (True/False): "))

for i, p in enumerate(plants):
    if is_sun == p.likes_sun and precipitation_num >= p.water_need and is_wind == p.likes_wind:
        print(f"plant {i + 1} is having a good day")

snow_num = int(input("what the amount of snow today ?  "))

for i, p in enumerate(plants):
    if snow_num >= p.deadly_snow:
        print(f"plant {i + 1} is dead due to the snow")
