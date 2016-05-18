ae = 'Jozsi'
# create a function that greets ae
def greet31(ae="valaki"):
    return 'Haliho, ' +ae

print(greet31(ae))

def greet_by_name(name):
  print("Szia,", name)

greet_by_name("Tojas")
greet_by_name("Barbi")


def make_green(name):
  new_name = "Zold " + name
  return new_name

name = make_green("Tojas")
greet_by_name(name)

def greet(greet="Szia", name="Valaki"):
  print(greet, name)

greet("hello", "Tojas")
greet("szevasz", "Barbi")
greet("csa")
greet(name="Mindenki")

def make_green(name):
  new_name = "Zold " + name
  return new_name

name = make_green("Tojas")
greet_by_name(name)
