import json


class patient :
    def __init__(self, name, age, mobile_number, appointment_date=None):
        self.name = name
        self.age = age
        self.mobile_number = mobile_number
        self.appointment_date = appointment_date
    
    def save_patient_data(self):
         with open("patient_data.json", "a") as f:
            json.dump(patient, f, indent=4)
    def load_patient_data(self):
        try:
            with open("patient_data.json", "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return []
    

