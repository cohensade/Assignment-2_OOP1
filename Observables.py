class Observables:
    def __init__(self):
        self.followers = []

    def add_follower(self, follower):
        if follower not in self.followers:
            self.followers.append(follower)
            return True
        return False

    def remove_follower(self, follower):
        if follower in self.followers:
            self.followers.remove(follower)
            return True
        return False

    def notify(self, notification):
        for follower in self.followers:
            follower.update(notification)
