import random

class Constant:
    _WAGE_PER_HOUR = 20  
    _FULL_DAY_HOUR = 8

    @property
    def WAGE_PER_HOUR(self):
        return self._WAGE_PER_HOUR

    @property
    def FULL_DAY_HOUR(self):
        return self._FULL_DAY_HOUR

class Employee:
    def check_employee(self):
        random_attendance = round(random.random())
        if random_attendance == 1:
            print("Employee is present")
            print("Full day wage is :",self.calculate_fullday_wage())
        else:
            print("Employee is absent") 

    def calculate_fullday_wage(self):
        constant = Constant()
        return constant.WAGE_PER_HOUR * constant.FULL_DAY_HOUR

employee = Employee()
employee.check_employee()