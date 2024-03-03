# 1 = The Jab
# 2 = The Cross
# 3 = The Lead Hook
# 4 = The Rear Hook
# 5 = The Lead Uppercut
# 6 = The Rear Uppercut

# higher number always more powerful with one exception move num 1 beats move num 6.
# extra: knock out(random)/health

import random

isChampionship = input("is this a regular fight or a championship ? \n press 0 for regular and 1 for championship : ")

def helper(u_move, my_move):
    if (u_move == 6 and my_move == 1) or u_move < my_move:
        print("you lose")
        return 0
    elif u_move > my_move:
        print("you win")
        return 2
    else:
        print("draw")
        return 1


if isChampionship == "0":
    print("this fight is only 1 round with 1 move, may the stronger win!!")
    u_move = int(input("select your move (1-6) : "))
    my_move = random.randint(1, 4)
    # print(my_move)
    helper(u_move, my_move)

else:
    print("this is a championship, the best out of 3 rounds wins ")
    u_score = 0
    for i in range(3):
        u_move = int(input("select your move (1-6) : "))
        my_move = random.randint(1, 4)
        u_score += helper(u_move, my_move)
    if u_score >= 3:
        print("you are the CHAMPIOOON !!!")
