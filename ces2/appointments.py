import json

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

        with open("appointment_data.json", "w") as f:
            json.dump(appointments, f, indent=4)
        print("✅ Appointment saved successfully.")

    def load_appointments(self):
        try:
            with open("appointment_data.json", "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    @staticmethod
    def show_all_appointments():
        try:
            with open("appointment_data.json", "r") as f:
                appointments = json.load(f)
                appointments.sort(key=lambda x: (x["date"], x["time"]))
                print("\n--- All Appointments ---")
                for a in appointments:
                    print(
                        f"Doctor ID: {a['doctor_id']}, "
                        f"Patient: {a['patient_name']}, "
                        f"Date: {a['date']}, Time: {a['time']}"
                    )
        except FileNotFoundError:
            print("No appointments found.")