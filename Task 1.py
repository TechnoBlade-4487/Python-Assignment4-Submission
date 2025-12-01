try:
    with open("sample.txt", "r") as file:
        print("Reading File Content:")
        file_lines = file.readlines()
        l_number = 1
        for line in file_lines:
            print(f"Line {l_number}: {line}")
            l_number += 1
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")
