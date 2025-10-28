import json
import os

DATA_FILE = r"C:\Users\aksha\Desktop\vs code\Python\ces2\patient_data.json"

class Patient:
    def __init__(self, name, age, mobile_number, appointment_date=None):
        self.name = name
        self.age = age
        self.mobile_number = mobile_number
        self.appointment_date = appointment_date

    def save_patient_data(self):
        patients = self.load_patient_data()
        patients.append(self.__dict__)
        with open(DATA_FILE, "w") as f:
            json.dump(patients, f, indent=4)
        print(f"✅ Patient data saved to {DATA_FILE}")

    def load_patient_data(self):
        if not os.path.exists(DATA_FILE):
            return []
        with open(DATA_FILE, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
