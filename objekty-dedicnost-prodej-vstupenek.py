from datetime import datetime, timedelta

apolloStart = datetime(1969, 7, 16, 14, 32)
otevreniKina = datetime(2021, 7, 1)
pozadovanyDenNavstevyKina_str = input("Zadej datum návštěvy (den. měsíc. rok): ")
pozadovanyDenNavstevyKina = datetime.strptime(pozadovanyDenNavstevyKina_str, "%d. %m. %Y")
zacatekLevnejsiSezony = datetime(2021, 8, 11)
uzavreniKina = datetime(2021, 9, 1)
pozadovanyPocetListku = int(input("Zadej počet lístků: "))

if pozadovanyDenNavstevyKina < otevreniKina:
  print("Kino je zavřeno.")
elif pozadovanyDenNavstevyKina < zacatekLevnejsiSezony:
  cenaZaVstupenku = 250
  print(f"Cena za vstupenky je {cenaZaVstupenku * pozadovanyPocetListku }.")
elif pozadovanyDenNavstevyKina < uzavreniKina:
  cenaZaVstupenku = 180
  print(f"Cena za vstupenky je {cenaZaVstupenku * pozadovanyPocetListku }.")
else:
  print("Kino je uzavřeno.")