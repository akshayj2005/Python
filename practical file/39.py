try:
    file= open("example.txt","r")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("Error: the file was not found.")
finally:
    if 'file' in locals():
        file.close()  #ensures the file is closed whether or not an exception occured
    print("file exists")
