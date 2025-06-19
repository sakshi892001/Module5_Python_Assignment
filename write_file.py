try:
    with open("output.txt", "a+") as file:
        # Step 1: Write new text
        user_input = input("Enter text to write to the file: ")
        file.write(user_input + "\n")
        print("✅ Data successfully written to 'output.txt'.")

        # Step 2: Append additional text
        additional_input = input("Enter additional text to append to the file: ")
        file.write(additional_input + "\n")
        print("✅ Additional data successfully appended to 'output.txt'.")

        # Step 3: Read final content
        file.seek(0)  # Move cursor to beginning for reading
        print("\n📄 Final content of 'output.txt':")
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print("The file 'output.txt' does not exist.")
except IOError:
    print("Error: An error occurred while handling the file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
