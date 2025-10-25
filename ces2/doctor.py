import json

class Doctor:
    def __init__(self, doctor_id, name, specialization, available_slots):
        self.doctor_id = doctor_id
        self.name = name
        self.specialization = specialization
        self.available_slots = available_slots  # list of strings

    def is_available(self, slot):
        return slot in self.available_slots

    def save_doctor_data(self):
        with open("doctor_data.json", "a") as f:
            json.dump(Doctor, f, indent=4)

    def load_doctor_data(self):
        try:
            with open("doctor_data.json", "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return []
