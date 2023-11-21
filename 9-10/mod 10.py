'''
#1
class Elevator:
    def __init__(self, lower_floor, upper_floor):
        self.lower_floor = lower_floor
        self.upper_floor = upper_floor
        self.current_floor = lower_floor

    def go_to_floor(self, target_floor):
        if target_floor > self.current_floor:
            self.floor_up(target_floor)
        elif target_floor < self.current_floor:
            self.floor_down(target_floor)
        else:
            print(f'Elevator is already on floor {target_floor}')

    def floor_up(self, target_floor):
        while self.current_floor < target_floor and self.current_floor < self.upper_floor:
            self.current_floor += 1
            print(f'Your floor is: {self.current_floor}')

    def floor_down(self, target_floor):
        while self.current_floor > target_floor and self.current_floor > self.lower_floor:
            self.current_floor -= 1
            print(f'Your floor is: {self.current_floor}')

elevator = Elevator(lower_floor=1, upper_floor=10)
elevator.go_to_floor(6)

#2
class Elevator:
    def __init__(self, lower_floor, upper_floor):
        self.lower_floor = lower_floor
        self.upper_floor = upper_floor
        self.current_floor = lower_floor

    def go_to_floor(self, target_floor):
        if target_floor > self.current_floor:
            self.floor_up(target_floor)
        elif target_floor < self.current_floor:
            self.floor_down(target_floor)
        else:
            print(f'Elevator is already on floor {target_floor}')

    def floor_up(self, target_floor):
        while self.current_floor < target_floor and self.current_floor < self.upper_floor:
            self.current_floor += 1
            print(f'Your floor is: {self.current_floor}')

    def floor_down(self, target_floor):
        while self.current_floor > target_floor and self.current_floor > self.lower_floor:
            self.current_floor -= 1
            print(f'Your floor is: {self.current_floor}')
class Building:
    def __init__(self, lower_floor, upper_floor, num_elevators):
        self.lower_floor = lower_floor
        self.upper_flooe = upper_floor
        self.elevators = [Elevator(lower_floor,upper_floor) for i in range(num_elevators)]
    def run_elevator(self, elevator_number, target_floor):
        if 0 < elevator_number < len(self.elevators):
            elevator = self.elevators[elevator_number]
            elevator.go_to_floor(target_floor)
        else:
            print(f'Invalid elevator number: {elevator_number}')
builtins = Building(lower_floor= 1, upper_floor= 10, num_elevators= 3)
builtins.run_elevator(elevator_number= 1, target_floor= 3)

#3
class Elevator:
    def __init__(self, lower_floor, upper_floor):
        self.lower_floor = lower_floor
        self.upper_floor = upper_floor
        self.current_floor = lower_floor

    def go_to_floor(self, target_floor):
        if target_floor > self.current_floor:
            self.floor_up(target_floor)
        elif target_floor < self.current_floor:
            self.floor_down(target_floor)
        else:
            print(f'Elevator is already on floor {target_floor}')

    def floor_up(self, target_floor):
        while self.current_floor < target_floor and self.current_floor < self.upper_floor:
            self.current_floor += 1
            print(f'Your floor is: {self.current_floor}')

    def floor_down(self, target_floor):
        while self.current_floor > target_floor and self.current_floor > self.lower_floor:
            self.current_floor -= 1
            print(f'Your floor is: {self.current_floor}')
class Building:
    def __init__(self, lower_floor, upper_floor, num_elevators):
        self.lower_floor = lower_floor
        self.upper_flooe = upper_floor
        self.elevators = [Elevator(lower_floor,upper_floor) for i in range(num_elevators)]
    def run_elevator(self, elevator_number, target_floor):
        if 0 < elevator_number < len(self.elevators):
            elevator = self.elevators[elevator_number]
            elevator.go_to_floor(target_floor)
        else:
            print(f'Invalid elevator number: {elevator_number}')
class Alarm:
    def __init__(self, target_floor):
        self.target_floor = target_floor
        self.current_floor = 0
        self.lower_floor = 0
        self.alarm = 1

    def run_alarm(self):
        if self.alarm == 1:
            while self.current_floor > self.target_floor and self.current_floor > self.lower_floor:
                self.current_floor -= 1
            print(f'Alarm: You are on the floor: {self.current_floor}')
        else:
            print('Alarm: you are on a 0 floor')

alarm_instance = Alarm(target_floor=3)
alarm_instance.run_alarm()
'''




