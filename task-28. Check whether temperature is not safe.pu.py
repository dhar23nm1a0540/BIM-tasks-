#28. Check whether temperature is not safe
temp=int(input("enter the temperature: "))
if not (temp> 15 and temp< 40):
  print("not safe")
else:
  print("safe")