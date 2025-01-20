import re

# Function to implement grep-like functionality
def grep(pattern, file_name):
    with open(file_name, 'r') as fp:
        for line in fp:
            if re.search(pattern, line):
                print(line.strip())
    return

# Function to replace old pattern with new pattern in a file (sed-like functionality)
def sed(old_pattern, new_pattern, file_name):
    with open(file_name, 'r') as fp:
        file_contents = fp.read()

    # Replacing the old pattern with the new pattern
    updated_contents = re.sub(old_pattern, new_pattern, file_contents)

    # Writing the updated content back to the file
    with open(file_name, 'w') as fp:
        fp.write(updated_contents)

    print(f"Replaced '{old_pattern}' with '{new_pattern}' in {file_name}.")
    return

# Function to print a specific column from a file (awk-like functionality)
def awk(n, file_name):
    with open(file_name, 'r') as fp:
        for line in fp:
            columns = line.split()  # Split line by whitespace
            if len(columns) >= n:   # Check if the line has enough columns
                print(columns[n - 1])  # Print the nth column (1-indexed)
            else:
                print(f"Line '{line.strip()}' does not have {n} columns.")
    return

# Main function to handle user input and call corresponding functions
def main():
    file_name = input("Enter the file name: ")
    command = input("Enter the command: grep, sed, awk: ")

    if command == 'grep':
        pattern = input("Enter the pattern: ")
        grep(pattern, file_name)
    elif command == 'sed':
        old_pattern = input("Enter old pattern: ")
        new_pattern = input("Enter new pattern: ")
        sed(old_pattern, new_pattern, file_name)
    elif command == 'awk':
        n = input("Enter the column number: ")
        num = int(n)
        awk(num, file_name)
    else:
        print("Command is invalid.")

if __name__ == "__main__":
    main()
