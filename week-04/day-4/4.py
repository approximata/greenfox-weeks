# 4. Given base and n that are both 1 or more, compute recursively (no loops)
# the value of base to the n power, so powerN(3, 2) is 9 (3 squared).
def power(x, n):
    if n <= 2:
        return x * x
    else:
        return x * power(x, n-1)
print(power(2, 4))
