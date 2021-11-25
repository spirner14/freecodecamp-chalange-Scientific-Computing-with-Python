class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def __str__(self):
        # > - right alighn
        # ^ - center
        # 'f' - Fixed point. Displays the number as a fixed-point number.
        title = f"{self.name:*^30}\n"
        middle = ""
        for i in self.ledger:
            middle += f"{i.get('description')[0:23]:23}" + f"{i.get('amount'):>7.2f}\n"
        return title + middle + "Total: " + str(self.get_balance())

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount) is True:
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        balance = 0
        for i in self.ledger:
            balance += i.get("amount")
        return balance

    def transfer(self, amount, transfer_to):
        if self.check_funds(amount) is True:
            self.withdraw(amount, "Transfer to " + transfer_to.name)
            transfer_to.deposit(amount, "Transfer from " + self.name)
            return True
        return False

    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        return True

    def category_total(self):
        cat_total = 0
        for i in self.ledger:
            if i.get("amount") < 0:
                cat_total += i.get("amount")
                # return (cat_total / Category.total * 100) // 10 * 10
        return cat_total

    def get_total(self, categories):
        total = 0
        for category in categories:
            total += category.category_total()
        return total

    def procentage_spent(self, categories):
        cat_total = 0
        for i in self.ledger:
            if i.get("amount") < 0:
                cat_total += i.get("amount")
                # return (cat_total / Category.total * 100) // 10 * 10
        return ((cat_total / self.get_total(categories) * 100) // 10 * 10)


# returns a string that is a bar chart.
def create_spend_chart(categories):
    top = "Percentage spent by category\n"
    # prints procentages and "o"
    procent = ""
    for i in range(100, -1, -10):
        procent += f"{i:3d}| "
        for category in categories:
            if category.procentage_spent(categories) >= i:
                procent += "o" + " " * 2
            else:
                procent += " " * 3
            if category == categories[-1]:
                procent += "\n"
    spacer = " " * 4 + "-"
    bottom = spacer + "-" * 3 * len(categories) + "\n"

    # max length of category
    max_ = 0
    for category in categories:
        max_ = max(len(category.name), max_)
    # prints name of category
    name = ""
    for i in range(max_):
        name += " " * 5
        for category in categories:
            try:
                name += category.name[i] + " " * 2
            except IndexError:
                name += " " * 3
            # when there is last letter we dont need \n
            if category == categories[-1] and i == max_ - 1:
                name += ""
            # we need \n if it isn't the last one
            elif category == categories[-1]:
                name += "\n"

    return top + procent + bottom + name

# food = Category("Food")
# food.deposit(1000, "initial deposit")
# food.withdraw(10.15, "groceries")
# food.withdraw(15.89, "restaurant and more food for dessert")
# clothing = Category("Clothing")
# food.transfer(50, clothing)
# clothing.withdraw(25.55)
# clothing.withdraw(100)
# auto = Category("Auto")
# auto.deposit(1000, "initial deposit")
# auto.withdraw(15)
# print(create_spend_chart([food, clothing, auto]))

food = Category("Food")
entertainment = Category("Entertainment")
business = Category("Business")
food.deposit(900, "deposit")
entertainment.deposit(900, "deposit")
business.deposit(900, "deposit")
food.withdraw(105.55)
entertainment.withdraw(33.40)
business.withdraw(10.99)
print(create_spend_chart([business, food, entertainment]))






