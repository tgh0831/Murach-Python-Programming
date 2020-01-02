class Product:
    def __init__(self, name="", price=0.0, discountPercent=0):
            self.name = name
            self.price = price
            self.discountPercent = discountPercent

    def getDiscountAmount(self):
        return self.price * self.discountPercent / 100

    def getDiscountPrice(self):
        return self.price - self.getDiscountAmount()

    def getDescription(self):
        return self.name
    
class Media(Product):
    def __init__(self, name="", price=0.0, discountPercent=0, format=""):
        Product.__init__(self, name, price, discountPercent)
        self.format = format

    def getDescription(self):
        return Product.getDescription(self) + " - " + self.format

class Book(Media):
    def __init__(self, name="", price=0.0, discountPercent=0, author="", format=""):
        Media.__init__(self, name, price, discountPercent, format)
        self.author = author

    def getDescription(self):
        return Product.getDescription(self) + " by " + self.author
                
class Movie(Media):
    def __init__(self, name="", price=0.0, discountPercent=0, year=0, format=""):
        Media.__init__(self, name, price, discountPercent, format)
        self.year = year

    def getDescription(self):
        return Product.getDescription(self) + " (" + str(self.year) + ")"

class Album(Media):
    def __init__(self, name="", price=0.0, discountPercent=0, artist="", format=""):
        Media.__init__(self, name, price, discountPercent, format)
        self.artist = artist
        self.format = format

    def getDescription(self):
        return Product.getDescription(self) + " by " + self.artist                
