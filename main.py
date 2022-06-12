import random

print("Rock -- Paper -- Scissor Game")

"""Vairables to note
'R' for 'rock'
'P' for 'paper'
'S' for 'scissor' """

player_Score = 0
cpu_Score = 0
tie_Score = 0
options = ['R for rock', 'P for paper', 'S for scisssor']

# Create fuctions
def checkFor_Winner(playerhand, cpuhand):
    if (playerhand == 'R' and cpuhand == 'P'):
        print("Oops, sorry you lost !!!")
        return "Cpu"
    elif(playerhand == 'R' and cpuhand == 'S'):
        print("Rock ruin the scissor...Yea You Win!!!")
        return "Player"
    elif(playerhand == 'P' and cpuhand == 'R'):
        print("Paper covered rock, congrats You Win!!!")
        return "Player"   
    elif(playerhand == 'P' and cpuhand == 'S'):
        print("oh no!! You lost")
        return "Cpu"
    elif(playerhand == 'S' and cpuhand == 'R'):
        print("Damn!! You lost")
        return  "Cpu"
    elif(playerhand == 'S' and cpuhand == 'P'):
        print('wow.. Congrats You Win')
        return "Player" 
    else:
        print("It's a tie!!!")    

#  Creating a loop that will control "playerhand" & "cpuhand"
while(player_Score != 3 and cpu_Score != 3):
    # introducing the while loop
    while True:
        playerhand = input(f'\nMake a choice {options}:  ')
        playerhand = playerhand.upper()
        if(playerhand == 'R' or playerhand =='P' or playerhand == 'S'):
            break
        else:
            print("Invalid input, Try again.")

    cpuhand = random.choice(['r','p','s'])
    cpuhand = cpuhand.upper()
    

    print("Your hand: ",playerhand)
    print("Cpu hand: ",cpuhand)
    result = checkFor_Winner(playerhand, cpuhand)
    if(result == "Player"):
        player_Score += 1
    elif(result == "Cpu"):
        cpu_Score += 1
    else:
        tie_Score += 1
   
    print("Your score: ", player_Score, "CPU: ",cpu_Score, "Ties: ",tie_Score)

    print()

    
print("Game Over!!!...hope you enjoyed the game.")            










