from ImagePost import ImagePost
from Observables import Observables
from Observer import Observer
from Observer import Observer
from SalePost import SalePost
from TextPost import TextPost


class User(Observables, Observer):
    def __init__(self, username, password):

        self.username = username
        Observables.__init__(self)  # followers
        Observer.__init__(self, username)  # notifications
        self.username = username
        self.password = password
        self.logged_in = True
        self.num_of_post = 0

    def __str__(self):
        return f"User name: {self.username},Number of posts: {self.num_of_post}, Number of followers: {len(self.followers)}"

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password

    def get_logged_in(self):

        return self.logged_in

    def follow(self, other_user):

        # Check if the user is trying to follow themselves
        if other_user == self.username:
            print("You can't follow yourself.")
            return
        # Check if the other user is logged in
        if other_user.logged_in:
            # Add the other user to the set of followed users
            self.start_follow(other_user)
            print(f"{self.username} started following {other_user.username}")
        else:
            print(f"{other_user.username} is not logged in. You can't follow them.")

    def unfollow(self, other_user):
        self.stop_follow(other_user)
        print(f"{self.username} unfollowing {other_user.username}")

    def publish_post(self, post_type, *post_args):
        if self.logged_in:
            self.num_of_post += 1
            self.notify(f"{self.username} has a new post")
            if post_type == "Text":
                if len(post_args) == 1:
                    print(f"{self.username} published a post:\n{post_args[0]}\n")
                    new_post = TextPost(self, post_args[0])
                    return new_post
                else:
                    print("Invalid arguments for Text post")
            elif post_type == "Image":
                if len(post_args) == 1:
                    print(f"{self.username} published a picture\n")
                    new_post = ImagePost(self, post_args[0])
                    return new_post
                else:
                    print("Invalid arguments for Image post")
            elif post_type == "Sale":
                if len(post_args) == 3:
                    print(
                        f"{self.username} posted a product for sale:\nFor sale! {post_args[0]}, price: {post_args[1]}, pickup from: {post_args[2]}\n")
                    new_post = SalePost(self, *post_args)
                    return new_post
                else:
                    print("Invalid arguments for Sale post")
            else:
                print("Invalid post type")
        else:
            print("You need to be logged in to publish a post.")
            return None
