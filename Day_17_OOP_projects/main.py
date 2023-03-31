import self as self


class User:
    # Constructor
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.follower = 0
        self.following = 0

    def follow(self, user):
        user.follower += 1
        self.following += 1


user_1 = User(123, "johnal")
user_2 = User(124, "angela")
print(user_1.id)
print(user_1.username)
user_1.follow(user_2)
print(user_1.follower)
print(user_1.following)
print(user_2.follower)
print(user_2.following)
