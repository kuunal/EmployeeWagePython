import random

class Constant:
    __WAGE_PER_HOUR = 20  
    __FULL_DAY_HOUR = 8

    @property
    def WAGE_PER_HOUR(self):
        return self.__WAGE_PER_HOUR

    @property
    def FULL_DAY_HOUR(self):
        return self.__FULL_DAY_HOUR

class Employee:
    switcher = {}
    def check_employee(self):
        random_attendance = round(random.randint(0,2))
        switcher = {
            0 : self.calculate_fullday_wage(),
            1 : self.calculate_fullday_wage()//2,
            2 : "Absent"
        }
        return switcher.get(random_attendance, "Invalid Choice!")

    def calculate_fullday_wage(self):
        constant = Constant()
        return constant.WAGE_PER_HOUR * constant.FULL_DAY_HOUR

employee = Employee()
print(employee.check_employee())