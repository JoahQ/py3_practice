# -*- utf-8 -*-
# from car import Car,ElectricCar

# my_car = Car('audi', 'a4', 2022)
# print(my_car.get_descriptive_name())

# my_car.odometer_reading = 23
# my_car.read_odometer()

# # from car import ElectricCar

# my_byd = ElectricCar('byd', '唐pro', 2023)

# print(my_byd.get_descriptive_name())
# my_byd.battery.describe_battery()
# my_byd.battery.get_range()

import car

my_car = car.Car('audi', 'a4', 2022)
print(my_car.get_descriptive_name())

my_car.odometer_reading = 23
my_car.read_odometer()


my_byd = car.ElectricCar('byd', '唐pro', 2023)

print(my_byd.get_descriptive_name())
my_byd.battery.describe_battery()
my_byd.battery.get_range()