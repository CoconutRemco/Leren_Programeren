print("Welkom bij pizzacalculator!")
# Deze lijn geeft info
print("Voer het aantal pizza's per groote in.")
# Deze lijn geeft info
print("Hoeveel pizza's small wilt u?")
# Deze lijn stelt een vraag
try:
    small = int(input())
except:
    print("U Moet een getal invoeren")
# Deze lijn vraagt om een waarde

print("Hoeveel pizza's medium wilt u?")
# Deze lijn stelt een vraag
try:
    medium = int(input())
except:
    print("U Moet een getal invoeren")
# Deze lijn vraagt om een waarde

print("Hoeveel pizza's large wilt u?")
# Deze lijn stelt een vraag
try:
    large = int(input())
except:
    print("U Moet een getal invoeren")
# Deze lijn vraagt om een waarde
sprice = 3
mprice = 6
lprice = 10

print("Totaal prijs pizza's small")
# Deze lijn geeft info
try:
   print(small * sprice)
except:
    print("Er is iets foutgegaan")
# Deze lijn geeft een waarde

print("Totaal prijs pizza's medium")
# Deze lijn geeft info
try:
   print(medium * mprice)
except:
    print("Er is iets foutgegaan")
# Deze lijn geeft een waarde

print("Totaal prijs pizza's large")
# Deze lijn geeft info
try:
    print(large * lprice)
except:
    print("Er is iets foutgegaan")
# Deze lijn geeft een waarde

print("Totaal Bon:")
# Deze lijn geeft info

print("------------------------------")
try:
    print(small * sprice)
except:
    print("Er is iets foutgegaan")
# Deze lijn geeft een waarde
try:
   print(medium * mprice)
except:
    print("Er is iets foutgegaan")
# Deze lijn geeft een waarde
try:
   print(large * lprice)
except:
    print("Er is iets foutgegaan")
# Deze lijn geeft een waarde

print("Totaal Bedrag:")
# Deze lijn geeft info
try:
     print(small * sprice + medium * mprice + large * lprice)
except:
    print("Er is iets foutgegaan")
# Deze lijn geeft een waarde


print("------------------------------")

