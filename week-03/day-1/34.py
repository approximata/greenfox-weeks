ag = [3, 4, 5, 6, 7]

for n in range(len(ag)):
    ag[n] *= 2
print(ag)

n=0
while len(ag) > n:
    ag[n] *= 2
    n +=1
print(ag)
