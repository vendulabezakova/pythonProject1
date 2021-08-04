def pozdrav_uzivatele(osloveni1, osloveni2):
    print(f"Ahoj, {osloveni1}")


def secti_dve_cisla(a, b):
    return a + b


vysledek_volani_funkce = secti_dve_cisla(2, 3)
print(vysledek_volani_funkce)


# známka
def zjisti_znamku(points, bonus=0):
    if points <= 60:
        mark = 5
    elif points <= 70:
        mark = 4
    elif points <= 80:
        mark = 3
    elif points <= 90:
        mark = 2
    else:
        mark = 1
    return mark


pocet_bodu = int(input("Zadej počet bodů: "))
pocet_bonusovych_bodu = int(input("Zadej počet bonusových bodů: "))
znamka = zjisti_znamku(pocet_bodu, pocet_bonusovych_bodu)
if znamka == 5:
    body_z_opravneho_pokusu = int(input("Počet bodů z opravného pokusu: "))
    znamka_z_opravneho_pokusu = zjisti_znamku(body_z_opravneho_pokusu)
print(f"Výsledná známka je {znamka}", )
