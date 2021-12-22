class User:
    def __init__(self, username, name, email):
        self.username = username
        self.name = name
        self.email = email

    def introduce_yourself(self, guest_name):
        print("Hi {}, I'm {}! Contact me at {}.".format(
            guest_name, self.name, self.email))

    def __repr__(self):
        return "User({}, {}, {})".format(self.username, self.name, self.email)

    def __str__(self):
        return self.__repr__()


class UserDatabase:

    def __init__(self):
        self.users = []

    def insert(self, user):
        i = 0
        while i < len(self.users):
            # Find the first username greater than the new user's username
            if self.users[i].username > user.username:
                break
            i += 1
        self.users.insert(i, user)

    def find(self, username):
        for user in self.users:
            if user.username == username:
                return user

    def update(self, user):
        target = self.find(user.username)
        target.name, target.email = user.name, user.email

    def list_all(self):
        return self.users


if __name__ == "__main__":
    john = User("john", "John Doe", "john@doe.com")

    # john.introduce_yourself("David")
    # print(john)

    aakash = User('aakash', 'Aakash Rai', 'aakash@example.com')
    biraj = User('biraj', 'Biraj Das', 'biraj@example.com')
    hemanth = User('hemanth', 'Hemanth Jain', 'hemanth@example.com')
    jadhesh = User('jadhesh', 'Jadhesh Verma', 'jadhesh@example.com')
    siddhant = User('siddhant', 'Siddhant Sinha', 'siddhant@example.com')
    sonaksh = User('sonaksh', 'Sonaksh Kumar', 'sonaksh@example.com')
    vishal = User('vishal', 'Vishal Goel', 'vishal@example.com')

    users = [aakash, biraj, hemanth, jadhesh, siddhant, sonaksh, vishal]

    # print(users)

    database = UserDatabase()

    database.insert(hemanth)
    database.insert(aakash)
    database.insert(siddhant)

    database.update(User('siddhant', 'Siddhant U', 'siddhantu@example.com'))

    print(database.list_all())
