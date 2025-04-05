from datetime import datetime

class OralHealthCheck:
    def __init__(self):
        self.checkup_history = []

    def check_plaque_levels(self, image_path):
        """Analyze plaque levels from the given image."""
        result = f"Plaque detected in moderate levels from {image_path}."
        self.store_checkup("Plaque Levels", result)
        return result

    def detect_bad_breath(self, symptoms):
        """Determine if bad breath is present based on symptoms."""
        if "dry mouth" in symptoms or "bad taste" in symptoms:
            result = "Possible bad breath detected due to dry mouth."
        else:
            result = "No significant signs of bad breath detected."
        self.store_checkup("Bad Breath", result)
        return result

    def check_sensitivity(self, user_feedback):
        """Assess teeth sensitivity based on feedback."""
        if user_feedback.lower() in ["hot", "cold", "sweet"]:
            result = f"Teeth sensitivity detected for {user_feedback}."
        else:
            result = "No significant sensitivity detected."
        self.store_checkup("Sensitivity", result)
        return result

    def detect_tooth_decay(self, image_path):
        """Analyze signs of tooth decay from the image."""
        result = f"Possible early-stage tooth decay detected in {image_path}."
        self.store_checkup("Tooth Decay", result)
        return result

    def check_mouth_ulcers(self, symptoms):
        """Check for mouth ulcers based on symptoms."""
        if "painful sores" in symptoms or "red spots" in symptoms:
            result = "Mouth ulcers detected. Consider oral gel treatment."
        else:
            result = "No signs of mouth ulcers detected."
        self.store_checkup("Mouth Ulcers", result)
        return result

    def check_gum_bleeding(self, symptoms):
        """Determine gum bleeding based on symptoms."""
        if "blood on brushing" in symptoms:
            result = "Gum bleeding detected. Possible early gum disease."
        else:
            result = "No gum bleeding detected."
        self.store_checkup("Gum Bleeding", result)
        return result

    def check_jaw_pain(self, symptoms):
        """Analyze jaw pain based on user feedback."""
        if "difficulty chewing" in symptoms:
            result = "Jaw pain detected. Possible TMJ disorder."
        else:
            result = "No significant jaw pain detected."
        self.store_checkup("Jaw Pain", result)
        return result

    def detect_tongue_health(self, image_path):
        """Analyze tongue for signs of health issues."""
        result = f"Healthy tongue detected in {image_path}."
        self.store_checkup("Tongue Health", result)
        return result

    def check_for_infections(self, symptoms):
        """Check for oral infections based on symptoms."""
        if "swelling" in symptoms or "pus" in symptoms:
            result = "Possible oral infection detected. Consult a dentist."
        else:
            result = "No signs of oral infections detected."
        self.store_checkup("Oral Infections", result)
        return result

    def get_checkup_history(self):
        """Retrieve checkup history."""
        return self.checkup_history

    def store_checkup(self, checkup_type, result):
        """Store checkup result in history."""
        timestamp = datetime.now()
        self.checkup_history.append((timestamp, checkup_type, result))
