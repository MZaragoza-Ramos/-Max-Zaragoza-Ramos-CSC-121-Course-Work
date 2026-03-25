class User:
    """Creating a user's profile and adding more information."""
    def __init__(self, first_name, last_name, birth_year, followers):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year
        self.followers = followers
        self.login_attempts = 0

    def describe_user(self):
        """Summary of the user and their additional information"""
        full_name = f"{self.first_name} {self.last_name}"
        print(f"The user is {full_name.title()}.")
        message = f"They were born in {self.birth_year}"
        message += f" and they have {self.followers} followers!"
        print(message)

    def greet_user(self):
        """Makes a personalized greeting for the user."""
        full_name = f"{self.first_name} {self.last_name}"
        print(f"\nHello, {full_name.title()}!")

    def increment_login_attempts(self, attempts):
        """Increments the value of login attempts"""
        self.login_attempts += attempts
        print(f"\nYou have tried to login {self.login_attempts} times.")
    
    def reset_login_attempts(self):
        """Resets the value of login attempts to 0"""
        self.login_attempts = 0
        print("\nYour login attempts have been reset!")

my_profile = User('max', 'zaragoza', 2005, 100)
my_profile.describe_user()
my_profile.greet_user()
my_profile.increment_login_attempts(1)
my_profile.increment_login_attempts(1)
my_profile.increment_login_attempts(1)
my_profile.reset_login_attempts()
print(f"\nCurrent Number of login attempts: {my_profile.login_attempts}")