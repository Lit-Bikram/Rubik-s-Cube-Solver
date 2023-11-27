import random

def scrambler(moves_list):
    scramble_list = []
    same_move_counter = 0
    opp_move_counter = 0
    while (len(scramble_list) != 20):
        x = random.randint(0,len(moves_list) - 1)
        temp = x//3
        temp2 = x//6
        if (same_move_counter != temp) or (opp_move_counter != temp2):
            same_move_counter = x//3
            opp_move_counter = x//6
            scramble_list.append(moves_list[x])
    
    return " ".join(scramble_list)