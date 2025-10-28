import json
import os

DATA_FILE = r"C:\Users\aksha\Desktop\vs code\Python\ces2\appointment_data.json"

class Appointment:
    def __init__(self, doctor_id, patient_name, date, time):
        self.doctor_id = doctor_id
        self.patient_name = patient_name
        self.date = date
        self.time = time

    def save_appointment(self):
        appointments = self.load_appointments()
        for a in appointments:
            if (
                a["doctor_id"] == self.doctor_id
                and a["date"] == self.date
                and a["time"] == self.time
            ):
                print("❌ Appointment conflict! Doctor already booked at this time.")
                return

        appointments.append(self.__dict__)
        with open(DATA_FILE, "w") as f:
            json.dump(appointments, f, indent=4)
        print("✅ Appointment saved successfully.")

    def load_appointments(self):
        if not os.path.exists(DATA_FILE):
            print(f"⚠️ File not found: {DATA_FILE}")
            return []
        with open(DATA_FILE, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                print("⚠️ JSON file is invalid or empty!")
                return []

    @staticmethod
    def show_all_appointments():
        print(f"📂 Checking file: {DATA_FILE}")
        if not os.path.exists(DATA_FILE):
            print("❌ No appointments found (file missing).")
            return

        with open(DATA_FILE, "r") as f:
            try:
                appointments = json.load(f)
            except json.JSONDecodeError:
                print("❌ Error: appointment_data.json is not valid JSON.")
                return

        if not appointments:
            print("❌ No appointments found (file empty).")
            return

        appointments.sort(key=lambda x: (x["date"], x["time"]))
        print("\n--- All Appointments ---")
        for a in appointments:
            print(
                f"Doctor ID: {a['doctor_id']}, "
                f"Patient: {a['patient_name']}, "
                f"Date: {a['date']}, Time: {a['time']}"
            )
