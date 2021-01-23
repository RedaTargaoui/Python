import random
game_words=["rock","paper","scissors"]
computer=0
player=0
print("Score : Computer " +str(computer)+ " player " +str(player))
game=True
while game :
    computer_choice=random.choice(game_words)
    player_choice=input("Rock , paper or scissors ? press q to Quit !!")
    if player_choice==computer_choice :
        print("draw")
    elif player_choice=="rock" :
        if computer_choice=="scissors" :
            print("player win !!")
            player+=1
        else:
            print("computer win !!")
            computer+=1
    elif player_choice=="paper" :
        if computer_choice=="rock" :
            print("player win !!")
            player+=1
        else:
            print("computer win!!")
            computer+=1
    elif player_choice=="scissors" :
        if computer_choice=="paper" :
            print("player win !!")
            player+=1
        else:
            print("computer win !!")
            computer+=1
    elif player_choice=="q" :
        break
    else:
        print("invalid command !!")
    print("player :" + player_choice)
    print("computer : " + computer_choice)
    print("")
    print("Score : Computer " + str(computer) + " player " + str(player))
    print("")
