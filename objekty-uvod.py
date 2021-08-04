class Zamestnanec:
  def vybrat_dovolenou(self, pocet_dni):
    if pocet_dni <= self.dny_dovolene:
      self.dny_dovolene=self.dny_dovolene - pocet_dni
      return "Užij si dovolenou."
    else:
      return "Už nemáš nárok na tolik dovolené."

  def vypis_informace(self):
    return f"Zaměstnanec se jmenuje {self.jmeno} a pracuje na pozici {self.pozice}. "

  def __init__(self, jmeno, pozice):
    self.jmeno = jmeno
    self.pozice = pozice
    self.dny_dovolene = 25

"""class Manager(Zamestnanec):
  def getInfo(self):
    text = super().__str__()
    text = text + f"Má {self.pocetPodrizenych} podřízených."
    return text

  def __init__(self, jmeno, pozice, pocetPodrizenych):
    super().__init__(jmeno, pozice)
    self.pocetPodrizenych = pocetPodrizenych
    self.jmeno = jmeno
    self.pozice = pozice
    self.dny_dovolene = 25
    self.pocetPodrizenych = pocetPodrizenych"""

class PartTimeEmpoyee(Zamestnanec):
  def __init__(self, jmeno, pozice, workload):
    super().__init__(jmeno, pozice)
    self.workload = workload

  def getInfo(self):
    text = super().vypis_informace()
    text = text + f"Má {self.workload}% úvazek."
    return text

  def __int__(self, jmeno, pozice, workload):
    super().__init__(jmeno, pozice)
    self.workload = workload




frantisek = Zamestnanec("František Giesl", "UX designér")
frantisek.jmeno = "František Giesl"
frantisek.pozice = "konstruktér"

klara = Zamestnanec("Klára Nová", "konstruktérka")
klara.jmeno = "Klára Nová"
klara.pozice = "konstruktérka"

"""simona = Manager("Simona Havlíková", "projektová manažerka", 5)
simona.jmeno = "Simona Havlíková"
simona.pozice = "projektová manažerka"
simona.pocetPodrizenych = 5"""

petr = PartTimeEmpoyee("Petr Havlík", "vědecký pracovník", 0.75)
petr.jmeno = "Petr Havlík"
petr.pozice = "vědecký pracovník"
petr.workload = 0.75

print(petr.getInfo())
