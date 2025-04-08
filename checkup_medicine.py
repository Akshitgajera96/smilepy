from datetime import datetime, timedelta

class CheckupMedicineReminder:
    def __init__(self):
        self.reminders = []

    def schedule_appointment_reminder(self):
        """Schedule a dental appointment reminder."""
        date_str = input("Enter appointment date & time (YYYY-MM-DD HH:MM): ").strip()
        try:
            date_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
            self.reminders.append({"type": "Appointment", "date": date_time})
            print(f"✅ Reminder set: Dental appointment on {date_time.strftime('%Y-%m-%d %H:%M')}.")
        except ValueError:
            print("⚠ Invalid format! Use YYYY-MM-DD HH:MM.")

    def add_medication_reminder(self):
        """Set a reminder for taking medicine."""
        medicine_name = input("Enter medicine name: ").strip()
        time_of_day = input("Enter time to take medicine (HH:MM): ").strip()
        try:
            datetime.strptime(time_of_day, "%H:%M")
            self.reminders.append({"type": "Medicine", "name": medicine_name, "time": time_of_day})
            print(f"✅ Reminder set: Take {medicine_name} at {time_of_day}.")
        except ValueError:
            print("⚠ Invalid time format! Use HH:MM.")

    def show_upcoming_reminders(self):
        """Display all upcoming reminders."""
        now = datetime.now()
        upcoming = [r for r in self.reminders if r["type"] == "Appointment" and r["date"] > now]
        if upcoming:
            for r in upcoming:
                print(f"🔔 Upcoming Appointment: {r['date'].strftime('%Y-%m-%d %H:%M')}")
        else:
            print("✅ No upcoming appointments.")

    def suggest_next_dental_checkup(self):
        """Suggest the next dental checkup date (6 months later)."""
        last_checkup = input("Enter last checkup date (YYYY-MM-DD): ").strip()
        try:
            last_checkup_date = datetime.strptime(last_checkup, "%Y-%m-%d")
            suggested_date = last_checkup_date + timedelta(days=180)
            print(f"📅 Suggested next checkup on {suggested_date.strftime('%Y-%m-%d')}.")
        except ValueError:
            print("⚠ Invalid date format! Use YYYY-MM-DD.")

    def track_missed_appointments(self):
        """Check for missed appointments."""
        now = datetime.now()
        missed = [r for r in self.reminders if r["type"] == "Appointment" and r["date"] < now]
        print(f"⚠ You have missed {len(missed)} appointments." if missed else "✅ No missed appointments.")

    def adjust_medication_timing(self):
        """Suggest new medicine time if a dose is missed."""
        medicine_name = input("Enter medicine name: ").strip()
        last_taken_time_str = input("Enter last taken time (HH:MM): ").strip()
        try:
            last_taken_time = datetime.strptime(last_taken_time_str, "%H:%M")
            new_time = last_taken_time + timedelta(hours=4)
            print(f"⏰ Suggested new time for {medicine_name}: {new_time.strftime('%H:%M')}.")
        except ValueError:
            print("⚠ Invalid time format! Use HH:MM.")

    def detect_irregular_medication_usage(self):
        """Detect irregular medication usage based on user input."""
        missed_doses = int(input("How many doses did you miss in the past week? "))
        if missed_doses > 3:
            print("⚠ Warning! Your medication adherence is poor.")
        else:
            print("✅ Your medication schedule is consistent.")

    def auto_reschedule_appointment(self):
        """Auto-reschedule a missed appointment to next week."""
        old_date_str = input("Enter missed appointment date (YYYY-MM-DD): ").strip()
        try:
            old_date = datetime.strptime(old_date_str, "%Y-%m-%d")
            new_date = old_date + timedelta(days=7)
            print(f"📅 New appointment set for {new_date.strftime('%Y-%m-%d')}.")
        except ValueError:
            print("⚠ Invalid date format! Use YYYY-MM-DD.")

    def recommend_teeth_cleaning_schedule(self):
        """Suggests a professional teeth cleaning schedule."""
        print("✅ Recommended: Professional teeth cleaning every 6 months.")

def main():
    reminder_system = CheckupMedicineReminder()

    while True:
        print("\n🔔 AI-Based Checkup & Medicine Reminder")
        print("1. Schedule Appointment Reminder")
        print("2. Add Medication Reminder")
        print("3. Show Upcoming Reminders")
        print("4. Suggest Next Dental Checkup")
        print("5. Track Missed Appointments")
        print("6. Adjust Medication Timing")
        print("7. Detect Irregular Medication Usage")
        print("8. Auto-Reschedule Missed Appointment")
        print("9. Recommend Teeth Cleaning Schedule")
        print("10. Exit")

        choice = input("Enter your choice (1-10): ").strip()

        if choice == "1":
            reminder_system.schedule_appointment_reminder()
        elif choice == "2":
            reminder_system.add_medication_reminder()
        elif choice == "3":
            reminder_system.show_upcoming_reminders()
        elif choice == "4":
            reminder_system.suggest_next_dental_checkup()
        elif choice == "5":
            reminder_system.track_missed_appointments()
        elif choice == "6":
            reminder_system.adjust_medication_timing()
        elif choice == "7":
            reminder_system.detect_irregular_medication_usage()
        elif choice == "8":
            reminder_system.auto_reschedule_appointment()
        elif choice == "9":
            reminder_system.recommend_teeth_cleaning_schedule()
        elif choice == "10":
            print("👋 Exiting Reminder System. Stay healthy! 😊")
            break
        else:
            print("⚠ Invalid choice! Enter a number between 1-10.")

if __name__ == "__main__":
    main()
