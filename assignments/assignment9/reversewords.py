def main():
    file_name = input("Enter the filename: ")

    with open(file_name) as f:
        for i in f.readlines():
            for j in i.split():
                print(j[::-1], end=" ")
            print()


if __name__ == "__main__":
    main()
