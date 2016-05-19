# Create a new class called `Person` that has a first_name and a last_name (takes it in it's constructor)
# It should have a `greet` method that prints it's full name

# Create a `Student` class that is the child class of `Person`
# it should have a method to add grades
# it should have a `salute` method that prints it's full name and the average of it's grades as well

class Person():

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def greet(self):
        return 'hello' + " " + self.first_name + " " + self.last_name

class Student(Person):

    gradelist = []
    def add_grade(self, grade):
        self.gradelist.append(grade)
        return self.gradelist

    def get_average(self):
        summy = 0.0
        for grade in self.gradelist:
            summy += grade
        averagemy = summy / len(self.gradelist)
        return(averagemy)

    def salute(self):
        print(self.greet())



mat = Person('Mate', 'Bodor')
print(mat.greet())

matka = Student('Bela', 'Talan')
matka.salute()
matka.add_grade(4)
matka.add_grade(3)
print(matka.get_average())
