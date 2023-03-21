class Category:
    def __init__(self, Category):
        self.Category = Category  # Initialize the category name
        self.ledger = []  # Initialize the ledger for the category

    def deposit(self, amount, description=''):
        # Add a deposit entry to the ledger
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description):
        total_amount = self.get_balance()
        # Check if withdrawal amount is less than or equal to the total amount
        if amount <= total_amount:
            self.ledger.append({'amount': -1 * amount, 'description': description})
            return True
        else:
            return False

    def get_balance(self):
        # Calculate the total balance of the category
        try:
            return sum(list(map(lambda x: x['amount'], self.ledger)))
        except:
            return 0

    def transfer(self, amount, destination):
        # Check if the destination is a valid Category object and not the same category
        if not isinstance(destination, Category) or (
                isinstance(destination, Category) and destination.Category == self.Category):
            return False
        sente = 'Transfer to ' + destination.Category
        if self.withdraw(amount, sente):
            destination.deposit(amount, 'Transfer from ' + self.Category)
            return True
        else:
            return False

    def check_funds(self, amount):
        total_amount = self.get_balance()

        if amount <= total_amount:
            return True
        else:
            return False

    def __str__(self):
        # Create a string representation of the Category object
        len_cat = len(list(self.Category))
        num_asterk = len_cat // 2
        if len_cat % 2:
            num_asterk += 1
        line_1 = ''
        for i in range(15 - num_asterk):
            line_1 += '*'
        line_1 += self.Category
        for i in range(30 - len(list(line_1))):
            line_1 += '*'
        line_1 += '\n'

        # Add ledger entries to the string representation
        for moves in self.ledger:
            amount = moves['amount']
            description = moves['description']
            description = f'{description:.23s}'
            idx = 30 - (len(list(str(int(amount)))) + 3)
            line_1 += description
            for i in range(len(list(description)), idx):
                line_1 += ' '
            line_1 += f'{amount:.2f}'
            line_1 += '\n'

        # Add the total balance to the string representation
        line_1 += f'Total: {self.get_balance():.2f}'
        return line_1


def create_spend_chart(list_cat):
    # Calculate spending per category
    list_with = [-1 * sum(list(map(lambda x: x['amount'] if x['amount'] < 0 else 0, cat.ledger))) for cat in list_cat]
    list_per = [int(round(100 * cat / sum(list_with), -1)) for cat in list_with]

    # Print the spending chart
    for per in range(100, -10, -10):
        num_space = 3 - len(list(str(per)))
        line = ''
        for j in range(num_space):
            line += ' '
        line += f'{per}| '
        for x in list_per:
            if per <= x:
                line += 'o'
            else:
                line += ' '
            line += '  '
        print(line)
    line = '    ' 
    for i in range(1+len(list_per)+2*len(list_per)):
        line += '-'
    print(line)

    # Print the category names vertically
    max_let = max([len(list(cat.Category)) for cat in list_cat])
    list_names = []
    for cat in list_cat:
        name = cat.Category[:]
        for letter in range(max_let-len(list(cat.Category))):
            name+= ' '
        list_names.append(name)

    for let in range(max_let):
        line = '     '
        for name in list_names:
            line += name[let]
            line += '  '
        print(line)