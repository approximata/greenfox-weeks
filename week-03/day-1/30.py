ac = 8
time = 120
out = ''
# if ac is dividable by 4
# and time is not more than 200
# set out to 'check'
# if time is more than 200
# set out to 'Time out'
# otherwise set out to 'Run Forest Run!'
if (ac % 4 == 0 and time <=200):
    out = "check"
elif time > 200:
    out = "time out"
else:
    out="run Forest"
print (out)

if time > 200:
    out = "Time out"
elif ac % 4 == 0:
    out = "check"
else:
    out = "run forest"
print (out)
