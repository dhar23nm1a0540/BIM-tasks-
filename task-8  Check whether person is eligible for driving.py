# Check whether person is eligible for driving
age=int(input("Enter age: "))
license=bool(input("Enter licensce availability(T/F): "))
if age>=18 and license==True :
  print("Eligible")
else: 
  print("not Eligible")
#print(age>=18 and license==True)