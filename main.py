# Import the necessary classes and functions from budget.py
from budget import Category, create_spend_chart

# Create instances of Category
food_category = Category("Food")
clothing_category = Category("Clothing")
entertainment_category = Category("Entertainment")

# Perform operations on the categories
food_category.deposit(1000, "initial deposit")
food_category.withdraw(10.15, "groceries")
food_category.withdraw(15.89, "restaurant and more food")
food_category.transfer(50, clothing_category)

clothing_category.deposit(500, "initial deposit")
clothing_category.withdraw(25.55, "clothes")
clothing_category.withdraw(100, "accessories")

entertainment_category.deposit(100, "initial deposit")
entertainment_category.withdraw(15, "movie tickets")
entertainment_category.withdraw(10, "popcorn")

# Print the categories
print(food_category)
print(clothing_category)
print(entertainment_category)

# Create a spend chart
categories = [food_category, clothing_category, entertainment_category]
spend_chart = create_spend_chart(categories)
print(spend_chart)
