import cv2
import numpy as np
from datetime import datetime

class TeethAnalyzer:
    def __init__(self):
        self.analysis_history = []

    def _read_image(self, image_input):
        """Reads an image from a file path or accepts an existing image array."""
        if isinstance(image_input, str):  # If image path is provided
            image = cv2.imread(image_input)
            if image is None:
                raise ValueError("Failed to load image")
        elif isinstance(image_input, np.ndarray):  # If image array is provided
            image = image_input
        else:
            raise TypeError("Invalid input type. Expected file path or numpy array.")
        return image

    def _preprocess_image(self, image):
        """Preprocess image for better analysis."""
        image = cv2.GaussianBlur(image, (5, 5), 0)  # Reduce noise
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
        return clahe.apply(gray)

    def detect_cavities(self, image_input):
        """Detects cavities using image processing."""
        image = self._preprocess_image(self._read_image(image_input))
        image = cv2.medianBlur(image, 5)  # Reduce noise before thresholding
        thresh = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                                       cv2.THRESH_BINARY_INV, 11, 2)
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cavity_count = sum(1 for cnt in contours if 100 < cv2.contourArea(cnt) < 1000)  # Filter cavities
        result = f"Found {cavity_count} potential cavities. "
        result += "Immediate dental consultation recommended." if cavity_count > 5 else "Schedule a checkup." if cavity_count > 0 else "No significant cavities detected."
        self.analysis_history.append((datetime.now(), result))
        return result

    def measure_teeth_whiteness(self, image_input):
        """Measures teeth whiteness."""
        original_image = self._read_image(image_input)
        preprocessed_image = self._preprocess_image(original_image)
        _, teeth_mask = cv2.threshold(preprocessed_image, 180, 255, cv2.THRESH_BINARY)
        whiteness_average = np.mean(preprocessed_image[teeth_mask > 0])
        return "Excellent" if whiteness_average > 200 else "Good" if whiteness_average > 170 else "Average - Consider whitening" if whiteness_average > 140 else "Below average - Professional cleaning recommended."

    def detect_plaque(self, image_input):
        """Detects plaque levels."""
        image = self._preprocess_image(self._read_image(image_input))
        _, plaque_mask = cv2.threshold(image, 100, 255, cv2.THRESH_BINARY_INV)
        plaque_count = np.sum(plaque_mask == 255)  # Count plaque regions
        return "High plaque buildup detected!" if plaque_count > 1000 else "Low plaque levels. Maintain hygiene."

    def check_teeth_alignment(self, image_input):
        """Analyzes teeth alignment."""
        image = self._preprocess_image(self._read_image(image_input))
        edges = cv2.Canny(image, 50, 150)
        alignment_score = np.count_nonzero(edges)
        return "Teeth misalignment detected. Consider orthodontic consultation." if alignment_score > 5000 else "Teeth alignment is normal."

    def detect_gum_inflammation(self, image_input):
        """Detects gum inflammation."""
        image = self._read_image(image_input)
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        lower_red, upper_red = np.array([0, 70, 50]), np.array([10, 255, 255])
        mask1 = cv2.inRange(hsv, lower_red, upper_red)
        lower_red, upper_red = np.array([170, 70, 50]), np.array([180, 255, 255])
        mask2 = cv2.inRange(hsv, lower_red, upper_red)
        red_mask = cv2.bitwise_or(mask1, mask2)  # Optimized red detection
        inflammation_score = np.count_nonzero(red_mask) / red_mask.size
        return "Significant inflammation detected. Consult dentist." if inflammation_score > 0.1 else "Mild inflammation. Improve oral hygiene." if inflammation_score > 0.05 else "Gum health appears normal."

    def analyze_enamel_strength(self, image_input):
        """Estimates enamel strength."""
        image = self._preprocess_image(self._read_image(image_input))
        return "Weak enamel detected. Reduce acidic foods." if np.var(image) < 500 else "Enamel strength is good!"

    def detect_tooth_sensitivity(self, image_input):
        """Detects tooth sensitivity."""
        image = self._preprocess_image(self._read_image(image_input))
        return "High sensitivity risk detected!" if np.std(image) > 50 else "Tooth sensitivity is within normal range."

    def analyze_teeth_health(self, image_input):
        """Performs a full teeth health analysis."""
        results = [
            self.detect_cavities(image_input),
            self.measure_teeth_whiteness(image_input),
            self.detect_plaque(image_input),
            self.check_teeth_alignment(image_input),
            self.detect_gum_inflammation(image_input),
            self.analyze_enamel_strength(image_input)
        ]
        report = "\n- ".join(results)
        self.analysis_history.append((datetime.now(), report))
        return f"Teeth Health Report:\n- {report}"

    def get_analysis_history(self):
        """Returns the history of analyses performed."""
        return self.analysis_history
