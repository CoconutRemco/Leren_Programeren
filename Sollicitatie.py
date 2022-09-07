print("Ja is 1 nee is 2")
nee = 2
print("Hoeveel jaar ervaring heeft u in de dierendressuur of jongleren of acrobatiek?")
vraag1 = input()
if int(vraag1) > int(3):
    print("Bent u in het bezit van een mbo-4 ondernemen diploma?")
else:
    print("Helaas u valt af")
vraag2 = input()
if nee > int(vraag2):
    print("Bent u in bezit van een geldig vrachtwagen rijbewijs?")
else:
    print("Helaas valt u af.")
vraag3 = input()
if nee > int(vraag3):
    print("Bent u in bezit van een hoge hoed?")
else:
    print("Helaas valt u af.")
vraag4 = input()
if nee > int(vraag4):
    print("Bent u een man met snor langer dan 10cm of vrouw met rood krulhaar van langer dan 20 cm?")
else:
    print("Helaas valt u af.")
vraag5 = input()
if nee > int(vraag5):
    print("Hoe lang bent u?")
else:
    print("Helaas valt u af.")
vraag6 = input()
if int(150) > int(vraag6):
    print("Helaas valt u af.")
else:
    print("Hoeveel weegt u?")
vraag7 = input()
if int(90) > int(vraag7):
    print("Helaas u valt af.")
else:
    print("Heeft u een certificaat overleven met gevaarlijk personeel?")
vraag8 = input()
if nee > int(vraag8):
    print("Bent u capabel?")
else:
    print("U heeft het helaas niet behaald.")
vraag9 = input()
if nee > int(vraag9):
    print("Rijd u vaak onder invloed?")
else:
    print("Helaas u heeft het niet gehaald.")
vraag10 = input()
if nee > int(vraag10):
    print("Bent u op dit moment onder invloed?")
else:
    print("Helaas u heeft het niet gehaald.")
vraag11 = input()
if nee > int(vraag11):
    print("U heeft de test behaald gefeliciteerd!")
else:
    print("Helaas u heeft door de laatse vraag de test niet behaald.")

