# -*-coding: utf-8 -*-
"""汽车类"""
class Car:
    """一次模拟汽车的简单尝试。"""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0  # 里程

    def get_descriptive_name(self):
        """返回整洁的描述信息。"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """打印一条指出汽车里程的消息。"""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print("You can't roll back an odometer!")


class ElectricCar(Car):
    """电动车的独特之处。"""
    def __init__(self, make, model, year):
        """
        初始化父类的属性。
        再初始化电动汽车特有的属性。
        """
        super().__init__(make, model, year)
        # self.battery_size = 75
        self.battery = Battery()

    # def describe_battery(self):
    #     print(f"This car has a {self.battery_size}-kwh battery.")

class Battery:
    """电瓶类"""
    def __init__(self, battery_size=75):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kwh battery.")

    def get_range(self):
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f"This car can go about {range} miles on a full charge.")

# my_tesla = ElectricCar('tesla', 'model y', 2019)
# print(my_tesla.get_descriptive_name())
# my_tesla.battery.describe_battery()
# my_tesla.battery.get_range()
# my_new_car = Car('audi', 'a4', 2019)
# print(my_new_car.get_descriptive_name())
# my_new_car.update_odometer(33)
# my_new_car.read_odometer()
# my_new_car.update_odometer(20)

# my_new_car.increment_odometer(0)
# my_new_car.read_odometer()