
"""item = {"title": "Čajová konvička s hrnky", "price": 899, "inStock": True}
item["price"] = 929
print("Název položky je " + item["title"] +"." + "Jeho cena je " + str(item["price"]) + " Kč.")
print(f"Cena položky je {item['price']} Kč.")
item["weight"] = 0.5
if "weight" in item:
    print(f"Hmotnost je {item['weight']} kg.")
else:
    print(f"Hmotnost není zadána.")

sausages = {"jirka": 2, "Natálie": 1, "Bart": 4, "Martin": 3}
print(len(sausages))
sausages.pop("Martin")
print(len(sausages))

#vysvedceni
vysvedceni = {"Matematika": 3, "Český jazyk": 1, "Dějepis": 2}
print(vysvedceni)

#knihy
sales = {
    "Zkus mě chytit": 4165,
    "Vrah zavolá v deset": 5681,
    "Zločinný steh": 2565,
}

sales = {
    "Zkus mě chytit": 4165,
    "Vrah zavolá v deset": 5681,
    "Zločinný steh": 2565,
}

sales["Noc, která mě zabila"] = 0
sales["Vrah zavolá v deset"] +=100
print(sales)

#tombola
tombola = {
    7: "Láhev kvalitního vína Château Headache",
    15: "Pytel brambor z místního družstva",
    23: "Čokoládový dort",
    47: "Kniha o historii města",
    55: "Šiška salámu",
    67: "Vyhlídkový let balónem",
    79: "Moderní televizor",
    91: "Roční předplatné městského zpravodaje",
    93: "Společenská hra Sázky a dostihy",
}
cislo = int(input("Jaké je číslo tvého lístku? "))

if cislo in tombola:
  vyhra = tombola.pop(cislo)
  print(f"Vyhráváš: {vyhra}")
else:
  print("Bohužel jsi nevyhrál.")

#večírek
passwords = {
  "Jiří": "tajne-heslo",
  "Natálie": "jeste-tajnejsi-heslo",
  "Klára": "nejtajnejsi-heslo"
}

guest = input("Jaké je tvé jméno? ")

if guest in passwords:
  password = input("Jaké je tvoje heslo? ")
  if password == passwords[guest]:
    print("Smíš vstoupit.")
  else:
    if password == passwords[guest]:
      print("Smíš vstoupit.")
    else:
      print("Máš smůlu.")
else:
  print("Máš smůlu.")

#baliky
baliky = {
    "B541X": True,
    "B547X": False,
    "B251X": False,
    "B501X": True,
    "B947X": False,
}

balik = input("Jaké je číslo balíku? ")
if balik in baliky:
    if baliky[balik] == True:
        print("Balík byl předán kurýrovi.")
    else:
        print("Balík nebyl předán kurýrovi.")
else:
    print("Balík neexistuje.")

vstup = input("Zadej vstup: ")
for i in vstup:
    print(morseCode[i], end=" ")

#detektivky podruhé
prodeje2019 = {
    "Zkus mě chytit": 4165,
    "Vrah zavolá v deset": 5681,
    "Zločinný steh": 2565,
}

prodeje2020 = {
    "Zkus mě chytit": 3157,
    "Vrah zavolá v deset": 3541,
    "Vražda podle knihy": 2510,
    "Past": 2364,
    "Zločinný steh": 5412,
}

kniha = input("Zadej název knihy: ")
soucet = 0
if kniha in prodeje2019:
    soucet = soucet + prodeje2019[kniha]
soucet = soucet + prodeje2020[kniha]
print(f"Knih se prodalo {soucet} kusů.")

#cyklus

sales = {
    "Zkus mě chytit": 4165,
    "Vrah zavolá v deset": 5681,
    "Zločinný steh": 2565,
}
soucet = 0
for nazev, prodano in sales.items():
    print(f"Knihy {nazev} bylo prodáno {prodano} kusů.")
    soucet = soucet + prodano
print(f"Bylo prodáno {soucet} kusů knih.")



knihy = [
  {"nazev": "Zkus mě chytit", "prodano_kusu": 4165,"cena": 347, "rok_vydani": 2018},
  {"nazev": "Vrah zavolá v deset", "prodano_kusu": 5681,"cena": 299, "rok_vydani": 2019},
  {"nazev": "Zločinný steh", "prodano_kusu": 2565,"cena": 369, "rok_vydani": 2019},
]

celkove_trzby = 0

for kniha in knihy:
  if kniha["rok_vydani"] == 2019: celkove_trzby += kniha["prodano_kusu"] * kniha["cena"]
  print(f"Celkové tržby za rok 2019 jsou {celkove_trzby} Kč.")

"""

#morseovka
morseCode = {
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "!": "-.-.--",
    "-": "-....-",
    "/": "-..-.",
    "@": ".--.-.",
    "(": "-.--.",
    ")": "-.--.-"
}