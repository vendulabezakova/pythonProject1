import math

def overCislo(cislo):
    if cislo[0] == "+":
        if len(cislo) == 13:
            return True
        else:
            return False
    else:
        if len(cislo) == 9:
            return True
        else:
            return False
def cenaZpravy (zprava):
    return math.ceil(zprava) // 180) *3
cislo = input("Zadej telefonní číslo: ")
    if telefonniCislo
zprava = input("Text zprávy: ")
cenaZpravy()