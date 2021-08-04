class Auto:
    def getInfo(self):
        return f"{self.znackaATyp}, {self.regZnacka}, najeto {self.pocetKm}."
    def vratAuto(self, pocetDni, stavTachometru):
        self.pocetKm = stavTachometru
        self.volne = True
            if pocetDni < 7:
                return pocetDni * 400
            else:
                return pocetDni * 300
    def pujcAuto(self):
        if self.volne == True:
            self.volne = False
            return f"Potvrzuji půjčení auta."
        else:
            return f"Auto není k dispozici."

    def __init__(self, regZnacka, znackaATyp, pocetKm):
        self.regZnacka = regZnacka
        self.znackaATyp = znackaATyp
        self.pocetKm = pocetKm
        self.volne = True

auto1 = Auto("4A6 HJG", "Peuget 407", 1764)
auto1.pujcAuto()
auto2 = Auto("8B6 HFD", "Fiat Tempra", 2643)
pozadovaneAuto = input("Zadej typ auta (Peugeot / Fiat: " )
if pozadovaneAuto == "Peugeot":
    print(auto1.getInfo())
    print(auto1.pujcAuto())
else:
    print(auto2.getInfo())
    print(auto2.getInfo())
