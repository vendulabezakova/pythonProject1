class Package:
    def getInfo(self):
        return f"Balík je na adresu {self.address}, váží {self.weightInKilos} kg, stav doručení je {self.delivered}. "

    def deliver(self):
        self.delivered = True

    def __init__(self, address, weightInKilos):
        self.address = address
        self.weightInKilos = weightInKilos
        self.delivered = False

class ValuablePackage(Package):
    def getInfo(self):
        text = super().getInfo()
        text = text + f"Hodnota balíku je {self.value} Kč."
        return text

    def __init__(self, address, weightInKilos, value):
        self.address = address
        self.weightInKilos = weightInKilos
        self.delivered = False
        self.value = value



balik = ValuablePackage("Václavské náměstí 67", 5, 399)
balik.deliver()
print(balik.getInfo())


