class Person:
    def __init__(self, name, money, mood, health_rate):
        self.name = name
        self.money = money
        self.mood = mood
        self.health_rate = health_rate

    # Methods in Person
    def sleep(self, sleep_hours):
        if sleep_hours == 7:
            self.mood = 'happy'
        elif sleep_hours < 7:
            self.mood = 'tired'
        else:
            self.mood = 'lazy'

    def eat(self, number_of_meals):
        if number_of_meals == 3:
            self.health_rate = '100%'
        elif number_of_meals == 2:
            self.health_rate = '75%'
        elif number_of_meals == 1:
            self.health_rate = '50%'

    def buy(self, items):
        self.money -= items * 10


class Employee(Person):
    def __init__(self, id, car, email, salary, distance_to_work, name, money, mood, health_rate):
        super().__init__(name, money, mood, health_rate)
        self.id = id
        self.email = email
        self.salary = salary
        self.distance_to_work = distance_to_work
        self.car = car

    # Methods in Employee
    def drive(self, distance):
        self.car.run(distance, self.car.velocity)

    def work(self, work_hours):
        if work_hours == 8:
            self.mood = 'happy'
        elif work_hours > 8:
            self.mood = 'tired'
        else:
            self.mood = 'lazy'

    def refuel(self, gasAmount=100):
        self.car.fuelRate += gasAmount
        if self.car.fuelRate > 100:
            print('fuelRate cannot be greater than 100')

    def send_mail(self, message):
        print(f"Sending email to {self.email}: {message}")


class Car:
    def __init__(self, name, fuelRate, velocity):
        self.name = name
        self.fuelRate = fuelRate
        self.velocity = velocity

    @property
    def fuelRate(self):
        return self._fuelRate

    @fuelRate.setter
    def fuelRate(self, value):
        if value < 0:
            self._fuelRate = 0
        elif value > 100:
            self._fuelRate = 100
        else:
            self._fuelRate = value

    @property
    def velocity(self):
        return self._velocity

    @velocity.setter
    def velocity(self, value):
        if value < 0:
            self._velocity = 0
        elif value > 200:
            self._velocity = 200
        else:
            self._velocity = value

    def run(self, distance, velocity):
        self.velocity = velocity
        fuel_consumed = (distance // 10) * 0.10 * self.fuelRate
        self.fuelRate -= fuel_consumed
        if self.fuelRate <= 0:
            self.fuelRate = 0
            remaining_distance = distance - ((self.fuelRate + fuel_consumed) / (0.10 * self.fuelRate)) * 10
            self.stop(remaining_distance)
        else:
            self.stop(0)

    def stop(self, remain_distance):
        if remain_distance > 0:
            print(f"Stopped due to lack of fuel. Remaining distance: {remain_distance} km")
        else:
            print("Arrived at destination.")

class Office:
    employeesNum = 0
    def __init__(self, name):
        self.name = name
        self.employees = []

    @classmethod
    def change_emps_num(cls, num):
        cls.employeesNum = num

    def get_all_employees(self):
        return self.employees

    def get_employee(self, empId):
        for emp in self.employees:
            if emp.id == empId:
                return emp
        return None

    def hire(self, employee):
        self.employees.append(employee)
        Office.employeesNum += 1

    def fire(self, empId):
        emp = self.get_employee(empId)
        if emp:
            self.employees.remove(emp)
            Office.employeesNum -= 1

    def deduct(self, empId, deduction):
        emp = self.get_employee(empId)
        if emp:
            emp.salary -= deduction

    def reward(self, empId, reward):
        emp = self.get_employee(empId)
        if emp:
            emp.salary += reward

    def check_lateness(self, empId, moveHour):
        emp = self.get_employee(empId)
        if emp:
            targetHour = 9

            travelTime = emp.distance_to_work / emp.car.velocity
            arrivalTime = moveHour + travelTime
            if arrivalTime > targetHour:
                print(f"{emp.name} is late! Arrival time: {arrivalTime}")
            else:
                print(f"{emp.name} arrived on time. Arrival time is : {arrivalTime}")
fiat_128 = Car(name="Fiat 128", fuelRate=100, velocity=60)
samy = Employee(name='samy',id=1, car=fiat_128,email="samy@example.com",salary=5000,distance_to_work=20,
                money=1000, mood="happy",health_rate=100)
iti_office = Office(name="ITI Smart Village")
iti_office.hire(samy)
samy.drive(samy.distance_to_work)
iti_office.check_lateness(empId=1, moveHour=8)