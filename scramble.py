import random

def scrambler():
    moves_list = [
        "U","U2","U'","D","D2","D'",  
        "R","R2","R'","L","L2","L'",  
        "F","F2","F'","B","B2","B'",
    ]
    
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
    
    return scramble_list