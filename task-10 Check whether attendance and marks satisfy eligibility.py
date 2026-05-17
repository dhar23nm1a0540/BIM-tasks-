#Check whether attendance and marks satisfy eligibility
att=float(input("Enter attendence percentage(0.00):"))
marks=int(input("Enter marks:"))
if att>=75.00 and marks>=35:
    print("good")
else:
    print("need to work")
#print(att>=75.00 and marks>=35)