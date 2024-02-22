class Observer:
    def __init__(self, username):
        self.username = username
        self.notifications = []

    def update(self, notification):
        self.notifications.append(notification)

    def start_follow(self, user):
        user.add_follower(self)

    def stop_follow(self, user):
        user.remove_follower(self)

    def print_notifications(self):
        print(self.username + "'s notifications:")
        for notification in self.notifications:
            print(notification)
