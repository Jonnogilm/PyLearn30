import statistics

ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
class Statistics:
    def __init__(self, lst):
        self.lst = lst

    def count(self):
        return len(self.lst)
    def sum(self):
        return sum(self.lst)
    def min(self):
        return min(self.lst)
    def max(self):
        return max(self.lst)
    def range(self):
        return self.max()-self.min()
    def mean(self):
        return statistics.mean(self.lst)
    def median(self):
        return statistics.median(self.lst)
    def mode(self):
        return statistics.mode(self.lst)
    def std(self):
        return statistics.stdev(self.lst)
    def var(self):
        return statistics.variance(self.lst)
    def describe(self):
        return {
            'Count': self.count(),
            'Sum': self.sum(),
            'Min': self.min(),
            'Max': self.max(),
            'Range': self.range(),
            'Mean': self.mean(),
            'Median': self.median(),
            'Mode': self.mode(),
            'Standard Deviation': self.std(),
            'Variance': self.var()
        }
data = Statistics(ages)
print(data.describe())

'''Create a class called PersonAccount. It has firstname, lastname, incomes, expenses properties and it has total_income, total_expense, account_info, add_income, add_expense and account_balance methods. 
Incomes is a set of incomes and its description. The same goes for expenses.'''
class PersonAccount:
    def __init__(self, firstname, lastname, incomes, expenses):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = incomes
        self.expenses = expenses
    
    def total_income(self):
        return sum(self.incomes.values())
    def total_expense(self):
        return sum(self.expenses.values()) # need list()?
    def account_info(self):
        return self.incomes.keys()
    def add_income(self, description, income):
        self.incomes[description] = income
    def add_expense(self, description, expense):
        self.expenses[description] = expense
    def account_balance(self):
        return self.total_income() - self.total_expense()

person1 = PersonAccount(
    "Jonathan",
    "Gilmer",
    {
        "Salary": 4500,
        "Freelance": 1200,
        "Dividends": 300
    },
    {
        "Rent": 1800,
        "Food": 450,
        "Gas": 120,
        "Internet": 80
    }
)

print(person1.account_info())

print("Total Income:", person1.total_income())
print("Total Expense:", person1.total_expense())
print("Account Balance:", person1.account_balance())

person1.add_income("Tutoring", 250)
person1.add_expense("Gym", 60)

print("\nAfter updates:\n")

print(person1.account_info())

print("Total Income:", person1.total_income())
print("Total Expense:", person1.total_expense())
print("Account Balance:", person1.account_balance())