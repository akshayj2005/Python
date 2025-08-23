try:
    file= open('38.py','r')
    content = file.read()
except FileNotFoundError:
    print("Error: the file was not found.")
finally:
    file.close()  #ensures the file is closed whether or not an exception occured
    print("file exists")
