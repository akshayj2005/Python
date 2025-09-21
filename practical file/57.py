text = "Hello , World"

#changing case
lowercase_text = text.lower()
uppercase_text = text.upper()
title_text = text.title()

#trimming whitespace
stripped_text = text.strip()
left_stripped_text = text.lstrip()
right_stripped_text = text.rstrip()

#splitting and joining
words = stripped_text.split(",")
joined_text = "-".join(words)

#replacing and finding
replaced_text = stripped_text.replace("World" , "python")
index = stripped_text.find("World")
count = stripped_text.count("o")

print(lowercase_text)
print(uppercase_text)
print(title_text)
print(stripped_text)
print(left_stripped_text)
print(right_stripped_text)
print(words)
print(joined_text)
print(replaced_text)
print(index)
print(count)

