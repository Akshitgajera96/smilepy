import cv2
import numpy as np
from datetime import datetime

class TeethAnalyzer:
    def __init__(self):
        self.analysis_history = []

    def analyze_teeth(self, image_path):
        """Analyzes the teeth condition in real-time."""
        image = cv2.imread(image_path, 0)
        avg_brightness = np.mean(image)
        _, threshold = cv2.threshold(image, 150, 255, cv2.THRESH_BINARY)
        cavity_count = np.sum(threshold == 0)

        report = "Teeth Analysis Report:\n"

        if cavity_count > 500:
            report += "- Possible cavities detected. Consider improving oral hygiene.\n"
        else:
            report += "- No major cavities detected.\n"

        if avg_brightness < 120:
            report += "- Teeth appear yellowish. Whitening recommended.\n"
        elif avg_brightness < 180:
            report += "- Teeth in moderate condition. Keep brushing regularly.\n"
        else:
            report += "- Teeth are in great condition!\n"

        self.analysis_history.append((datetime.now(), report))
        return report

    def get_analysis_history(self):
        """Returns past analysis reports."""
        return self.analysis_history


class PatientRecord:
    def __init__(self, user_name, age):
        """Stores personal teeth health history."""
        self.user_name = user_name
        self.age = age
        self.teeth_history = []
        self.teeth_analyzer = TeethAnalyzer()

    def analyze_teeth_now(self, image_path):
        """Performs instant teeth analysis and stores results."""
        result = self.teeth_analyzer.analyze_teeth(image_path)
        self.teeth_history.append((datetime.now().strftime("%Y-%m-%d"), result))
        return result

    def get_user_info(self):
        """Returns user details and analysis history."""
        return {
            "Name": self.user_name,
            "Age": self.age,
            "Teeth Health History": self.teeth_history
        }

    def get_last_analysis(self):
        """Gets the latest teeth check-up result."""
        return self.teeth_history[-1] if self.teeth_history else "No analysis history found."

    def clear_teeth_history(self):
        """Clears all past analysis records."""
        self.teeth_history.clear()
        return "Teeth analysis history cleared."

    def get_whiteness_suggestion(self):
        """Provides suggestions for teeth whitening based on past analyses."""
        for _, report in self.teeth_history:
            if "yellowish" in report:
                return "Consider using whitening toothpaste or home remedies."
        return "No whitening required. Maintain hygiene."

    def get_cavity_alert(self):
        """Checks if past analyses indicate cavity risk."""
        for _, report in self.teeth_history:
            if "cavities" in report:
                return "You might have cavities. Consider improving oral care."
        return "No cavity issues detected. Keep up the good work!"

    def get_all_treatment_suggestions(self):
        """Summarizes all past suggestions from analysis."""
        return [report for _, report in self.teeth_history]

    def search_teeth_history(self, keyword):
        """Searches history for specific keywords like 'cavities' or 'whitening'."""
        return [record for record in self.teeth_history if keyword.lower() in record[1].lower()]

    def get_real_time_status(self):
        """Provides a quick summary of recent teeth health status."""
        return self.get_last_analysis()
