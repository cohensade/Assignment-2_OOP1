import matplotlib.pyplot as plt
from matplotlib import image
from Post import Post


class ImagePost(Post):
    def __init__(self, user, image_path):
        super().__init__(user, image_path)
        self.image_path = image_path

    def __str__(self):
        return f"{self.user.username} posted a picture\n"

    def display(self):
        plt.show()
        print("Shows picture")
