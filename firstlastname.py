name = input("Input a name: ")
lname, fname = name.split(", ")
print(f"{fname[0].upper()}. {lname.capitalize()}")