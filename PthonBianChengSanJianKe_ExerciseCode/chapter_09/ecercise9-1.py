# -*-coding:utf-8 -*-
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"The restaurant's name is {self.restaurant_name}.\n",
            f"It's cuisine type is {self.cuisine_type}.")
    def open_restaurant(self):
        print(f"\n{self.restaurant_name} restaurant is in operation.")


restaurant1 = Restaurant("博白", "中餐")

print(f"name: {restaurant1.restaurant_name}. Type: {restaurant1.cuisine_type}")

restaurant1.describe_restaurant()
restaurant1.open_restaurant()