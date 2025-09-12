#String Functions
text = "Hello, World!"
print(text.lower())          # Convert to lowercase
print(text.upper())          # Convert to uppercase
print(text.title)     # Capitalize the first letter
print(text.strip())         # Remove leading and trailing whitespace
print(text.lstrip())
print(text.rstrip())

print(text.strip().split(" , "))
print(" - ".join(text.strip().split(" , ")))
         # Remove leading and trailing whitespace
  # Replace substring