# 3. Given a non-negative int n,
# return the sum of its digits recursively (no loops).
# Note that mod (%) by 10 yields the rightmost digit (126 % 10 is 6),
# while divide (/) by 10 removes the rightmost digit (126 / 10 is 12).
def addnumbers(n):
    if n // 10 == 0:
        return n
    else:
        return  n % 10 + addnumbers(n // 10)
print(addnumbers(328))
