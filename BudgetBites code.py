# Step 1: Gather User Input
budget = float(input("Enter your budget for the meal: "))
time_constraints = int(input("Enter your time constraints in minutes: "))
calorie_preference = int(input("Enter your calorie intake preference: "))
dietary_requirements = input("Enter your dietary requirements (e.g., vegetarian, vegan, none etc.): ")

# Step 2: Search Database (this is a mock database)
filtered_recipes = [
    {
        "name": "Salad",
        "budget": 10,
        "time": 15,
        "calories": 200,
        "diet": "vegetarian",
        "ingredients": ["Lettuce", "Tomato", "Cucumber", "Olive oil"],
        "steps": ["Chop vegetables", "Mix in a bowl", "Add olive oil"]
    },
     {
        "name": "Chicken Soup",
        "budget": 15,
        "time": 30,
        "calories": 300,
        "diet": "non-vegetarian",
        "ingredients": ["Chicken", "Carrots", "Onions", "Celery", "Broth"],
        "steps": ["Boil chicken", "Add vegetables", "Simmer until cooked"]
    },
    {
        "name": "Vegan Stir Fry",
        "budget": 12,
        "time": 20,
        "calories": 250,
        "diet": "vegan",
        "ingredients": ["Tofu", "Bell peppers", "Soy sauce", "Garlic"],
        "steps": ["Chop tofu and vegetables", "Stir - fry in a pan", "Add soy sauce and garlic"]
    },
     {
        "name": "Pasta Primavera",
        "budget": 14,
        "time": 25,
        "calories": 350,
        "diet": "vegetarian",
        "ingredients": ["Pasta", "Bell peppers", "Zucchini", "Parmesan cheese", "Olive oil"],
        "steps": ["Cook pasta", "Sauté vegetables", "Mix pasta and vegetables", "Top with Parmesan cheese"]
    },
    {
        "name": "Beef Tacos",
        "budget": 18,
        "time": 20,
        "calories": 400,
        "diet": "non-vegetarian",
        "ingredients": ["Ground beef", "Taco shells", "Lettuce", "Cheese", "Salsa"],
        "steps": ["Cook ground beef", "Fill taco shells with beef", "Add lettuce, cheese, and salsa"]
    },
    {
        "name": "Quinoa Salad",
        "budget": 12,
        "time": 15,
        "calories": 220,
        "diet": "vegan",
        "ingredients": ["Quinoa", "Cherry tomatoes", "Cucumber", "Lemon juice", "Olive oil"],
        "steps": ["Cook quinoa", "Chop vegetables", "Mix quinoa and vegetables", "Add lemon juice and olive oil"]
    },
     {
        "name": "Grilled Cheese Sandwich",
        "budget": 5,
        "time": 10,
        "calories": 300,
        "diet": "vegetarian",
        "ingredients": ["Bread", "Cheese", "Butter"],
        "steps": ["Butter the bread", "Place cheese between slices", "Grill until golden brown"]
    },
    {
        "name": "Shrimp Scampi",
        "budget": 20,
        "time": 25,
        "calories": 450,
        "diet": "pescatarian",
        "ingredients": ["Shrimp", "Garlic", "Butter", "Lemon", "Pasta"],
        "steps": ["Cook pasta", "Sauté shrimp with garlic and butter", "Mix shrimp with pasta and lemon juice"]
    },
    {
        "name": "Lentil Soup",
        "budget": 10,
        "time": 30,
        "calories": 250,
        "diet": "vegan",
        "ingredients": ["Lentils", "Carrots", "Onions", "Celery", "Broth"],
        "steps": ["Sauté vegetables", "Add lentils and broth", "Simmer until lentils are tender"]
    }
    # Add more recipes as needed
]


#Step 3: Filter recipes:
filtered_recipes = [
    recipe for recipe in filtered_recipes
    if recipe["budget"] <= budget and
       recipe["time"] <= time_constraints and
       recipe["calories"] <= calorie_preference and
       recipe["diet"].lower() == dietary_requirements.lower()

]

# Step 4: Output the filtered recipes
if filtered_recipes:
    print("Here are the recipes that match your preferences:")
    for recipe in filtered_recipes:
        print(f"Recipe Name: {recipe['name']}")
        print(f"Budget: £{recipe['budget']}")
        print(f"Time: {recipe['time']} minutes")
        print(f"Calories: {recipe['calories']} kcal")
        print(f"Ingredients: {recipe['ingredients']}")
        print(f"Dietary Requirements: {recipe['diet']}")
        print(f"Steps: {recipe['steps']}")
else:
    print("No recipes match your preferences.")