from datetime import datetime

class DietTeethCare:
    def __init__(self):
        self.food_recommendations = {
            "calcium": ["Milk", "Cheese", "Yogurt", "Almonds"],
            "vitamin_d": ["Salmon", "Egg Yolks", "Mushrooms"],
            "phosphorus": ["Fish", "Lean Meat", "Nuts"],
            "crunchy_fruits_veggies": ["Apples", "Carrots", "Celery"],
            "green_tea": ["Rich in antioxidants to reduce gum inflammation"],
            "water": ["Keeps the mouth hydrated and washes away food particles"],
            "strong_teeth": ["Calcium", "Vitamin D", "Phosphorus", "Crunchy Fruits & Veggies"],
            "cavity_protection": ["Calcium", "Vitamin D", "Phosphorus", "Crunchy Fruits & Veggies"],
            "gum_health": ["Green Tea", "Water"],
            "avoid": ["Sugary Snacks", "Soda", "Acidic Foods", "Sticky Candy"],
            "sugar_intake": ["Limit sugar intake to less than 20g per day"],
        }
        self.user_diet_log = {}
    
    def get_food_suggestions(self, concern):
        """Returns food recommendations based on concern."""
        return self.food_recommendations.get(concern, "Invalid category")
    
    def personalized_diet_plan(self, user_age, existing_issues):
        """Generates a diet plan based on age and dental condition."""
        diet_plan = set()
        if user_age < 18:
            diet_plan.update(self.food_recommendations["strong_teeth"])
        if "cavities" in existing_issues:
            diet_plan.update(self.food_recommendations["cavity_protection"])
        if "gum_issues" in existing_issues:
            diet_plan.update(self.food_recommendations["gum_health"])
        return list(diet_plan)
    
    def evaluate_sugar_intake(self, daily_sugar_intake):
        """Analyzes if sugar intake is excessive."""
        if daily_sugar_intake < 20:
            return "Low Risk"
        elif daily_sugar_intake < 50:
            return "Moderate Risk"
        return "High Risk - Reduce sugar intake!"
    
    def detect_unhealthy_diet_patterns(self, food_list):
        """Detects unhealthy eating habits."""
        unhealthy_items = [food for food in food_list if food in self.food_recommendations["avoid"]]
        return f"Warning! Reduce: {', '.join(unhealthy_items)}." if unhealthy_items else "Your diet looks healthy!"
    
    def log_user_meal(self, user_id, meal, date=None):
        """Logs user's food intake."""
        date = date or datetime.now().strftime('%Y-%m-%d')
        self.user_diet_log.setdefault(user_id, []).append({"date": date, "meal": meal})
        return "Meal logged successfully."
    
    def get_diet_history(self, user_id):
        """Retrieves past diet history."""
        return self.user_diet_log.get(user_id, "No records found.")
    
    def generate_weekly_diet_report(self, user_id):
        """Analyzes past food intake and provides a diet score."""
        meals = self.user_diet_log.get(user_id, [])
        healthy_count = sum(1 for meal in meals if "avoid" not in meal["meal"])
        score = (healthy_count / max(len(meals), 1)) * 100
        return f"Weekly Diet Score: {score:.2f}% - Keep up the good work!" if meals else "No data available."
    
    def recommend_tooth_friendly_snacks(self):
        """Suggests teeth-friendly snack options."""
        return ["Cheese", "Nuts", "Yogurt", "Carrots", "Apples", "Sugar-free gum"]
    
    def predict_teeth_health_trend(self, user_id):
        """Predicts dental health trends based on diet habits."""
        meals = self.user_diet_log.get(user_id, [])
        unhealthy_count = sum(1 for meal in meals if "avoid" in meal["meal"])
        return "Warning! Your diet may lead to cavities soon." if unhealthy_count > 5 else "Your diet supports good dental health!"
