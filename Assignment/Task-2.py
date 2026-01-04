# Taking input from user
data = input("Enter data to write to the file: ")

# Writing data to file
with open("output.txt", "w") as file:
    file.write(data + "\n")

# Appending additional data
with open("output.txt", "a") as file:
    file.write("This is appended data.\n")

# Reading and displaying final content
print("\nFinal content of output.txt:\n")
with open("output.txt", "r") as file:
    for line in file:
        print(line.strip())
