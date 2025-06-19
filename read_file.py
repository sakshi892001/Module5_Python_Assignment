try:    # code that might raise an error
    file1=open("sample.txt","r")
    reading_line=file1.readlines()
    for line in reading_line:
        print(line.strip())
except FileNotFoundError:
    print("The File 'sample.txt' not found") #exceutes only if the file is not found
except IOError:
    print("Error: An error occurred while reading the file.")
finally:
    file1.close() # This block will always execute, whether an exception occurred or not