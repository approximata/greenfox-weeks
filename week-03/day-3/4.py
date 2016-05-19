# Create a student Class
# that has a method `add_grade`, that takes a grade from 1 to 5
# an other method `get_average`, that returns the average of the
# grades

class Student:
    def __init__(self):
        self.grade = 0
        self.gradelist = []

    def add_grade(self, grade):
        if self.grade > 5 and self.grade < 1 :
            print "wrong number"
        else:
            self.gradelist.append(grade)
        return self.gradelist

    def get_average(self):
        summy = 0.0
        for grade in self.gradelist:
            summy += grade
        averagemy = summy / len(self.gradelist)
        return(averagemy)

laci = Student()
jozsi = Student()
print(laci.add_grade(4))
print(jozsi.add_grade(3))
print(jozsi.add_grade(4))
print(jozsi.add_grade(5))
print(jozsi.add_grade(5))
print(jozsi.get_average())
