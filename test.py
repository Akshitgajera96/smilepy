from teethanalyzer import TeethAnalyzer
from datetime import datetime

# Create an instance
analyzer = TeethAnalyzer()

# Provide an image path (Make sure the image exists)
image_path = r"C:\Users\gajer\OneDrive\Desktop\sem-4\pyhton\smilepy\download.jpeg"  # Place a teeth image in the same folder

# Run all functions
print(analyzer.detect_cavities(image_path))
print(analyzer.check_gum_health(50))
print(analyzer.measure_teeth_whiteness(image_path))
print(analyzer.bad_breath_risk(datetime.now(), ['garlic', 'onion']))
print(analyzer.teeth_alignment_check([1, -2, 3, 6, -7]))  # Example positions
print(analyzer.plaque_detection(80))
print(analyzer.tooth_sensitivity_test(8))
print(analyzer.enamel_strength_check(7, 1))
print(analyzer.grinding_teeth_risk(8, 6))
print(analyzer.oral_hygiene_score(2, 1, ['sugar']))
print(analyzer.analyze_teeth_condition("download.jpeg"))
