def main():
    print(f"Nice to meet you {get_name()}. Congratulations on your {get_age()} years.")


def validname(name):
    for i in name:
        if i.isdigit():
            return False
    else:
        return True

def get_name():
    valid = False
    while not valid:

        name = input("What's your name? ").strip()
        if name != "":
            valid = validname(name)
        if not valid:
            print("Please enter a valid name.")
    return name



def get_age():
    
    valid = False
    while not valid:

        age = input("How old are you? ").strip()
        try:
            age = int(age)
            if age <= 125 and age >= 0:
                valid = True
            else:
                print(f"You seriously expect me to believe you are {age} years old?")
        except ValueError:
            print("Please enter an integer.")

        
    return age


if __name__ == "__main__":
    main()
