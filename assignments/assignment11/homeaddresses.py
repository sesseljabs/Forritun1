# Main program starts here
def main():
    home_addresses = get_home_addresses()
    print(home_addresses)
    street_and_number = get_tuple_from_home_addresses(home_addresses)
    print(street_and_number)

"".isdigit
# Write your functions here

def get_home_addresses():
    addresses = []
    addr = ""
    while addr != "q":
        addr = input("Home address: ")
        if addr != "q":
            addresses.append(addr)
    return addresses

def get_tuple_from_home_addresses(home_addresses):
    addresses = []
    for i in home_addresses:
        a = i.split()
        addresses.append((a[0],a[1]))
    return addresses

if __name__ == "__main__":
    main()
