import random

numeroRandom = random.randint(0, 100)
while True: 
    print("Benvingut al joc de adivinar el número")
    print("Que vols fer?")
    print("1.- Jugar (rang per defecte: 0 al 100")
    print("2.- Elegir el rang de valors")
    print("3.- Exit")
    selecio = input()
    if selecio == "1" or selecio == "jugar":
        if('numInici' not in vars() or 'numFi' not in vars()):
            numInici = 0
            numFi = 100
        numeroRandom = random.randint(numInici, numFi)
        print("El numero d'inici seleccionat és " + str(numInici))
        print("El numero de fi seleccionat es "+ str(numFi))
        print("Numero aleatori creat, quina es la teva elecció?")
        numeroElegit = int(input())
        while(numeroElegit != numeroRandom):
            if numeroRandom<numeroElegit:
                print("El num que has elegit és major al numero que ha sortit")
            else:
                print("El numero que has escollit es menor que el numero que ha sortit")
            print("Selecciona un altre nombre")
            numeroElegit = int(input())
        print("Has guanyat!!")
        print("El numero aleatori era el número " + str(numeroRandom))

    elif selecio == "2" or selecio == "rang":
        print("Selecciona el número d'inici")
        numInici = int(input())
        print("Selecciona el numero de fi")
        numFi = int(input())
    elif selecio == "3" or selecio == "exit":
        break
    else:
        print("Selecciona un numero correcte: 1 al 3")
