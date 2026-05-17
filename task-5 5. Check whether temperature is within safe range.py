#5. Check whether temperature is within safe range
temp=int(input('Enter Temperature: '))
if temp<=40 and temp>=15:
    print("Safe temperature")
else:
    print("take care")
#print(temp<=40 and temp>=15)