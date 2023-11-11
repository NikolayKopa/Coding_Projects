class Employee:
    '''This is a super class '''
    bonus_raise = 1.02
    def __init__(self,emp_id,first,last,pay,pos):
        self.employee_id = emp_id
        self.fname = first
        self.lname = last
        self.pay = pay
        self.pos = pos
        self.email = first +'.' + last + '@cmp.org'
        
    def fullname(self):
            return ('{} , {} : {}'.format(self.fname, self.lname,self.pos))
        
    
    def bonuspay(self):
        pay_with_bonus =  self.pay * self.bonus_raise
        return pay_with_bonus



class Developer(Employee):
    ''' This is a sub class of Employee class. Bonus_raise class variable is redefined here'''
    bonus_raise = 1.04
    def __init__(self, parent ,prog_lang):   # while creating an instance use the Employee instance (parent's instance) in place of parent
         # to let the superclass  (parent class) handle these attributes)
        super().__init__(parent.employee_id,parent.fname,parent.lname,parent.pay, parent.pos)   
        
        #Employee.__init__(self,parent.employee_id,parent.fname,parent.lname,parent.pay, parent.pos)              # another way to call parent init method
        self.prog_lang = prog_lang
        
    def fullname(self):    # Method overriding - Redefining fullname method defined in it's parent class
        return ('Developer : {} , {} '.format(self.fname, self.lname))
  
class Manager(Employee):
    
    def __init__(self, parent,employees=[] ):
      super().__init__(parent.employee_id,parent.fname, parent.lname, parent.pay, parent.pos)
      self.employees = employees
      
    def add_emp(self, empl_id):
      if empl_id not in self.employees:
        self.employees.append(empl_id)
      
    def remove_emp(self, empl_id):
      if empl_id in self.employees:
        self.employees.remove(empl_id)
    
       
# ##########      To print Method resolution order ################
#print(help(Developer))

###########     To print docstring  ###############
#print(Developer.__doc__)

####### Instances    #################
emp1 = Employee("E1","John","Smith",90000,"Programmer Analyst")
print(emp1.fullname())

emp2 = Employee("M1","Joe","Bill",90000,"Project Manager")

dev1= Developer(emp1,"Python")
# The method is in parent class but the value of the class variable used is from it's own class
print("Bonus Raise 1.04 is used : ",dev1.bonuspay())
# method is from it's own class (the same method is available in parent class as well) -> Method overriding
print("Method in base class : ",dev1.fullname())  


m1 = Manager(emp2,["E1"])
#the method and the class variable is from parent class
print("Bonus Raise 1.02 is used : ",m1.bonuspay())
m1.add_emp("E2")
print(m1.employees)
m1.remove_emp("E2")
print(m1.employees)

