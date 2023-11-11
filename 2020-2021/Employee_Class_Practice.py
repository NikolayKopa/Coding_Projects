import datetime
class School():
    def __init__(self, lastname, firstname):
        self.lname = lastname
        self.fname = firstname
        self.email = firstname + "." + lastname + "@mcpsmd.net"
    def Student_Grad_Year(self, gradelevel):
        year = datetime.date.today().year
        month = datetime.date.today().month
        if month <= 6:
            grad_year = year + (12 - gradelevel)
        else:
            grad_year = year + (13 - gradelevel)
        return grad_year
student1 = School("Kopaliani", "Nick")
student2 = School("Smith", "Jack")

print(student1.Student_Grad_Year(8))
print(student2.Student_Grad_Year(9))

