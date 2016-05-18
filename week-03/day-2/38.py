numbers = [7, 5, 8, -1, 2]
# Write a function that returns the minimal element
# in a list (your own min function)
def mymin(nu):
    minnum=nu[0]
    for i in range(len(nu)):
        if minnum < nu[i]:
            pass
        else:
            minnum = nu[i]
    return minnum
print(mymin(numbers))
