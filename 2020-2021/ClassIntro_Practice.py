class Triangle():
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
    def forms_triangle(self, side1, side2, side3):
        if side1 + side2 > side3:
            self.check_type(side1, side2, side3)
        else:
            print("This is not a possible triangle.")
    def check_type(self, side1, side2, side3):
        if side1 == side2 or side2 == side3 or side1 == side3:
            if side1 == side2 and side2 == side3:
                print("This triangle is Equilateral.")
            else:
                print("This triangle is Isosceles.")
        if side1 != side2 and side1 != side3:
            print("This triangle is Scalene.")


t1 = Triangle(7,10,5)
t2 = Triangle(6,6,6)
t3 = Triangle(5,5,4)

t1.forms_triangle(7,10,5)
t2.forms_triangle(6,6,6)
t3.forms_triangle(5,5,4)
