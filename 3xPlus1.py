import keyboard

def even(getal2):
    getal2 = int(getal2 / 2)
    return getal2


def oneven(getal2):
    getal2 = 3 * getal2 + 1
    return getal2


while True:
    try:
        getal = 10
        ronde = 1

        while getal > 1:
            if ((getal % 2)) > 0:
                x = int(oneven(getal))
                print("Oneven:", x, " Ronde: ", ronde)
                ronde = ronde + 1
                getal = x
            else:
                x = int(even(getal))
                print("Even:", x, " Ronde: ", ronde)
                ronde = ronde + 1
                getal = x
        if keyboard.is_pressed('q'):
            break
    except:
        break



#def main():
#    getal = int(input())
#    ronde = 1

#    while getal > 1:
#        if ((getal % 2)) > 0:
#            x = int(oneven(getal))
#            print("Oneven:", x, " Ronde: ", ronde)
#            ronde = ronde + 1
#            getal = x
#        else:
#            x = int(even(getal))
#            print("Even:", x, " Ronde: ", ronde)
#            ronde = ronde + 1
#            getal = x
#    else:
#        ronde = ronde - 1
#        print("Rondes gebruikt: ", ronde)


#def even(getal2):
#    getal2 = int(getal2 / 2)
#    return getal2


#def oneven(getal2):
#    getal2 = 3 * getal2 + 1
#    return getal2


#if __name__ == "__main__":
#    main()
