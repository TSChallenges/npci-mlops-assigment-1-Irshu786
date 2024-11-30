import os
import sys

def create_directory(dir_name):
    try:
        os.makedirs(dir_name)
        print(f"Directory '{dir_name}' created successfully")
    except FileExistsError:
        print(f"Directory '{dir_name}' already exists")
    return

def change_directory(dir_name):
    try:
        os.chdir(dir_name)
        print(f"Changed to directory: {dir_name}")
    except FileNotFoundError:
        print(f"Directory '{dir_name}' does not exist")
    return

def delete_directory(dir_name):
    try:
        os.rmdir(dir_name)
        print(f"Directory '{dir_name}' deleted successfully")
    except OSError as e:
        print(f"Error: {e}")
    return

def list_dir():
    try:
        for item in os.listdir():
            print(item)
    except Exception as e:
        print(f"Error: {e}")
    return

def display_pwd():
    print(f"Current working directory: {os.getcwd()}")
    return

def create_file(file_name):
    with open(file_name, 'w') as f:
        pass
    print(f"File '{file_name}' is created")
    return

def write_file(file_name):
    contents = input("Enter the contents into the file: ")
    with open(file_name, 'a') as f:
        f.write(contents + '\n')
    print("Contents written to file successfully")
    return

def read_file(file_name):
    try:
        with open(file_name, 'r') as f:
            print(f.read())
    except FileNotFoundError:
        print(f"File '{file_name}' does not exist")
    return

def delete_file(file_name):
    try:
        os.remove(file_name)
        print(f"File '{file_name}' deleted successfully")
    except FileNotFoundError:
        print(f"File '{file_name}' does not exist")
    return

def main():
    while True:
        print("\n1. Create a file")
        print("2. Write to a file")
        print("3. Read a file")
        print("4. Delete a file")
        print("5. Create a directory")
        print("6. Change directory")
        print("7. Delete a directory")
        print("8. List current directory contents")
        print("9. Display current working directory")
        print("0. Exit")
        choice = input("Enter your choice here: ")

        if choice == '1':
            file_name = input("Enter the file name: ")
            create_file(file_name)
        elif choice == '2':
            file_name = input("Enter the file name: ")
            write_file(file_name)
        elif choice == '3':
            file_name = input("Enter the file name: ")
            read_file(file_name)
        elif choice == '4':
            file_name = input("Enter the file name: ")
            delete_file(file_name)
        elif choice == '5':
            dir_name = input("Enter the directory name: ")
            create_directory(dir_name)
        elif choice == '6':
            dir_name = input("Enter the directory name: ")
            change_directory(dir_name)
        elif choice == '7':
            dir_name = input("Enter the directory name: ")
            delete_directory(dir_name)
        elif choice == '8':
            list_dir()
        elif choice == '9':
            display_pwd()
        elif choice == '0':
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
