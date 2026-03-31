"""Created several instances representing different users, with different attributes,
each associated to a class called Users.Implemented one method that prints out a 
summary of the user's information. Implemented a second method that prints out a 
personalized messsage to the user."""

class Users:
    def __init__(self, first_name, last_name, username, age, location, gender, email):
        """Intializes user attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.age = age
        self.location = location
        self.gender = gender
        self.email = email

    def desc_user(self):
        """Prints a summary which describes the user's profile."""
        print(f"Summary of {self.username}'s profile:")
        print(f"\tfirst name: {self.first_name}, last name: {self.last_name}, age: {self.age}")
        print(f"\tlocation: {self.location}, gender: {self.gender}, email address: {self.email}\n")

    def greet_user(self):
        """Prints a personalized greeting to each user."""
        print(f"Hello {self.username}, welcome to your profile.")

# Create instances with different attributes
user_1 = Users('Rick', 'Hansen', 'rhenk93', '52', 'UK', 'male', 'rhen93@aol.com')
user_1.greet_user()
user_1.desc_user()

user_2 = Users('Milo', 'Harrington', 'milo_harr', '32', 'Denver, CO', 'male', 'milo.harrington@skytrail.io')
user_2.greet_user()
user_2.desc_user()

user_3 = Users('Serena', 'Vale', ' serenav_92', '28', 'Tampa, FL', 'female', 'serena.vale@luminet.app')
user_3.greet_user()
user_3.desc_user()

user_4 = Users('Kieran', 'Moss', 'moss.k', '24', 'Portlan, OR', 'nonbinary', 'kieran.moss@northforge.dev')
user_4.greet_user()
user_4.desc_user()

user_5 = Users('Amara', 'Dupont', 'amaradp', '45', 'Chicago, IL', 'female', 'amara.dupont@metroline.org')
user_5.greet_user()
user_5.desc_user()

user_6 = Users('Theo', 'Rusk', 'trusk27', '30', 'Boston, MA', 'male', 'theo.rusk@bytehaven.co')
user_6.greet_user()
user_6.desc_user()

user_7 = Users('Nadia', 'Kelm', 'nadia_kelm', '37', 'Phoenix, AZ', 'female', 'nadia.kelm@suncrestmail.net')
user_7.greet_user()
user_7.desc_user()

user_8 = Users('Jalen', 'Brooks', 'jbrooks45', '41', 'Atlanta, GA', 'male', 'jalen.brooks@urbanwave.us')
user_8.greet_user()
user_8.desc_user()

user_9 = Users('Riku', 'Tanaka', 'riku_tnk', '34', 'Seattle, WA', 'male', 'riku.tanaka@pacificpulse.m')
user_9.greet_user()
user_9.desc_user()

user_10 = Users('Harper', 'Quinn', 'hquinn_tx', '26', 'Austin, TX', 'female', 'harper.quinn@lumenlane.dev')
user_10.greet_user()
user_10.desc_user()

user_11 = Users('Evan', 'Corbett', 'evc_phl', '33', 'Philadelphia, PA', 'male', 'evan.corbett@keystonehub.org')
user_11.greet_user()
user_11.desc_user()

user_12 = Users('Sahana', 'Patel', 'sahana_p28', '28', 'San Francisco, CA', 'female', 'sahana.patel@cloudcrest.dev')
user_12.greet_user()
user_12.desc_user()

user_13 = Users('Markus', 'Feld', 'markusf52', '52', 'Milwaukee, WI', 'male', 'markus.feld@midwestconnect.biz')
user_13.greet_user()
user_13.desc_user()

user_14 = Users('Nova', 'Redd', 'nova_r24', '24', 'New York, NY', 'nonbinary', 'nova.redd@skylinewave.com')
user_14.greet_user()
user_14.desc_user()



