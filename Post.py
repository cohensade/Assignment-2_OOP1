class Post:

    def __init__(self, user, content):
        self.user = user
        self.content = content

    def __str__(self):
        pass

    def get_username(self):
        return self.user.username

    def get_content(self):
        return self.content

    def comment(self, user, comment):
        if user.get_logged_in():  # Check if the user is logged in
            print(
                f"notification to {self.user.get_username()}: {user.get_username()} commented on your post: {comment}")
            self.user.update(f"{user.get_username()} commented on your post")
        else:
            print("None")

    def like(self, other_user):
        if other_user.get_logged_in():  # Check if the user is logged in
            if other_user.get_username() != self.user.get_username():
                print(f"notification to {self.user.get_username()}: {other_user.get_username()} liked your post")
                # print("to username from user1")
                self.user.update(f"{other_user.get_username()} liked your post")
        else:
            print("None")
