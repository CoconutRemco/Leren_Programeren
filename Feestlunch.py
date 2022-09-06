print("Kosten Croissantje?")
a = input()
print("Aantal Croissantjes?")
b = input()
print("Prijs Stokbroodje?")
c = input()
print("Aantal Stokbroodjes?")
d = input()
print("Totaal kortingsbonnen x0.50")
e = input()
totaal_bedrag_is = float(a)*float(b)+float(c)*float(d)-float(e)

print("Croissantjes Zijn")
# Deze regel geeft informatie
print(float(a)*float(b))
# Deze regel geeft een waarde
print("Stokbroden Zijn")
# Deze regel geeft informatie
print(float(c) * float(d))
# Deze regel geeft een waarde
print("Korting Is")
# Deze regel geeft informatie
print(e)
# Deze regel geeft een waarde
print("Totaal Bedrag Is")
# Deze regel geeft informatie
print(totaal_bedrag_is)
# Deze regel geeft een waarde

print("De feestlunch kost je bij de bakker  " +str(totaal_bedrag_is)+ "  Dit is erg voordelig")
