def extract_first_number_from_string(string_input):
    splitstring = string_input.split(" ")
    for i in splitstring:
        if i.isdigit():
            return i
    else:
        return -1
print(extract_first_number_from_string("There are 365 or 366 days in the year."))