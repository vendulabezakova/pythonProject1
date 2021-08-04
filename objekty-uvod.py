class Zamestnanec:
  def vybrat_dovolenou(self, pocet_dni):
    if pocet_dni <= self.dny_dovolene:
      self.dny_dovolene=self.dny_dovolene - pocet_dni
      return "Užij si dovolenou."
    else:
      return "Už nemáš nárok na tolik dovolené."
  def vypis_informace(self):
    return f"Zaměstnanec se jmenuje {self.jmeno} a pracuje na pozici {self.pozice}."
  def __init__(self, jmeno, pozice):
    self.jmeno = jmeno
    self.pozice = pozice
    self.dny_dovolene = 25


frantisek = Zamestnanec("František Giesl", "UX designér")
frantisek.jmeno = "František Giesl"
frantisek.pozice = "konstruktér"

klara = Zamestnanec("Klára Nová", "konstruktérka")
klara.jmeno = "Klára Nová"
klara.pozice = "konstruktérka"

simona = Zamestnanec("Simona Havlíková", "projektová manažerka")
simona.jmeno = "Simona Havlíková"
simona.pozice = "projektová manažerka"

print(frantisek.vypis_informace())
print(klara.vypis_informace())
print(simona.vypis_informace())
print(frantisek.vybrat_dovolenou(20))
print(frantisek.vybrat_dovolenou(10))
