COUNTRIES_OF_THE_WORLD = "countries.txt"
INPUT_PROMPT = "Enter a suffix for a country: "


def main():
    country_suffix = input(INPUT_PROMPT)

    # TODO: Finish the program
    count = 0
    with open(COUNTRIES_OF_THE_WORLD) as f:
        countries = f.readlines()
        for i in countries:
            i = i.strip()
            if country_suffix == i[len(i)-len(country_suffix):]:
                print(i)
                count+=1
    print(f"{count} countries with suffix '{country_suffix}'.")


# or being imported into another module.
#
# If it is being run, then its __name__ attribute will be "__main__".
# But if it is being imported, it's __name__ will be the name of the .py file.
#
# In case it is being imported, we don't want to run any functions, just import their names.
# But if it is being run, then we call the main() function to start the program.
if __name__ == "__main__":
    main()
