from doctor import Doctor
from patient import patient
from appointments import Appointment

def main():
    print("\n🏥 Welcome to Hospital Patient Management System 🏥")

    while True:
        print("\nMain Menu:")
        print("1. Add Doctor")
        print("2. Add Patient")
        print("3. Book Appointment")
        print("4. View All Appointments")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            try:
                doc_id = int(input("Enter Doctor ID: "))
                name = input("Enter Doctor Name: ")
                specialization = input("Enter Specialization: ")
                slots = input("Enter Available Slots (comma separated): ").split(",")

                doctor = Doctor(doc_id, name, specialization, slots)
                doctor.save_doctor_data()
                print("✅ Doctor added successfully.")
            except Exception as e:
                print("Error:", e)

        elif choice == "2":
            try:
                name = input("Enter Patient Name: ")
                age = int(input("Enter Age: "))
                mobile = input("Enter Mobile Number: ")
                date = input("Enter Appointment Date (YYYY-MM-DD) [optional]: ") or None

                patient = Patient(name, age, mobile, date)
                patient.save_patient_data()
                print("✅ Patient added successfully.")
            except Exception as e:
                print("Error:", e)

        elif choice == "3":
            try:
                doctor_id = int(input("Enter Doctor ID: "))
                patient_name = input("Enter Patient Name: ")
                date = input("Enter Appointment Date (YYYY-MM-DD): ")
                time = input("Enter Appointment Time (e.g., 10AM, 3PM): ")

                appointment = Appointment(doctor_id, patient_name, date, time)
                appointment.save_appointment()
            except Exception as e:
                print("Error:", e)

        elif choice == "4":
            Appointment.show_all_appointments()
        elif choice == "5":
            print("👋 Exiting the system. Have a good day!")
            break

        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
