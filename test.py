import cv2
from teethanalyzer import TeethAnalyzer
from patientrecord import PatientRecord
from oral_healthcheck import OralHealthCheck
from diet_teethcare import DietTeethCare
from checkup_medicine import CheckupMedicineReminder
from datetime import datetime

def run_analysis(image_path):
    
    try:
        img = cv2.imread(image_path)
        if img is None:
            print("\nError: Invalid image path or file not found. Please check the image location.")
            return
        
        analyzer = TeethAnalyzer()

        print("\n=== Dental Analysis Report ===\n")
        print("1. Cavity Detection:")
        print("   " + analyzer.detect_cavities(image_path))

        print("\n2. Gum Health Assessment:")
        print("   " + analyzer.detect_gum_inflammation(image_path))

        print("\n3. Teeth Whiteness Analysis:")
        print("   " + analyzer.measure_teeth_whiteness(image_path))

        print("\n4. Full Analysis Report:")
        print(analyzer.analyze_teeth_health(image_path))

        print("\n=== Analysis History ===")
        for timestamp, result in analyzer.get_analysis_history():
            print(f"\nDate: {timestamp.strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"Result: {result}")

    except Exception as e:
        print(f"\nError during analysis: {str(e)}")

def test_patient_record():
    try:
        patient = PatientRecord("John Doe", 30)
        image_path = r"C:\Users\gajer\OneDrive\Desktop\sem-4\pyhton\smilepy\download.jpg"
        
        print("\n=== Patient Record Test ===\n")
        print(f"Patient: {patient.user_name}, Age: {patient.age}")
        
        result = patient.analyze_teeth_now(image_path)
        print("\nTeeth Analysis Result Stored.")

        print("\n=== Patient Info & Teeth History ===")
        patient_info = patient.get_user_info()
        for key, value in patient_info.items():
            print(f"{key}: {value}")

        print("\n=== Last Analysis ===")
        print(patient.get_last_analysis())

        print("\n=== Whiteness Suggestion ===")
        print(patient.get_whiteness_suggestion())

        print("\n=== Cavity Alert ===")
        print(patient.get_cavity_alert())

        print("\nClearing Teeth History...")
        print(patient.clear_teeth_history())

    except Exception as e:
        print(f"\nError during patient record test: {str(e)}")

def test_oral_health_check():
    try:
        oral_check = OralHealthCheck()
        image_path = r"C:\Users\gajer\OneDrive\Desktop\sem-4\pyhton\smilepy\download.jpg"

        print("\n=== Oral Health Check Test ===\n")
        print("1. Plaque Levels:")
        print("   " + oral_check.check_plaque_levels(image_path))

        print("\n2. Bad Breath Detection:")
        print("   " + oral_check.detect_bad_breath(["dry mouth"]))

        print("\n3. Sensitivity Check:")
        print("   " + oral_check.check_sensitivity("cold"))

        print("\n4. Tooth Decay Detection:")
        print("   " + oral_check.detect_tooth_decay(image_path))

        print("\n5. Mouth Ulcers Detection:")
        print("   " + oral_check.check_mouth_ulcers(["red spots"]))

        print("\n6. Gum Bleeding Check:")
        print("   " + oral_check.check_gum_bleeding(["blood on brushing"]))

        print("\n7. Jaw Pain Analysis:")
        print("   " + oral_check.check_jaw_pain(["difficulty chewing"]))

        print("\n8. Tongue Health Analysis:")
        print("   " + oral_check.detect_tongue_health(image_path))

        print("\n9. Oral Infections Check:")
        print("   " + oral_check.check_for_infections(["swelling"]))

        print("\n=== Oral Health Checkup History ===")
        for timestamp, checkup_type, result in oral_check.get_checkup_history():
            print(f"\nDate: {timestamp.strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"Checkup Type: {checkup_type}")
            print(f"Result: {result}")

    except Exception as e:
        print(f"\nError during oral health check test: {str(e)}")

def test_diet_teeth_care():
    try:
        diet_care = DietTeethCare()

        print("\n=== Diet & Teeth Care Test ===\n")
        print("1. Suggest Diet for Strong Teeth:")
        print("   " + diet_care.suggest_diet("strong_teeth"))

        print("\n2. Suggest Diet for Whitening:")
        print("   " + diet_care.suggest_diet("whitening"))

        print("\n3. Get Personalized Diet Plan:")
        print("   " + str(diet_care.get_personalized_diet_plan("John Doe")))

        print("\n4. Get Diet History:")
        print("   " + str(diet_care.get_diet_history("John Doe")))

    except Exception as e:
        print(f"\nError during diet & teeth care test: {str(e)}")

def test_checkup_medicine_reminder():
    try:
        reminder = CheckupMedicineReminder()
        print("\n=== Checkup & Medicine Reminder Test ===\n")

        print("1. Set Appointment Reminder:")
        print("   " + reminder.set_appointment_reminder("John Doe", "2025-05-10 14:00"))

        print("\n2. Set Medicine Reminder:")
        print("   " + reminder.set_medicine_reminder("John Doe", "Painkiller", "08:00 AM"))

        print("\n3. Get Reminders:")
        print("   " + str(reminder.get_reminders("John Doe")))

    except Exception as e:
        print(f"\nError during checkup & medicine reminder test: {str(e)}")

if __name__ == "__main__":
    image_path = r'C:\Users\gajer\OneDrive\Desktop\sem-4\pyhton\smilepy\download.jpg'

    print("\n=== Running SmilePy System ===\n")
    
    # Check if image exists before running analysis
    img = cv2.imread(image_path)
    if img is not None:
        run_analysis(image_path)
    else:
        print("\nSkipping Teeth Analysis: Image file not found!")

    test_patient_record()
    test_oral_health_check()
    test_diet_teeth_care()
    test_checkup_medicine_reminder()

    print("\n=== All Tests Completed Successfully ===")
