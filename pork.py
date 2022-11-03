def porkgame():
    punten=0
    print("Official Copyrighted by PorkEnterprises. Dont you dare to copy!")
    
    print("This is an story based game about pigs")
    print("Press enter to go to next sentence!")

    input("There is a crowd of pigs on the other side of the ocean!")
    input("Do you want to go there by boat or by helicopter?")
    input("Press 1 for boat Press 2 for helicopter")
    Task1 = input()
    if Task1 == '1' :
        input("Oke cool now get to the shore to find wood and build an boat!")
        input("Oke we are at the shore now and we are lucky there is already an boat there!")
        input("Good job finding the boat we made it to the shore undamaged")
        input("Now whe are here and we see the pigs what do you wanna do?")
        input("Press 1 to slaughter the pigs and eat them tonight. Press 2 to save them and bread more.")
        punten+=1
        Task3 = input()
        if Task3 == '1':
            input("Well hey boy now you have to slaughter them 1 by 1 without getting them mad!")
            input("Well hey you fucked up they are mad as fuck now you have to escape!")
            input("Press 1 to run Press 2 to steal the scooter at the waterside")
            Task4 = input()
            if Task4 == "1":
                input("Fuck wrong decission your crushed to die")
                vraag1 = input("You received an golden carrot you can revive yourself press 1 to revive press 2 for game over")
                if vraag1 == "1":
                    print("You won the game by finding the golden carrot!")
                    punten+=10
            else:
                input("Shit dog there's no fuel in it but you found an underground bunker")
                input("You see that it leads to an underground carrots storage")
                input("You must be verry happy now you can bread the pigs and sell them to your uncle Sam")
                input("press 1 to take carrots and breed press 2 to eat all the carrots")
                punten+=1
                task6 = input()
                if task6 == '1':
                    input("Wow verry good choise")
                    input("Now you get out the bunker and get back to the pigs you are happy they aren't mad anymore bud!")
                    input("You feed the pigs and they breed")
                    input("When they are big you sell half of them to uncle Sam")
                    print("Now you are able to build a big big pig farm and live happily!")
                    print("You won the game! Fantastic!")
                    punten+=2
                else:
                    input("Well fuck mate what did you think you were gonna receive with this?")
                    input("Game over idiot!")
                    punten=0
                
        else:
            input("Hey good choise go get some carrots to breed!")
            input("Do you wanna buy carrots at the farm or get them for free at the river?")
            input("Press 1 to buy Press 2 to get for free")
            Task5 = input()
            if Task5 == '1':
                input("Well good choise these are way better qaulity")
                input("You did an really good job now you breeded them and they are so big already!")
                input("You have reached the end of the game well done!")
                punten+=3
            else:
                input("These carrots are so bad qaulity that you can't use them you'r yourney is over!")
                input("Game over")
        
    elif Task1 == '2' :
        input("Wow nice choice now we have to steal one from uncle Brooke!")
        input("Oke we just arrived at uncle Brooke he seems to have a couple of helicopters we only need a 2 seater!")
        input("Press 1 to steal press 2 to pay rent!")
        Task2 = input()
        if Task2 == '1':
            input("Oh shit boy hes hella mad we have to make it up to him later!")
            punten-2
        else:
            input("Its gonna cost some money but atleast he isn't mad!")
        input("Ooh fuck man you crashed the helicopter in the water we will drown now")
        input("We have an chance to swim out off the river")
        vraag2 = input("Press 1 to use al energy press 2 to swim without using all your energy!")
        if vraag2 == "2":
            input("You stupid idiot ofcourse you didn't make it")
            punten=0
        else:
            input("Wel unfortunaly you made it but there are no pigs here!")
            input("Game over!")
            punten-2
    else:
        input("Hey you didn't anwser 1 or 2 try again!")
    print("Uw punten zijn! " + punten)
porkgame()
nognkeer=input("Nog een keer spelen?")
if nognkeer == "ja":
    porkgame()       

        


    

