import random

class Constant:
    __WAGE_PER_HOUR = 20  
    __FULL_DAY_HOUR = 8
    __MONTHLY_WORKING_DAY = 20

    @property
    def WAGE_PER_HOUR(self):
        return self.__WAGE_PER_HOUR

    @property
    def FULL_DAY_HOUR(self):
        return self.__FULL_DAY_HOUR

    @property
    def MONTHLY_WORKING_DAY(self):
        return self.__MONTHLY_WORKING_DAY


class Employee:
    constant = Constant()
    def check_employee(self):
        random_attendance = round(random.randint(0,2))
        switcher = {
            0 : self.calculate_fullday_wage(),
            1 : self.calculate_fullday_wage()//2,
            2 : 0
        }
        return switcher.get(random_attendance, -1)

    def calculate_fullday_wage(self):
        return self.constant.WAGE_PER_HOUR * self.constant.FULL_DAY_HOUR

    def calculate_monthly_wage(self):
        monthly_wage = 0
        for days in range(self.constant.MONTHLY_WORKING_DAY):
            monthly_wage += int(self.check_employee())
        print(f'Monthly wage is {monthly_wage}') 

employee = Employee()
print(employee.check_employee())
print(employee.calculate_monthly_wage())