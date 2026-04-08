"""A set of modules to describe user and admin privileges."""

class Users:
    def __init__(self, first_name, last_name, username, age, location, gender, email, login_attempts):
        """Intializes user attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.age = age
        self.location = location
        self.gender = gender
        self.email = email
        self.login_attempts = login_attempts

    def desc_user(self):
        """Prints a summary which describes the user's profile."""
        print(f"Summary of {self.username}'s profile:")
        print(f"\tfirst name: {self.first_name}, last name: {self.last_name}, age: {self.age}")
        print(f"\tlocation: {self.location}, gender: {self.gender}, email address: {self.email}\n")

    def greet_user(self):
        """Prints a personalized greeting to each user."""
        print(f"Hello {self.username}, welcome to your profile.")

class Admin(Users):
    """represents admin profile properties """
    def __init__(self, first_name, last_name, username, age, location, gender, email, login_attempts):
        # Initalize attributes of parent class
        super().__init__(first_name, last_name, username, age, location, gender, email, login_attempts)
        # Initialize attributes specific to Admin class."""
        self.privileges = Privileges()

class Privileges():
    """models privileges of Admin user"""
    def __init__(self):
        """Initalize admin privileges attributes."""
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        """lists the administrator's set of privilges."""
        print(f"Current list of admin privileges:\n\t{self.privileges}")    