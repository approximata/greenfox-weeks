# Create a function that prints a triangle like this:
#   *
#   **
#   ***
#   ****
#   *****
#   ******
# It should take a number as parameter that describes how many lines the triangle has

firstletter = '*'

def stars(char):
    for i in range(8):
        print i * char


stars(firstletter)
