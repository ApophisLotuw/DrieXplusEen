def berekening(begingetal):

    try:
        if (begingetal % 2) > 0:
            begingetal = 3 * begingetal + 1
            print("ifblok = ", begingetal)

        elif begingetal == 1:
            begingetal = begingetal + 1
            print("elisblok = ", begingetal)

        else:
            begingetal = int(begingetal / 2)
            print("elseblok = ", begingetal)

        return (begingetal)

    except:
        print("ërror")


def main():
    begingetal = int(input())
    berekening(begingetal)
    print("Begingetal = ", begingetal)

if __name__ == "__main__":
    main()

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
