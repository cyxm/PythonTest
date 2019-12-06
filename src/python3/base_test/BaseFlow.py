# !/usr/bin/python3

varCondition = 0
if varCondition == 0:
    pass
elif varCondition == 1:
    pass
else:
    pass

while varCondition < 3:
    varCondition += 1
    print("while loop condition=%d" % varCondition)

while varCondition < 5:
    varCondition += 1
else:
    print("while condition=%d" % varCondition)

for i in range(0, 4):
    print("for loop i=%d" % i)

for i in ["index0", "index1"]:
    print("for loop i=%s" % i)
