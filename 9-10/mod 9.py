#1
'''
class car:
    def __init__(self, reg_number, max_speed):
        self.reg_number = reg_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.distance = 0
new_car = car('ABC-123', 142)
print('Reg number: ', new_car.reg_number)
print('Max speed: ', new_car.max_speed)
print('Сurrent speed: ', new_car.current_speed)
print('Distance: ', new_car.distance)

#2
class car:
    def __init__(self, reg_number, max_speed):
        self.reg_number = reg_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.distance = 0
    def acceleration(self, change_speed):
        if self.current_speed + change_speed >= 0:
            if self.current_speed + change_speed >= self.max_speed:
                self.current_speed += change_speed
            else:
                self.current_speed = self.max_speed
        else:
            self.current_speed = 0
new_car = car('ABC-123', 142)
new_car.acceleration(20)
new_car.acceleration(30)
new_car.acceleration(40)
print('Current speed', new_car.current_speed)

new_car.acceleration(-200)
print('Final speed', new_car.current_speed)

#3
class car:
    def __init__(self, reg_number, max_speed):
        self.reg_number = reg_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.distance = 0
    def acceleration(self, change_speed):
        if self.current_speed + change_speed >= 0:
            if self.current_speed + change_speed >= self.max_speed:
                self.current_speed += change_speed
            else:
                self.current_speed = self.max_speed
        else:
            self.current_speed = 0
    def drive(self, time):
        self.distance += self.current_speed * time
new_car = car('ABC-123', 142)
new_car.acceleration(20)
new_car.acceleration(30)
new_car.acceleration(40)
print('Current speed', new_car.current_speed)
new_car.drive(1.5)
print('Distanse', new_car.distance)
'''
#4
import random
import tabulate
class car:
    def __init__(self, reg_number):
        self.reg_number = reg_number
        self.max_speed = random.randint(100,200)
        self.current_speed = 0
        self.distance = 0
    def acceleration(self):
        change_speed = random.randint(-10,15)
        if self.current_speed + change_speed >= 0:
            if self.current_speed + change_speed >= self.max_speed:
                self.current_speed += change_speed
            else:
                self.current_speed = self.max_speed
        else:
            self.current_speed = 0
    def drive(self):
        self.distance += self.current_speed

cars = [car(f'ABC-{i}') for i in range (1,11)]
while all(car.distance < 10000 for car in cars):
    for car in cars:
        car.acceleration()
        car.drive()
data = [(car.reg_number,car.max_speed,car.distance) for car in cars]
distance = ['reg_number', 'max_speed','Distanse']
info = tabulate.tabulate(data, headers=distance, tablefmt='pretty')
print(info)