class Book:
    def getInfo(self):
        return f"Kniha {self.title} má {self.pages}, stojí {self.price} a cena po slevě je {self.discount}."

    def __init__(self, title, pages, price):
        self.title = title
        self.pages = pages
        self.price = price
# dodelat vypocet slevy
    def discount(self, discount):
        self.price = self.price * (1 - discount / 100)

kniha1 = Book("Zdroj", 549, 399)
kniha1.title = "Zdroj"
kniha1.pages = 549
kniha1.price = 399
# dodelat vypocet slevy
# kniha1.discount(10)

kniha2 = Book("Atlasova vzpoura", 849, 589)
kniha2.title = "Atlasova  vzpoura"
kniha2.pages = 849
kniha2.price = 589

print(kniha1.getInfo())
print(kniha2.getInfo())