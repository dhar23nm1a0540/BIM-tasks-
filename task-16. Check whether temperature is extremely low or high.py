#16. Check whether temperature is extremely low or high
temp=int(input("enter temperture:"))
if temp>=40 or temp<=18:
    print("unfavourable conditions")
else:
    print("safe")