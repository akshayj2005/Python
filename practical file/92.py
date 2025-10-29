#user defined exception
class ValidationError(Exception):
    def __init__(self, message,field):
        self.message = message
        self.field = field
    def __str__(self):
        return f"ValidationError in field '{self.field}': {self.message}"
def validate_age(age):
    if age < 0 or age > 120:
        raise ValidationError("Age must be between 0 and 120", "age")
    return True

try:
    age = int(input("Enter your age: "))
    validate_age(age)
    print("Age is valid.")
except ValidationError as ve:
    print(ve)

