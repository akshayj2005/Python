try:
    file=open('example.txt','r')
    content=file.read()
    print(content)
except FileNotFoundError:
    print("Error: The file was  not found.")
finally:
    file.close()

