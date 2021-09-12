def main():
    getal = int(input())
    ronde = 1

    while (getal > 1):
        if (getal == 1):
            print("Rondes gebruikt: ", ronde)
            exit()
        elif (int(getal % 2)) > 0:
            x = int(oneven(getal))
            print("Oneven:", x, " Ronde: ", ronde)
            ronde = ronde + 1
            getal = x
        else:
            x = int(even(getal))
            print("Even:", x, " Ronde: ", ronde)
            ronde = ronde + 1
            getal = x
    else:
        print("Klaar")


def even(getal2):
    getal2 = int(getal2 / 2)
    return getal2

def oneven(getal2):
    getal2 = 3 * getal2 + 1
    return getal2

if __name__ == "__main__":
    main()