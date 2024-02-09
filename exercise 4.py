maths = int(input("input maths"))
eng = int(input("input English"))
physics = int(input("input pyhsics"))
chem = int(input("input chem"))
geo = int(input("input geo"))

if maths and eng and physics and chem and geo < 0:
    print("invalid")
if maths or eng or physics or chem or geo > 100:
    print("invalid")
average = ((maths + eng + physics + chem + geo)/5)
print(average)
if average < 40:
    print("E")
elif average > 39 < 50:
    print("D")
elif average > 51 < 61:
    print("C")
elif average > 60 < 71:
    print("B")
else:
    print("A")
