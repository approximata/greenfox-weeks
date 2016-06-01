# Write a Person class that have a name and a birth_date property
# It should raise an error of the birthdate is less than 0 or more than 2016

class Person():
    def __init__(self, name, birth_date):
        self.name = name
        if int(birth_date) < 0 or int(birth_date) > 2016:
            raise ValueError('The year must be an integer between 0 and 2016')
        else:
            self.birth_date = birth_date

try:
    person2 = Person('Zolu', 2010)
    print(person2.name, person2.birth_date)
    person1 = Person('Jani', 2018)


except ValueError:
    print('Something wrong with the birth date')
