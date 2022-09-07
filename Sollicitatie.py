print("Ja is 1 nee is 2")
nee = 2
print("Hoeveel jaar ervaring heeft u in de dierendressuur of jongleren of acrobatiek?")
vraag1 = input()

print("Bent u in het bezit van een mbo-4 ondernemen diploma?")

vraag2 = input()

print("Bent u in bezit van een geldig vrachtwagen rijbewijs?")

vraag3 = input()
print("Bent u in bezit van een hoge hoed?")

vraag4 = input()

print("Bent u een man of een vrouw? 1 man 2 vrouw")
manofvrouw = input()
if int(manofvrouw) < 2:
    print("Heeft u een snor van 10cm of langer?")
    snorlengte = input()
else:
    print("Heeft u rood gekrult haar van 20cm of langer?")
    roodhaar = input()



print("Hoe lang bent u?")

    
vraag6 = input()

    

print("Hoeveel weegt u?")
vraag7 = input()

    

print("Heeft u een certificaat overleven met gevaarlijk personeel?")
vraag8 = input()

print("Bent u capabel?")

    
vraag9 = input()

print("Rijd u vaak onder invloed?")

    
vraag10 = input()

print("Bent u op dit moment onder invloed?")

vraag11 = input()

if int(vraag1) > 3 and int(vraag2) < 2 and int(vraag3) < 2 and int(vraag4) < 2  and int(vraag6) > 150 and int(vraag7) > 90 and int(vraag8) < 2 and int(vraag9) <2 and int(vraag10) <2 and int(vraag11) <2 and int(snorlengte) > 10 and int(roodhaar) > 20:
    print("U bent aangenomen!")
else:
    print("Helaas u heeft het niet gehaald!")

