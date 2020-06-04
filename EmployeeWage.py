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
    def check_employee(self):
        random_attendance = round(random.randint(0,2))
        if random_attendance == 1:
            print("Employee is present")
            print("Full day wage is :",self.calculate_fullday_wage())
        elif random_attendance == 2:
            print("Emplyee is working part time")
            print("Part time wage is :",self.calculate_fullday_wage()//2)
        else:
            print("Employee is absent") 

    def calculate_fullday_wage(self):
        constant = Constant()
        return constant.WAGE_PER_HOUR * constant.FULL_DAY_HOUR

employee = Employee()
employee.check_employee()