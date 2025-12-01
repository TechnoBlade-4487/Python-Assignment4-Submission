with open("output.txt", "wt") as file:
    write_text = input("Enter text to write to the file: ")
    file.write(f"{write_text}\n")
    print("Data successfully written to output.txt.")
    print()

with open("output.txt", "at") as file:
    append_text = input("Enter additional text to append: ")
    file.write(append_text)
    print("Data successfully appended.")
    print()

with open("output.txt", "rt") as file:
    print("Final content of output.txt:")
    print(file.read())
