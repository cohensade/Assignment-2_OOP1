

from Post import Post


class TextPost(Post):
    def __init__(self, user, content):
        super().__init__(user,content)
        self.content = content

    def __str__(self):
        return f"{self.user.username} published a post:\n {self.content}\n"

