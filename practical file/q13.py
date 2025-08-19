from datetime import datetime
dob_input = input("Enter your date of birth (DD/MM/YYYY): ")
dob = datetime.strptime(dob_input, "%d/%m/%Y")
target_input = input("Enter the date to calculate age on (DD/MM/YYYY): ")
target_date = datetime.strptime(target_input, "%d/%m/%Y")
age = target_date.year - dob.year
if (target_date.month, target_date.day) < (dob.month, dob.day):
    age -= 1
print(f"\nYour age on {target_date.strftime('%d/%m/%Y')} will be: {age} years")
