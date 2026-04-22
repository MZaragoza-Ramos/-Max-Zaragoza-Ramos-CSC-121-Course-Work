class Employee:
    """Collect and store employee information"""

    def __init__(self, first, last, annual_salary):
        """Gets the employee's name and annual salary."""
        self.first = first
        self.last = last
        self.annual_salary = annual_salary

    def give_raise(self, raise_amount=5000):
        """Gives the employee a raise"""
        self.annual_salary += raise_amount
