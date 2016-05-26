# 1. write a recursive function
# that takes one parameter: n
# and counts down from n
def countdown(n):
    if n <= 0:
        return []
    else:
        return [n] + countdown(n-1)
print(countdown(5))
