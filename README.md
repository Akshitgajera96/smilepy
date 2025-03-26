# SmilePy - Dental Analysis Tool

SmilePy is a Python-based dental analysis tool that helps assess various aspects of oral health using image processing and diagnostic parameters.

## Features

- Cavity detection from dental images
- Gum health assessment
- Teeth whiteness measurement
- Bad breath risk analysis
- Teeth alignment checking
- Plaque detection
- Tooth sensitivity evaluation
- Enamel strength assessment
- Teeth grinding risk analysis
- Overall oral hygiene scoring
- Comprehensive teeth condition analysis

## Installation

1. Ensure you have Python installed on your system
2. Install required dependencies:
```bash
pip install opencv-python numpy
```

## Usage

### Basic Example
```python
from teethanalyzer import TeethAnalyzer
from datetime import datetime

# Create an analyzer instance
analyzer = TeethAnalyzer()

# Analyze teeth from an image
image_path = "path/to/your/teeth/image.jpg"
print(analyzer.analyze_teeth_condition(image_path))
```

### Available Functions

1. **Cavity Detection**
   ```python
   analyzer.detect_cavities(image_path)
   ```

2. **Gum Health Check**
   ```python
   # redness_level: 0-100 (higher means more red/inflamed)
   analyzer.check_gum_health(redness_level)
   ```

3. **Teeth Whiteness**
   ```python
   analyzer.measure_teeth_whiteness(image_path)
   ```

4. **Bad Breath Risk**
   ```python
   # Pass current time and list of consumed foods
   analyzer.bad_breath_risk(datetime.now(), ['garlic', 'onion'])
   ```

5. **Teeth Alignment**
   ```python
   # Pass list of teeth positions (negative values indicate inward positioning)
   analyzer.teeth_alignment_check([1, -2, 3, 6, -7])
   ```

6. **Plaque Detection**
   ```python
   # plaque_level: 0-100
   analyzer.plaque_detection(80)
   ```

7. **Sensitivity Test**
   ```python
   # response_to_cold: 1-10 (higher means more sensitive)
   analyzer.tooth_sensitivity_test(8)
   ```

8. **Enamel Strength**
   ```python
   # acid_exposure: 1-10, brushing_habit: 1-10
   analyzer.enamel_strength_check(7, 1)
   ```

9. **Grinding Risk**
   ```python
   # stress_level: 1-10, jaw_pain: 1-10
   analyzer.grinding_teeth_risk(8, 6)
   ```

10. **Oral Hygiene Score**
    ```python
    # brushing: times per day, flossing: times per day, diet: list of foods
    analyzer.oral_hygiene_score(2, 1, ['sugar'])
    ```

## Notes for Patients

- For image analysis features, ensure good lighting and clear photos of your teeth
- Be honest with the input parameters for accurate results
- This tool is for preliminary assessment only and does not replace professional dental consultation
- Always consult a dentist for proper diagnosis and treatment

## Technical Requirements

- Python 3.6+
- OpenCV
- NumPy
- Sufficient lighting for dental images
- Clear, focused images of teeth for analysis

## Disclaimer

This tool is for educational and preliminary assessment purposes only. It should not be used as a substitute for professional dental care or diagnosis.
