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

class Driver:
    def priradBalik(self, balik):
        if balik.delivered == True:
            print("Balík již byl doručen.")
        else:
            self.packageList.append(balik)
        self.packageList.append(balik)

    def zbyvaBaliku(self,zbyvaBaliku):
        zbyvaBaliku = 0
        for polozka in self.packageList:
            if polozka.delivered == False:
                pocetBaliku = pocetBaliku + 1
            return pocetBaliku

    def __init__(self, name):
        self.name = name
        self.packageList = []

balik = ValuablePackage("Václavské náměstí 67", 5, 399)
balik.deliver()
print(balik.getInfo())
ridic = Driver("Jirka")
ridic.priradBalik
