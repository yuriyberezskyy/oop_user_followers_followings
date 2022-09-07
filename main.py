class User:
    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

    def print_info(self):
        print(f"Print info:\n User_id: {self.user_id}\n Username: {self.username}\n Followers: "
              f"{self.followers}\n Following: {self.following}")

user1 = User("001", "sarah")
user2 = User("002", "angelo")


user1.follow(user2)
user1.print_info()
user2.print_info()