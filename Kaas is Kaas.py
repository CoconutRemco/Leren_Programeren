print("Is de kaas geel?")
print("ja is 1 nee is 2")
kaas = int(input())
nee = int(2)
if int(nee) > int(kaas):
   print("Zitten er gaten in?")
   gaten = int(input())
   if int(nee) > int(gaten):
      print("Is de kaas belachelijk duur?")
      duur = int(input())
      if int(nee) > int(duur):
        print("De kaas is Emmenthaler")
      else:
        print("De kaas is leerdammer")
   else:
        print("Is de kaas hard als een steen?")
        steen = int(input())
        if int(nee) > int(steen):
            print("De kaas is parmigiano reggiano")
        else:
            print("De kaas is goudse kaas")



else:
    print("Heeft de kaas blauwe schimmel?")
schimmel = int(input())
if int(nee) > int(schimmel):
    print("Heeft de kaas een korst?")
    korst2 = int(input())
    if nee > korst2:
        print("De kaas is Blue de rochbaron")
    else:
        print("De kaas is Foume d'Ambert")
else:
    print("Heeft de kaas een korst?")
korst = int(input())
if nee > korst:
    print("De kaas is camembert")
else:
    print("De kaas is mozzarella")



