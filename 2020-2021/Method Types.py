import datetime
class Employee:
    company_perform = 3
    def __init__(self, experience):
        self.experience = experience
    @classmethod
    def employ_bonus_perform(cls):
        cls.company_perform*= 3
        return("With the company performance, the employee bonus is "+ str(cls.company_perform))
    @staticmethod
    def weekday_weekend(day_of_week):
        if day_of_week == 6 or day_of_week == 7:
            return ("Today is a weekend")
        else:
            return ("Today is a weekday!")
    def employ_bonus_experience(self):
        employee_bonus = self.experience*6
        return ("With the employee's experience, the employee bonus is "+ str(employee_bonus))

Calvin = Employee(4)
print(Calvin.employ_bonus_experience())
print(Calvin.employ_bonus_perform())
day_of_week = datetime.datetime.today().weekday()
print(Calvin.weekday_weekend(day_of_week))
Kieth = Employee(7)
print(Kieth.employ_bonus_experience())
print(Kieth.employ_bonus_perform())
day_of_week = datetime.datetime.today().weekday()
print(Kieth.weekday_weekend(day_of_week))
