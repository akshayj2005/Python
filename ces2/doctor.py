import json
import os

DATA_FILE = r"C:\Users\aksha\Desktop\vs code\Python\ces2\doctor_data.json"

class Doctor:
    def __init__(self, doctor_id, name, specialization, available_slots):
        self.doctor_id = doctor_id
        self.name = name
        self.specialization = specialization
        self.available_slots = available_slots

    def is_available(self, slot):
        return slot in self.available_slots

    def save_doctor_data(self):
        doctors = self.load_doctor_data()
        doctors.append(self.__dict__)
        with open(DATA_FILE, "w") as f:
            json.dump(doctors, f, indent=4)
        print(f"✅ Doctor data saved to {DATA_FILE}")

    def load_doctor_data(self):
        if not os.path.exists(DATA_FILE):
            return []
        with open(DATA_FILE, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
