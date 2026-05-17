#Check whether entered value is between two ranges
print("Enter the range(max,min)")
max=int(input('enter max: '))
min=int(input('enter min: '))
x=int(input('Enter a number: '))
if x>=min and x<=max:
    print("yes")
else:
    print("no")
#print(x>=min and x<=max)