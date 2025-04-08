from datetime import datetime
import cv2
import numpy as np

class OralHealthCheck:
    def __init__(self):
        self.checkup_history = []

    def check_plaque_levels(self, image_path):
        """Analyze plaque levels from an image using edge detection."""
        image = cv2.imread(image_path, 0)
        edges = cv2.Canny(image, 100, 200)
        plaque_level = np.sum(edges) / 100000  # Rough intensity estimation
        return f"Plaque Level: {'High' if plaque_level > 50 else 'Moderate' if plaque_level > 20 else 'Low'}"

    def detect_bad_breath(self):
        """Detect bad breath based on symptoms."""
        symptoms = input("Do you have dry mouth or a bad taste? (yes/no): ").strip().lower()
        return "Possible bad breath due to dry mouth." if symptoms == "yes" else "No significant signs of bad breath."

    def check_sensitivity(self):
        """Assess teeth sensitivity based on user input."""
        user_feedback = input("What triggers sensitivity? (hot/cold/sweet/none): ").strip().lower()
        return f"Teeth sensitivity detected for {user_feedback}." if user_feedback in ["hot", "cold", "sweet"] else "No sensitivity detected."

    def detect_tooth_decay(self, image_path):
        """Analyze an image for early signs of tooth decay."""
        image = cv2.imread(image_path, 0)
        decay_score = np.mean(image)  # Higher mean = healthier teeth
        return "Possible early-stage tooth decay detected." if decay_score < 100 else "Teeth appear healthy."

    def check_mouth_ulcers(self):
        """Detect mouth ulcers based on symptoms."""
        symptoms = input("Do you have painful sores or red spots in your mouth? (yes/no): ").strip().lower()
        return "Mouth ulcers detected. Consider oral gel treatment." if symptoms == "yes" else "No signs of mouth ulcers."

    def check_gum_bleeding(self):
        """Analyze gum bleeding based on user symptoms."""
        symptoms = input("Do you see blood while brushing? (yes/no): ").strip().lower()
        return "Gum bleeding detected. Possible early gum disease." if symptoms == "yes" else "No gum bleeding detected."

    def check_jaw_pain(self):
        """Analyze jaw pain based on user input."""
        symptoms = input("Do you have difficulty chewing? (yes/no): ").strip().lower()
        return "Jaw pain detected. Possible TMJ disorder." if symptoms == "yes" else "No significant jaw pain detected."

    def detect_tongue_health(self, image_path):
        """Check tongue health based on image brightness."""
        image = cv2.imread(image_path, 0)
        brightness = np.mean(image)  # Darker areas could indicate issues
        return "Healthy tongue detected." if brightness > 100 else "Possible tongue health issues detected."

    def check_for_infections(self):
        """Detect oral infections based on symptoms."""
        symptoms = input("Do you have swelling or pus in your mouth? (yes/no): ").strip().lower()
        return "Possible oral infection detected. Consult a dentist." if symptoms == "yes" else "No signs of oral infections."

def main():
    health_checker = OralHealthCheck()

    while True:
        print("\nOral Health Checker")
        print("1. Check Plaque Levels (Requires Image)")
        print("2. Detect Bad Breath")
        print("3. Check Teeth Sensitivity")
        print("4. Detect Tooth Decay (Requires Image)")
        print("5. Check for Mouth Ulcers")
        print("6. Check for Gum Bleeding")
        print("7. Check Jaw Pain")
        print("8. Detect Tongue Health (Requires Image)")
        print("9. Check for Oral Infections")
        print("10. Exit")

        choice = input("Enter your choice (1-10): ").strip()

        if choice == "1":
            image_path = input("Enter image path for plaque analysis: ").strip()
            print(health_checker.check_plaque_levels(image_path))
        elif choice == "2":
            print(health_checker.detect_bad_breath())
        elif choice == "3":
            print(health_checker.check_sensitivity())
        elif choice == "4":
            image_path = input("Enter image path for tooth decay analysis: ").strip()
            print(health_checker.detect_tooth_decay(image_path))
        elif choice == "5":
            print(health_checker.check_mouth_ulcers())
        elif choice == "6":
            print(health_checker.check_gum_bleeding())
        elif choice == "7":
            print(health_checker.check_jaw_pain())
        elif choice == "8":
            image_path = input("Enter image path for tongue health analysis: ").strip()
            print(health_checker.detect_tongue_health(image_path))
        elif choice == "9":
            print(health_checker.check_for_infections())
        elif choice == "10":
            print("Exiting Oral Health Checker. Stay healthy! 😊")
            break
        else:
            print("Invalid choice! Please enter a number between 1-10.")

if __name__ == "__main__":
    main()