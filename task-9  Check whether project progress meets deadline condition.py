#Check whether project progress meets deadline condition
rem_days=int(input("Enter Remaining days: "))
prog_per=float(input("enter percentage: "))
if rem_days<=5 and prog_per>=80.00:
    print("good")
else:
    print("deadline is soon")

#print(rem_days<=5 and prog_per>=80.00)