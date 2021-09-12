def main():
    getal = int(input())
    ronde = 1

    if (getal % 2) > 0:
        oneven(getal)
        ronde = ronde + 1
        print("Oneven:", getal, " Ronde: ", ronde)
    else:
        even(getal)
        ronde = ronde + 1
        print("Even:", getal, " Ronde: ", ronde)

def even(getal2):
    getal2 = int(getal2 / 2)

def oneven(getal2):
    getal2 = 3 * getal2 + 1

if __name__ == "__main__":
    main()


#def berekening(begingetal):
#    try:
#        if (begingetal % 2) > 0:
#            begingetal = 3 * begingetal + 1
#            print("ifblok = ", begingetal)
#
#        elif begingetal == 1:
#            begingetal = begingetal + 1
#            print("elisblok = ", begingetal)
#
#        else:
#            begingetal = int(begingetal / 2)
#            print("elseblok = ", begingetal)
#
#        return (begingetal)
#
#    except:
#        print("ërror")
# from sys import exit
# def collatz(number, round):
#    if number == 1:
#        return 1
#    elif (number % 2) > 0:
#        result = 3 * number + 1
#    else:
#        result = int(number / 2)
#    print("Ronde: {}, oude getal: {}, nieuwe getal: {}".format(round, number, result))
#    return (result, round+1)
#    getal = 1
#    start = 1
#    try:
#        collatz(getal, start)
#    try:
#        getal = int(input("Vul begin-getal in: "))
#    except ValueError:
#        print("Oeps, graag een positief heel getal boven 0 invullen.")
#        exit(1)
#    while getal != 1:
#        (getal, start) = collatz(getal, start)
