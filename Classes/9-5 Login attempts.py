""" Utilized users.py program, to add a new attribute called login_attempts which tracks
the number of login attempts by user's associated with the User class. Added two additional 
methods (increment_login_attempts and rest_login_attempts) to simulate a user attempting to
log into their profile several times, unsuccessfuly. Afterwards, login attempts is reset back to 0. 
"""

class Users:
    def __init__(self, first_name, last_name, username, age, location, gender, email, login_attempts=0):
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
        print(f"\tlocation: {self.location}, gender: {self.gender}, email address: {self.email}")

    def greet_user(self):
        """Prints a personalized greeting to each user."""
        print(f"Hello {self.username}, welcome to your profile.")

    def increment_login_attempts(self, login):
        """increments login attempts by user"""
        self.login_attempts += login

    def reset_login_attempts(self):
        """resets the value of login_attempts to 0."""
        self.login_attempts = 0

# Create an instance
user_1 = Users('Rick', 'Hansen', 'rhenk93', '52', 'UK', 'male', 'rhen93@aol.com')
user_1.greet_user()
user_1.desc_user()

# Simulate several login attempts by user
user_1.increment_login_attempts(1)
user_1.increment_login_attempts(1)
user_1.increment_login_attempts(1)
user_1.increment_login_attempts(1)
user_1.increment_login_attempts(1)
user_1.increment_login_attempts(1)
user_1.increment_login_attempts(1)
user_1.increment_login_attempts(1)
user_1.increment_login_attempts(1)
user_1.increment_login_attempts(1)
user_1.increment_login_attempts(1)
user_1.increment_login_attempts(1)
user_1.increment_login_attempts(1)
user_1.increment_login_attempts(1)
user_1.increment_login_attempts(1)
user_1.increment_login_attempts(1)
user_1.increment_login_attempts(1)
user_1.increment_login_attempts(1)

# print total value of login attempts by user
print(f"\tlogin attempts:{user_1.login_attempts}")

# Reset login attempts to 0
user_1.reset_login_attempts()
print(f"\tlogin attempts reset:{user_1.login_attempts}")

