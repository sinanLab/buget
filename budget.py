class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        balance = 0
        for transaction in self.ledger:
            balance += transaction["amount"]
        return balance

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        total = 0
        for transaction in self.ledger:
            items += f"{transaction['description'][:23]:23}" + f"{transaction['amount']:7.2f}\n"
            total += transaction['amount']
        output = title + items + "Total: " + str(total)
        return output

def create_spend_chart(categories):
    # Calculate the percentage spent in each category
    total_withdrawals = 0
    category_spending = []
    for category in categories:
        category_withdrawals = 0
        for transaction in category.ledger:
            if transaction['amount'] < 0:
                category_withdrawals -= transaction['amount']
                total_withdrawals -= transaction['amount']
        category_spending.append(category_withdrawals)

    # Calculate the percentage spent for each category
    percentages = []
    for spending in category_spending:
        percentage = spending / total_withdrawals * 100
        percentage = int(percentage // 10) * 10  # Round down to nearest 10
        percentages.append(percentage)

    # Create the spend chart
    chart = "Percentage spent by category\n"
    for i in range(100, -10, -10):
        chart += f"{i:3d}| "
        for percentage in percentages:
            if percentage >= i:
                chart += "o  "
            else:
                chart += "   "
        chart += "\n"

    chart += "    " + "-" * (3 * len(categories) + 1) + "\n"

    # Find the longest category name
    max_name_length = max(len(category.name) for category in categories)

    # Add category names vertically
    for i in range(max_name_length):
        chart += "     "
        for category in categories:
            if i < len(category.name):
                chart += category.name[i] + "  "
            else:
                chart += "   "
        chart += "\n"

    return chart
