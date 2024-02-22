from Post import Post


class SalePost(Post):

    def __init__(self, user, description, price, location):
        super().__init__(user, description)
        self.description = description  # content
        self.price = price  # define price
        self.location = location  # define location
        self.isSold = False  # flag for isSold or not

    def discount(self, percent, user_password):
        # Check if the provided password matches the correct password
        if not self.isSold and user_password == f"{self.user.get_password()}":
            # Apply discount logic
            discount_amount = self.price * percent / 100
            self.price -= discount_amount
            print(f"Discount on {self.user.username}'s product! The new price is: {self.price}")
            return True
        else:
            print("Discount failed: Invalid password or already sold.")
            return False

    def sold(self, password):
        if password == self.user.get_password():
            print(f"{self.user.get_username()}'s product is sold")
            self.isSold = True
        else:
            print("The product cant be sold: incorrect password")

    def __str__(self):
        if not self.isSold:
            return (
                f"{self.user.get_username()} posted a product for sale:\n  For sale! {self.description}, price: {self.price}, "
                f"pickup from: {self.location}\n")
        else:
            return (
                f"{self.user.get_username()} posted a product for sale:\n  Sold! {self.description}, price: {self.price}, "
                f"pickup from: {self.location}\n")
