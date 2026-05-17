#19. Check whether entered city matches allowed cities
city=input("Enter a city: ")
if city=="hyd" or city=="vzg" or city=="vzm" or city=="pvpt" or city=="skl":
  print("allowed")
else:
  print("not allowed")