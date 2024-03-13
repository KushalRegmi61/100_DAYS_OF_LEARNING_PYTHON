class User:
    def __init__(self, id, username, salary ):
        self.id = id 
        self.username = username
        self.salary = salary
        self.workhour = 8
        self.follower = 0
        self.following = 0
    def follow(self, user):
        self.following += 1
        user.follower += 1
            
user_1 = User("42","kushal","4000")
user_2 = User("30 ","Nilam", "50000")
user_1.follow(user_2)
print("User_1",user_1.following, user_1.follower)
print("User_2",user_2.following, user_2.follower)