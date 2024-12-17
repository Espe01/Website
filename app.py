from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dictionary to store detailed meal plans
meal_plans = {
    "weight_loss": {
        "description": "This is a weight loss plan focusing on calorie deficit and high protein intake.",
        "meals": [
            {
                "name": "Breakfast",
                "details": "Oatmeal with berries and a protein shake"
            },
            {
                "name": "Lunch",
                "details": "Grilled chicken salad with mixed greens and vinaigrette"
            },
            {
                "name": "Dinner",
                "details": "Baked salmon with steamed vegetables"
            },
            {
                "name": "Snacks",
                "details": "Greek yogurt with honey and almonds"
            }
        ]
    },
    "muscle_gain": {
        "description": "This plan is designed for muscle gain with a focus on high protein and moderate carbs.",
        "meals": [
            {
                "name": "Breakfast",
                "details": "Scrambled eggs with spinach and whole grain toast"
            },
            {
                "name": "Lunch",
                "details": "Turkey and avocado wrap with a side of quinoa"
            },
            {
                "name": "Dinner",
                "details": "Beef stir-fry with brown rice"
            },
            {
                "name": "Snacks",
                "details": "Protein bar and a banana"
            }
        ]
    },
    "maintenance": {
        "description": "This plan helps maintain your current weight with a balanced intake of all macros.",
        "meals": [
            {
                "name": "Breakfast",
                "details": "Greek yogurt with granola and fresh fruit"
            },
            {
                "name": "Lunch",
                "details": "Grilled chicken sandwich with a side of mixed vegetables"
            },
            {
                "name": "Dinner",
                "details": "Pasta with marinara sauce and a side salad"
            },
            {
                "name": "Snacks",
                "details": "Apple slices with peanut butter"
            }
        ]
    },
    "keto": {
        "description": "This ketogenic plan focuses on high fats, moderate protein, and low carbs.",
        "meals": [
            {
                "name": "Breakfast",
                "details": "Avocado and bacon omelette"
            },
            {
                "name": "Lunch",
                "details": "Caesar salad with grilled chicken (no croutons)"
            },
            {
                "name": "Dinner",
                "details": "Steak with butter and asparagus"
            },
            {
                "name": "Snacks",
                "details": "Cheese sticks and almonds"
            }
        ]
    },
    "vegan": {
        "description": "This vegan plan ensures you get all necessary nutrients through plant-based foods.",
        "meals": [
            {
                "name": "Breakfast",
                "details": "Smoothie with almond milk, spinach, banana, and protein powder"
            },
            {
                "name": "Lunch",
                "details": "Chickpea salad wrap with a side of fruit"
            },
            {
                "name": "Dinner",
                "details": "Lentil curry with brown rice"
            },
            {
                "name": "Snacks",
                "details": "Hummus with carrot sticks"
            }
        ]
    }
}

# Dictionary to store detailed fitness programs
fitness_programs = {
    "weight_loss": {
        "description": "A weight loss program focusing on high-intensity interval training (HIIT) and cardio exercises.",
        "program": {
            "Monday": ["20 min HIIT workout", "30 min steady-state cardio"],
            "Tuesday": ["Full-body strength training", "15 min HIIT workout"],
            "Wednesday": ["30 min brisk walking", "20 min yoga"],
            "Thursday": ["20 min HIIT workout", "30 min steady-state cardio"],
            "Friday": ["Upper body strength training", "15 min HIIT workout"],
            "Saturday": ["30 min cycling", "20 min stretching"],
            "Sunday": ["Rest day"]
        }
    },
    "muscle_gain": {
        "description": "A muscle gain program focusing on strength training and progressive overload.",
        "program": {
            "Monday": ["Chest and triceps workout", "20 min cardio"],
            "Tuesday": ["Back and biceps workout", "20 min cardio"],
            "Wednesday": ["Legs workout", "20 min cardio"],
            "Thursday": ["Shoulders and abs workout", "20 min cardio"],
            "Friday": ["Full-body strength training", "20 min cardio"],
            "Saturday": ["Active recovery (light yoga or stretching)", "30 min brisk walking"],
            "Sunday": ["Rest day"]
        }
    },
    "general_fitness": {
        "description": "A general fitness program focusing on overall health and well-being.",
        "program": {
            "Monday": ["Full-body workout", "30 min steady-state cardio"],
            "Tuesday": ["Yoga or Pilates", "20 min light jogging"],
            "Wednesday": ["Upper body strength training", "30 min brisk walking"],
            "Thursday": ["Lower body strength training", "20 min cycling"],
            "Friday": ["Core and abs workout", "30 min steady-state cardio"],
            "Saturday": ["Active recovery (light yoga or stretching)", "30 min brisk walking"],
            "Sunday": ["Rest day"]
        }
    },
    "weight_gain": {
        "description": "A weight gain program focusing on muscle hypertrophy and compound movements.",
        "program": {
            "Monday": ["Upper body strength training", "20 min light cardio"],
            "Tuesday": ["Lower body strength training", "20 min light cardio"],
            "Wednesday": ["Full-body workout", "20 min light cardio"],
            "Thursday": ["Active recovery (light yoga or stretching)", "30 min brisk walking"],
            "Friday": ["Upper body strength training", "20 min light cardio"],
            "Saturday": ["Lower body strength training", "20 min light cardio"],
            "Sunday": ["Rest day"]
        }
    }
}

@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Handle login logic here
        return redirect(url_for('home'))
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Handle signup logic here
        return redirect(url_for('home'))
    return render_template('signup.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/nutrition', methods=['GET', 'POST'])
def nutrition():
    plan_details = None
    if request.method == 'POST':
        plan = request.form.get('nutrition_plan')
        plan_details = meal_plans.get(plan, {"description": "No plan selected", "meals": []})
    return render_template('nutrition.html', plan_details=plan_details)

@app.route('/fitness', methods=['GET', 'POST'])
def fitness():
    program_details = None
    if request.method == 'POST':
        goal = request.form.get('fitness_goal')
        program_details = fitness_programs.get(goal, {"description": "No program selected", "program": {}})
    return render_template('fitness.html', program_details=program_details)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/signout')
def signout():
    # Here you can add any signout logic, such as clearing session data
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
