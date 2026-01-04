try:
    # Open and read the file
    with open("sample.txt", "r") as file:
        print("File content:\n")
        for line in file:
            print(line.strip())

except FileNotFoundError:
    print("Error: The file 'sample.txt' does not exist.")
