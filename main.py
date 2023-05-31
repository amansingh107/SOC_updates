def tictac(xstate,ostate):
    zero='X'if xstate[0] else('o' if ostate[0] else 0)
    first='X'if xstate[1] else('o' if ostate[1] else 1)
    second='X'if xstate[2] else('o' if ostate[2] else 2)
    third='X'if xstate[3] else('o' if ostate[3] else 3)
    forth='X'if xstate[4] else('o' if ostate[4] else 4)
    fifth='X'if xstate[5] else('o' if ostate[5] else 5)    
    sixth='X'if xstate[6] else('o' if ostate[6] else 6)
    seventh='X'if xstate[7] else('o' if ostate[7] else 7)
    eight='X'if xstate[8] else('o' if ostate[8] else 8)

    print(f"{zero} | {first} | {second}")
    print("--|--|--")
    print(f"{third} | {forth} | {fifth}")
    print("--|--|--")
    print(f"{sixth} | {seventh} | {eight}")
    
def checkwin(xstate,ostate):
    winpoint=[[0,3,6],[1,4,7],[2,5,8],[0,1,2],[3,4,5],[6,7,8],[0,4,8],[2,4,6]]
    for win in winpoint:
        if(xstate[win[0]]+xstate[win[1]]+xstate[win[2]]==3):
            print("x wins")
            return 1

        if(ostate[win[0]]+ostate[win[1]]+ostate[win[2]]==3):
            print("o wins")
            return 0
    return -1


if __name__=="__main__":
    xstate=[0,0,0,0,0,0,0,0,0]
    ostate=[0,0,0,0,0,0,0,0,0]
    turn=1
    cont=0
    while(True):
        tictac(xstate,ostate)
        if(turn==1):#1for x and 0 for 0
            print("chance for x")
            value=int(input("Enter where you want to put using no.: "))
            xstate[value]=1
        else:
            print("chance for o")
            value=int(input("Enter where you want to put using no.: "))
            ostate[value]=1
        cont=cont + 1
        win=checkwin(xstate,ostate)
        if(win!=-1):
            print("Match is over")
            break
        if(cont==9):
            print("Match Tied")
            break
        turn=1-turn

