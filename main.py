class Category:
    def __init__(self, description):
        self.description = description
        self.ledger = []

    def deposit(self, amount, description=''):
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append({'amount': -1 * amount, 'description': description})
            return True 
        else:
            return False
    
    def transfer(self, amount, other_category):
        if self.withdraw(amount, f'Transfer to {other_category.description}'):
            other_category.deposit(amount, f'Transfer from {self.description}')
            return True
        return False
            
    def get_balance(self):
        total = sum(item['amount'] for item in self.ledger)
        return total

    def check_funds(self, amount):
        return self.get_balance() >= amount
        
    def __str__(self):
        line = f'{self.description.center(30, "*")}' + '\n'
        for item in self.ledger:
            desc = item['description']
            amt = item['amount']
            line += f'{desc[:23]:<23}{amt:>7.2f}\n'
        line += f'Total: {str(self.get_balance())}'

        return line


def create_spend_chart(categories):
    costs = []
    percentages = []

    for category in categories:
        spent = 0
        for item in category.ledger:
            if item['amount'] < 0:
                spent += item['amount']
        costs.append(spent)
    total_spent = sum(costs)

    for index, _ in enumerate(categories):
        percent = int((costs[index] / total_spent) * 100 // 10) * 10
        percentages.append(percent)
    chart = 'Percentage spent by category\n'

    for i in range(100, -1, -10):
        chart += f'{i:>3}|'
        for discount in percentages:
            if discount >= i:
                chart += ' o '
            else:
                chart += '   '
        chart += ' \n'

    names = [cat.description for cat in categories]
    longest = max(names, key=len)
    pillar = ''
    names = [item.ljust(len(longest)) for item in names]

    rows = ['     ' + '  '.join(letter) + '  ' for letter in zip(*names)]
    pillar = "\n".join(rows)

    line = "    " + "-" * (len(categories) * 3 + 1) + "\n"

    pillar = chart + line + pillar
    return pillar.rstrip('\n')
        

if __name__ == "__main__":
    food = Category("Food")
    food.deposit(1000, "initial deposit")
    food.withdraw(10.15, "groceries")

    clothing = Category("Clothing")
    food.transfer(50, clothing)
    clothing.withdraw(25.55, "t-shirt")

    entertainment = Category("Entertainment")
    entertainment.deposit(500, "initial deposit")
    entertainment.withdraw(150, "movies")

    categories = [food, clothing, entertainment]
    for category in categories:
        print(category)
    print(create_spend_chart(categories))
