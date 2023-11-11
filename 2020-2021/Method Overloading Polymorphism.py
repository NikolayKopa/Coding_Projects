class Employee: 
    def __init__(self):
         self.list_of_people = []
    def add_people(self, *people_to_add):
        for person in people_to_add:
            self.list_of_people.append(person)
class School:
    def __init__(self):
        self.list_of_people = []
    def add_people(self, *people_to_add):
        for person in people_to_add:
            self.list_of_people.append(person)
Employee = Employee()
School = School()
Employee.add_people(["Andrew", "Liam", "Josh"])
School.add_people(["Andrew", "Liam", "Josh"])
print(Employee.list_of_people)
print(School.list_of_people)

