def main():
    getal = int(input())
    ronde = 1

    if (getal == 1):
        print("Rondes gebruikt: ". ronde)
        exit()
    elif (getal % 2) > 0:
        x = oneven(getal)
        print("Oneven:", x, " Ronde: ", ronde)
        ronde = ronde + 1
        return(x)
    else:
        x = even(getal)
        print("Even:", x, " Ronde: ", ronde)
        ronde = ronde + 1
        return(x)


def even(getal2):
    getal2 = int(getal2 / 2)
    return getal2

def oneven(getal2):
    getal2 = 3 * getal2 + 1
    return getal2

if __name__ == "__main__":
    main()