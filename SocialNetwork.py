from User import User


class SocialNetwork:
    _instance = None

    def __new__(cls, name):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, name):
        super().__init__()
        self.username = None
        self.name = name
        self.users = []

    def __str__(self):
        user_info = "\n".join(f"{user}" for user in self.users)
        return f"{self.name} social network:\n{user_info}"

    def sign_up(self, username, password):
        if len(password) <= 4 or len(password) >= 8:
            return None  # Return None if password length is invalid
        for user in self.users:
            if user.username == username:
                return None  # Return None if username already exists
        new_user = User(username, password)  # Instantiate a new User object
        self.users.append(new_user)  # Add the new user to the users list
        # self.add_follower(new_user)  # Add the new user as an observer
        User.logged_in = True

        return new_user  # Return the new User object upon successful signup

    def log_in(self, username, password):
        for user in self.users:
            if user.username == username and user.password == password:
                user.logged_in = True
                print(f"{username} connected")
                return True
        return False

    def log_out(self, username):
        for user in self.users:
            if user.username == username:
                user.logged_in = False
                print(f"{username} disconnected")
                return True
        return False


