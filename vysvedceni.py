schoolReport = {
  "Český jazyk": 1,
  "Anglický jazyk": 1,
  "Matematika": 1,
  "Přírodopis": 2,
  "Dějepis": 1,
  "Fyzika": 2,
  "Hudební výchova": 4,
  "Výtvarná výchova": 2,
  "Tělesná výchova": 3,
  "Chemie": 4,
}

soucet_znamek = 0

for znamka in schoolReport.values():
  soucet_znamek += znamka
prumer = soucet_znamek/len(schoolReport)
print(f"Průměr Markových známek: {prumer}.")

for predmet, znamka in schoolReport.items():
  if znamka == 1:
    print(predmet)