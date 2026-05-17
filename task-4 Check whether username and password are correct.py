#Check whether username and password are correct
user="Dharani"
password=2604
user_input=input('Enter user name:')
user_password=int(input('Enter password:'))
if user_input==user and user_password==password:
    print("verified")
else:
    print("invalid")
 #print(user_input==user and user_password==password)