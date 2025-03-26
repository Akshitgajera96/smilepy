import cv2
import numpy as np
from datetime import datetime

class TeethAnalyzer:
    def __init__(self):
        self.analysis_history = []
    
    def detect_cavities(self, image_path):
        """Detects cavities in a teeth image using simple image processing."""
        image = cv2.imread(image_path, 0)
        _, threshold = cv2.threshold(image, 150, 255, cv2.THRESH_BINARY)
        cavity_count = np.sum(threshold == 0)
        result = "Cavities detected" if cavity_count > 500 else "No cavities detected"
        self.analysis_history.append((datetime.now(), result))
        return result
    
    def check_gum_health(self, redness_level):
        """Evaluates gum health based on redness level."""
        if redness_level > 70:
            return "High risk of gum disease! Visit a dentist."
        elif redness_level > 40:
            return "Moderate gum inflammation detected. Maintain oral hygiene."
        else:
            return "Gum health is good!"
    
    def measure_teeth_whiteness(self, image_path):
        """Measures teeth whiteness using grayscale analysis."""
        image = cv2.imread(image_path, 0)
        avg_brightness = np.mean(image)
        if avg_brightness > 180:
            return "Teeth are very white. Good condition!"
        elif avg_brightness > 120:
            return "Teeth are moderately white. Consider whitening treatments."
        else:
            return "Teeth are yellowing. Professional cleaning recommended."
    
    def bad_breath_risk(self, last_brush_time, diet):
        """Analyzes bad breath risk based on brushing habits and diet."""
        hours_since_brush = (datetime.now() - last_brush_time).total_seconds() / 3600
        risk_score = hours_since_brush * 2 + (5 if 'garlic' in diet or 'onion' in diet else 0)
        return "High bad breath risk!" if risk_score > 10 else "Breath is likely fresh."
    
    def teeth_alignment_check(self, teeth_positions):
        """Checks if teeth are misaligned based on given positions."""
        misalignment = sum([1 for pos in teeth_positions if abs(pos) > 5])
        return f"{misalignment} teeth appear misaligned. Consider orthodontic consultation." if misalignment else "Teeth alignment is good!"
    
    def plaque_detection(self, plaque_level):
        """Detects plaque level and provides advice."""
        if plaque_level > 70:
            return "High plaque buildup! Immediate cleaning needed."
        elif plaque_level > 40:
            return "Moderate plaque detected. Brush and floss regularly."
        else:
            return "Plaque levels are low. Keep up good oral hygiene!"
    
    def tooth_sensitivity_test(self, response_to_cold):
        """Checks tooth sensitivity based on reaction to cold items."""
        if response_to_cold > 7:
            return "Severe sensitivity detected! Visit a dentist."
        elif response_to_cold > 4:
            return "Moderate sensitivity. Use a sensitivity toothpaste."
        else:
            return "Teeth sensitivity is normal."
    
    def enamel_strength_check(self, acid_exposure, brushing_habit):
        """Assesses enamel health based on acid exposure and brushing habits."""
        if acid_exposure > 6 or brushing_habit < 2:
            return "Enamel weakening detected. Reduce acidic foods and improve brushing."
        return "Enamel health is good. Keep up proper care!"
    
    def grinding_teeth_risk(self, stress_level, jaw_pain):
        """Evaluates bruxism (teeth grinding) risk based on stress and pain levels."""
        if stress_level > 7 or jaw_pain > 5:
            return "High risk of teeth grinding. Consider using a night guard."
        return "Low risk of teeth grinding."
    
    def oral_hygiene_score(self, brushing, flossing, diet):
        """Calculates an oral hygiene score based on habits."""
        score = brushing * 2 + flossing * 3 - (3 if 'sugar' in diet else 0)
        return f"Oral hygiene score: {max(0, min(10, score))}/10. Maintain good habits!"
    
    def analyze_teeth_condition(self, image_path):
        """Analyzes the teeth image and suggests possible treatments."""
        image = cv2.imread(image_path, 0)
        avg_brightness = np.mean(image)
        _, threshold = cv2.threshold(image, 150, 255, cv2.THRESH_BINARY)
        cavity_count = np.sum(threshold == 0)
        
        report = "Teeth Analysis Report:\n"
        
        if cavity_count > 500:
            report += "- Cavities detected. Suggested treatment: Fillings or fluoride treatment.\n"
        else:
            report += "- No significant cavities detected.\n"
        
        if avg_brightness < 120:
            report += "- Yellowing detected. Suggested treatment: Whitening or professional cleaning.\n"
        elif avg_brightness < 180:
            report += "- Moderate whiteness. Maintain good oral hygiene.\n"
        else:
            report += "- Teeth are in great condition!\n"
        
        self.analysis_history.append((datetime.now(), report))
        return report
        
    def get_analysis_history(self):        
        return self.analysis_history
    