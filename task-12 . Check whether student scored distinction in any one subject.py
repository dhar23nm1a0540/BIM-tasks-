#Check whether student scored distinction in any one subject
list=[90,87,65]
x=0
for i in range(3):
    if list[i] >= 75:
      x=x+1

if x>0:
   print("Distinction")