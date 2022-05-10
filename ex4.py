cars = 100 #汽车
space_in_a_car = 4.0
drivers = 30 #司机
passengers = 90 #乘客
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * spacae_in_a_car
average_passengers_per_car = passengers / cars_driven

print("There are", cars , "cars available")
