import datetime
#Parent Class with the two methods I used in the two subclasses.
class School():
    def __init__(self, first_name, last_name, date_birth, email):
        self.first_name = first_name
        self.last_name = last_name
        self.date_birth = date_birth
        self.email = first_name + '.' + last.name + '@mcpsmd.org'
    def reportcard_week(self, quarter):
        return("This week is when the report cards for quarter" + str(quarter) + "are coming out!")
    def school_arrival(self):
        weekend_weekday = datetime.datetime.today().weekday()
        if weekend_weekday == 6 or weekend_weekday == 7:
            return ("Today is a weekend.")
        else:
            return ("Today is a weekday.")
#Here I have to more methods that are only special to this program. Then I put the two methods from the parent class here, which is method overriding, since I changed a part of the two methods.
#I also put School inside the Student subclass' parentheses since this allows it to inherit everything from the School parent class. The same thing is done with the other subclass.
class Student(School):
    def __init__(self, grade, course, average_grade):
        self.grade = grade
        self.course = course
        self.average_grade = average_grade
    def graduation_year(self, grade):
        year = datetime.date.today().year
        month = datetime.date.today().month
        if month <= 6:
            grad_year = year + (12 - grade)
        else:
            grad_year = year + (13 - grade)
        return ("You will graduate in " + str(grad_year) + ".")
    def homework_help_grade(self, average_grade):
        if average_grade == "A":
            student_help_time = 0
        if average_grade == "B" or average_grade == "C":
            student_help_time = 60
        if average_grade == "D" or average_grade == "F":
            student_help_time = 120
        return ("The amount of help this student needs is " + str(student_help_time) + " minutes.")
    def reportcard_week(self, quarter):
        return("This week is when the report cards for quarter " + str(quarter) + " are coming out! Make sure you complete and turn in all your work!")
    def school_arrival(self):
        weekend_weekday = datetime.datetime.today().weekday()
        if weekend_weekday == 6 or weekend_weekday == 7:
            return ("Today is a weekend. You can hangout with your friends!")
        else:
            return ("Today is a weekday. Looks like you have to go to school.")
#I did the same thing as I did in the other subclass.
class Staff(School):
    def __init__(self, position, years_at_school):
        self.position = position
        self.years_at_school = years_at_school
    def pay_according_position(self, position):
        if position == "principal":
            pay = 109000
        if position == "vice principal":
            pay = 70000
        if position == "teacher":
            pay = 61000
        if position == "school counselor":
            pay = 65000
        if position == "janitor":
            pay == 39000
        return ("The salary for this staff member is " + str(pay) + ".")
    def started_working(self, years_at_school):
        year = datetime.date.today().year
        started_year = year - years_at_school
        return ("This staff member started working at this school in " + str(started_year) + ".")
    def reportcard_week(self, quarter):
        return("This week is when the report cards for quarter " + str(quarter) + " are coming out! Make sure you grade all your student's work!")
    def school_arrival(self):
        weekend_weekday = datetime.datetime.today().weekday()
        if weekend_weekday == 6 or weekend_weekday == 7:
            return ("Today is a weekend. You can relax.")
        else:
            return ("Today is a weekday. Looks like you have to go to work!")

#Here I call the two subclasses, each with two objects.
Student1 = Student("Nick", "Math", "A")
print(Student1.graduation_year(8), Student1.homework_help_grade("A"), Student1.reportcard_week(2), Student1.school_arrival())
Student2 = Student("Keith", "English", "C")
print(Student2.graduation_year(6), Student2.homework_help_grade("C"), Student2.reportcard_week(2), Student2.school_arrival())
Staff1 = Staff("Jackson", 10)
print(Staff1.pay_according_position("teacher"), Staff1.started_working(10), Staff1.reportcard_week(3), Staff1.school_arrival())
Staff2 = Staff("Sally", 4)
print(Staff2.pay_according_position("principal"), Staff2.started_working(4), Staff2.reportcard_week(3), Staff2.school_arrival())
