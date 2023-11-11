class Introduction:
    Intro = "My name is "
    def __init__(self, lname, fname):
        self.lname = lname
        self.fname = fname
    def intro(self):
        return self.Intro + self.fname + " " + self.lname
Introduction = Introduction("Kopaliani", "Nick")
print(Introduction.intro())
