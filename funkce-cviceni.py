# nasobeni
def mult(a, b):
  return a*b

a = int(input("Zadej číslo: "))
b = int(input("Zadej číslo: "))

print(f"Násobek je {mult(a, b)}.")


# hotel
def totalPrice(persons, breakfast=False):
    return persons * (850+125 * breakfast)
print(totalPrice(1))
print(totalPrice(4,True))
