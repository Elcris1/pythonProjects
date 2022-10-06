#Import the necessary libraries
import random

#Create the loop for the whole game
while True: 

    #Basic prints for the game
    print("Benvingut al joc de adivinar el número")
    print("Que vols fer?")
    print("1.- Jugar (rang per defecte: 0 al 100")
    print("2.- Elegir el rang de valors")
    print("3.- Exit")

    #Reading the choice of the user
    selecio = input()

    #Change the action depending on the selection
    if selecio == "1" or selecio == "jugar":

        #Check if initial and Ending number exists
        if('numInici' not in vars() or 'numFi' not in vars()):
            #If they don't just create them
            numInici = 0
            numFi = 100
        
        #Generate random number ranging from initial number to ending 
        numeroRandom = random.randint(numInici, numFi)

        #Print some other random stuff for the game
        print("El numero d'inici seleccionat és " + str(numInici))
        print("El numero de fi seleccionat es "+ str(numFi))

        #Ask for the guessed number and then read it
        print("Numero aleatori creat, quina es la teva elecció?")
        numeroElegit = int(input())

        #Create a loop that works while the number is not found
        while(numeroElegit != numeroRandom):

            #If the guessed number is greater than the randomized one 
            if numeroRandom<numeroElegit:
                print("El num que has elegit és major al numero que ha sortit")
            else:
                print("El numero que has escollit es menor que el numero que ha sortit")

            #Ask for the next guessing if the user hasn't win
            print("Selecciona un altre nombre")
            numeroElegit = int(input())

        #When the user guesses the number the loop ends and shows some msg
        print("Has guanyat!!")
        print("El numero aleatori era el número " + str(numeroRandom) + " \n")

    elif selecio == "2" or selecio == "rang":

        #Prints and reads inputs for the initial and ending number changing
        print("Selecciona el número d'inici")
        numInici = int(input())
        print("Selecciona el numero de fi")
        numFi = int(input())

    elif selecio == "3" or selecio == "exit":

        #Ends the code if the selection is to exit
        break

    else:

        #If the user fails to chose an available option it messages them
        print("Selecciona un numero correcte: 1 al 3")
