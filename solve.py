import moves as move


def findEdge(cube,x,y):
    for i in range(6):
        for j in range(3):
            for k in range(3):
                if cube[i][j][k] == x:
                    temp1 = []
                    temp1.append(i)
                    temp1.append(j)
                    temp1.append(k)
    
    for i in range(6):
        for j in range(3):
            for k in range(3):
                if cube[i][j][k] == y:
                    temp2 = []
                    temp2.append(i)
                    temp2.append(j)
                    temp2.append(k)
    
    return temp1,temp2
def whiteCross(cube):
    white_edges = [["W2","G8"],["W4","R8"],["W6","O8"],["W8","B8"]]
    white_cross_moves = []
    for edge in white_edges:
        i,j = findEdge(cube,edge[0],edge[1])
        if i[0] == 0:
            continue
        elif i[0] == 1:
            if i[1] == 1:
                if i[2] == 0:
                    while (cube[0][2][1][0] == "W"):
                        move.moves_dict["U"](cube)
                        white_cross_moves.append("U")
                    move.moves_dict["F"](cube)
                    white_cross_moves.append("F")
                elif i[2] == 2:
                    while (cube[0][2][1][0] == "W"):
                        move.moves_dict["U"](cube)
                        white_cross_moves.append("U")
                    move.moves_dict["R2"](cube)
                    white_cross_moves.append("R2")
                    move.moves_dict["F"](cube)
                    white_cross_moves.append("F")
            elif i[1] == 0:
                move.moves_dict["R'"](cube)
                white_cross_moves.append("R'")
                move.moves_dict["F"](cube)
                white_cross_moves.append("F")
                move.moves_dict["R"](cube)
                white_cross_moves.append("R")
            elif i[1] == 2:
                while (cube[0][2][1][0] == "W"):
                    move.moves_dict["U"](cube)
                    white_cross_moves.append("U")
                move.moves_dict["R"](cube)
                white_cross_moves.append("R")
                move.moves_dict["F"](cube)
                white_cross_moves.append("F")
                move.moves_dict["R'"](cube)
                white_cross_moves.append("R'")
        elif i[0] == 2:
            if i[1] == 1:
                if i[2] == 0:
                    while (cube[0][1][0][0] == "W"):
                        move.moves_dict["U"](cube)
                        white_cross_moves.append("U")
                    move.moves_dict["L'"](cube)
                    white_cross_moves.append("L'")
                elif i[2] == 2:
                    while (cube[0][1][0][0] == "W"):
                        move.moves_dict["U"](cube)
                        white_cross_moves.append("U")
                    move.moves_dict["F2"](cube)
                    white_cross_moves.append("F2")
                    move.moves_dict["L'"](cube)
                    white_cross_moves.append("L'")
            elif i[1] == 0:
                move.moves_dict["F'"](cube)
                white_cross_moves.append("F'")
                move.moves_dict["U"](cube)
                white_cross_moves.append("U")
                move.moves_dict["L'"](cube)
                white_cross_moves.append("L'")
            elif i[1] == 2:
                while (cube[0][1][0][0] == "W"):
                    move.moves_dict["U"](cube)
                    white_cross_moves.append("U")
                move.moves_dict["F"](cube)
                white_cross_moves.append("F")
                move.moves_dict["L'"](cube)
                white_cross_moves.append("L'")
                move.moves_dict["F'"](cube)
                white_cross_moves.append("F'")
                
                    
                    
                    
    print(white_cross_moves)
    return

def solveCube(cube,cube_solved):
    print("SoLve the white cross : ")
    
    whiteCross(cube)
    
    return