import datetime 
class Employee():
   companyProfits = 1000
   def init(self, name, experience):
     self.name = name
     self.experience = experience

   def bonus(self):
     return self.experience*100
   @classmethod
   def companyBonus(cls):
     if cls.companyProfits >= 100:
       return True
     else:
       return False
   @staticmethod
   def day():
     if datetime.date.today().weekday() >= 5:
        return "weekend"
     else:
        return "weekday"

employee1 = Employee("John", 4)
print(employee1.bonus())
# 400
print(employee1.companyBonus())
# true
print(employee1.day())
# weekday
employee2 = Employee("Sara", 2)
print(employee2.bonus())
# 200
print(employee2.companyBonus())
# true
print(employee2.day())
