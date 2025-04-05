from datetime import datetime, timedelta

class CheckupMedicineReminder:
    def __init__(self):
        self.reminders = []

    def schedule_appointment_reminder(self, user_id, date_time):
        """Schedules an AI-based appointment reminder."""
        reminder = {"user_id": user_id, "type": "Appointment", "date": date_time}
        self.reminders.append(reminder)
        return f"Reminder: Dental appointment on {date_time.strftime('%Y-%m-%d %H:%M')}."

    def add_medication_reminder(self, user_id, medicine_name, time_of_day):
        """AI adds a medicine reminder for a user."""
        reminder = {"user_id": user_id, "type": "Medicine", "name": medicine_name, "time": time_of_day}
        self.reminders.append(reminder)
        return f"Reminder set: Take {medicine_name} at {time_of_day}."

    def get_upcoming_reminders(self, user_id):
        """Returns all upcoming reminders for a user."""
        return [r for r in self.reminders if r["user_id"] == user_id]

    def send_alerts(self, user_id):
        """Simulates AI-based notification alerts."""
        now = datetime.now()
        upcoming_alerts = [
            reminder for reminder in self.reminders
            if reminder["user_id"] == user_id and reminder["type"] == "Appointment" and reminder["date"] > now
        ]
        return [f"Alert: {reminder['type']} on {reminder['date'].strftime('%Y-%m-%d %H:%M')}" for reminder in upcoming_alerts]

    def suggest_next_dental_checkup(self, last_checkup_date):
        """AI-based checkup interval suggestion."""
        suggested_date = last_checkup_date + timedelta(days=180)  # 6 months later
        return f"Next checkup suggested on {suggested_date.strftime('%Y-%m-%d')}."

    def track_missed_appointments(self, user_id):
        """AI tracks missed appointments."""
        now = datetime.now()
        missed = [r for r in self.reminders if r["user_id"] == user_id and r["type"] == "Appointment" and r["date"] < now]
        return f"You have missed {len(missed)} appointments."

    def adjust_medication_timing(self, medicine_name, last_taken_time):
        """AI adjusts medicine timing if missed."""
        new_time = last_taken_time + timedelta(hours=4)  # Suggests taking it 4 hours later
        return f"New time suggested for {medicine_name}: {new_time.strftime('%H:%M')}."

    def detect_irregular_medication_usage(self, user_id, logs):
        """AI detects if the user is missing medicine doses."""
        missed_doses = sum(1 for log in logs if log["status"] == "missed")
        if missed_doses > 3:
            return "Warning! Your medication adherence is poor."
        return "Your medication schedule is consistent."

    def auto_reschedule_appointment(self, user_id, old_date):
        """AI auto-reschedules a missed appointment."""
        new_date = old_date + timedelta(days=7)  # Reschedules for a week later
        return f"New appointment set for {new_date.strftime('%Y-%m-%d')}."

    def recommend_teeth_cleaning_schedule(self, user_id):
        """Suggests a custom cleaning schedule based on past history."""
        return "Recommended: Professional teeth cleaning every 6 months."
