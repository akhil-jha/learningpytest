file = open("letters.txt","r") # Opening the file in reading mode and creating a handle for the file

# Printing the contents of the file
def print_values():
    for letters in file.readlines():
        print(letters,end='')


def main_fun():
    val = int(input("\nPress 1 to print the file: "))
    if val == 1:
        print_values()

if __name__ == "__main__":
    main_fun()