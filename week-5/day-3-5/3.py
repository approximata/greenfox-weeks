# Write a Person class that have a name and a birth_date property
# It should raise an error of the birthdate is less than 0 or more than 2016

class Person():

    def __init__(self):
        self.name = ''
        self.birth_date = 0

    def get_name(self):
        while True:
            try:
                self.name = str(input('what is your number\n'))
                print('your name is ' + self.name)
                break
            except ValueError:
                print('give me a string please')
    def get_birth_date(self):
        while True:
            try:
                self.birth_date = int(input('which year did you born?\n'))
                print('your born in', self.birth_date)
                break
            except ValueError:
                print('give me a valid integer number')


person1 = Person()
person1.get_name()
person1.get_birth_date()

print(person1.name, person1.birth_date)
