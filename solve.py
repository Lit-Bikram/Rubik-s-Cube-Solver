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
    white_daisy_moves = []
    for edge in white_edges:
        i,j = findEdge(cube,edge[0],edge[1])
        print(i,j)
        if i[0] == 0:
            continue
        elif i[0] == 1:
            if i[1] == 1:
                if i[2] == 0:
                    while (cube[0][2][1][0] == "W"):
                        move.moves_dict["U"](cube)
                        white_daisy_moves.append("U")
                    move.moves_dict["F'"](cube)
                    white_daisy_moves.append("F'")
                elif i[2] == 2:
                    while (cube[0][0][1][0] == "W"):
                        move.moves_dict["U"](cube)
                        white_daisy_moves.append("U")
                    move.moves_dict["B"](cube)
                    white_daisy_moves.append("B")
            elif i[1] == 0:
                move.moves_dict["R'"](cube)
                white_daisy_moves.append("R'")
                while (cube[0][2][1][0] == "W"):
                    move.moves_dict["U"](cube)
                    white_daisy_moves.append("U")
                move.moves_dict["F'"](cube)
                white_daisy_moves.append("F'")
            elif i[1] == 2:
                while (cube[0][2][1][0] == "W"):
                    move.moves_dict["U"](cube)
                    white_daisy_moves.append("U")
                move.moves_dict["R"](cube)
                white_daisy_moves.append("R")
                move.moves_dict["F'"](cube)
                white_daisy_moves.append("F'")
                move.moves_dict["R'"](cube)
                white_daisy_moves.append("R'")
        elif i[0] == 2:
            if i[1] == 1:
                if i[2] == 0:
                    while (cube[0][1][0][0] == "W"):
                        move.moves_dict["U"](cube)
                        white_daisy_moves.append("U")
                    move.moves_dict["L'"](cube)
                    white_daisy_moves.append("L'")
                elif i[2] == 2:
                    while (cube[0][1][2][0] == "W"):
                        move.moves_dict["U"](cube)
                        white_daisy_moves.append("U")
                    move.moves_dict["R"](cube)
                    white_daisy_moves.append("R")
            elif i[1] == 0:
                move.moves_dict["F'"](cube)
                white_daisy_moves.append("F'")
                while (cube[0][1][0][0] == "W"):
                    move.moves_dict["U"](cube)
                    white_daisy_moves.append("U")
                move.moves_dict["L'"](cube)
                white_daisy_moves.append("L'")
            elif i[1] == 2:
                while (cube[0][1][0][0] == "W"):
                    move.moves_dict["U"](cube)
                    white_daisy_moves.append("U")
                move.moves_dict["F"](cube)
                white_daisy_moves.append("F")
                move.moves_dict["L'"](cube)
                white_daisy_moves.append("L'")
                move.moves_dict["F'"](cube)
                white_daisy_moves.append("F'")
        elif i[0] == 3:
            if i[1] == 1:
                if i[2] == 0:
                    while (cube[0][1][0][0] == "W"):
                        move.moves_dict["U"](cube)
                        white_daisy_moves.append("U")
                    move.moves_dict["L2"](cube)
                    white_daisy_moves.append("L2")
                elif i[2] == 2:
                    while (cube[0][1][2][0] == "W"):
                        move.moves_dict["U"](cube)
                        white_daisy_moves.append("U")
                    move.moves_dict["R2"](cube)
                    white_daisy_moves.append("R2")
            elif i[1] == 0:
                while (cube[0][2][1][0] == "W"):
                    move.moves_dict["U"](cube)
                    white_daisy_moves.append("U")
                move.moves_dict["F2"](cube)
                white_daisy_moves.append("F2")
            elif i[1] == 2:
                while (cube[0][0][1][0] == "W"):
                    move.moves_dict["U"](cube)
                    white_daisy_moves.append("U")
                move.moves_dict["B2"](cube)
                white_daisy_moves.append("B2")
        elif i[0] == 4:
            if i[1] == 1:
                if i[2] == 0:
                    while (cube[0][0][1][0] == "W"):
                        move.moves_dict["U"](cube)
                        white_daisy_moves.append("U")
                    move.moves_dict["B'"](cube)
                    white_daisy_moves.append("B'")
                elif i[2] == 2:
                    while (cube[0][2][1][0] == "W"):
                        move.moves_dict["U"](cube)
                        white_daisy_moves.append("U")
                    move.moves_dict["F"](cube)
                    white_daisy_moves.append("F")
            elif i[1] == 0:
                move.moves_dict["L"](cube)
                white_daisy_moves.append("L")
                while (cube[0][2][1][0] == "W"):
                    move.moves_dict["U"](cube)
                    white_daisy_moves.append("U")
                move.moves_dict["F"](cube)
                white_daisy_moves.append("F")
            elif i[1] == 2:
                while (cube[0][2][1][0] == "W"):
                    move.moves_dict["U"](cube)
                    white_daisy_moves.append("U")
                move.moves_dict["L'"](cube)
                white_daisy_moves.append("L'")
                move.moves_dict["F"](cube)
                white_daisy_moves.append("F")
                move.moves_dict["L"](cube)
                white_daisy_moves.append("L")
        elif i[0] == 5:
            if i[1] == 1:
                if i[2] == 0:
                    while (cube[0][1][2][0] == "W"):
                        move.moves_dict["U"](cube)
                        white_daisy_moves.append("U")
                    move.moves_dict["R'"](cube)
                    white_daisy_moves.append("R'")
                elif i[2] == 2:
                    while (cube[0][1][0][0] == "W"):
                        move.moves_dict["U"](cube)
                        white_daisy_moves.append("U")
                    move.moves_dict["L"](cube)
                    white_daisy_moves.append("L")
            elif i[1] == 0:
                move.moves_dict["B'"](cube)
                white_daisy_moves.append("B'")
                while (cube[0][1][2][0] == "W"):
                    move.moves_dict["U"](cube)
                    white_daisy_moves.append("U")
                move.moves_dict["R'"](cube)
                white_daisy_moves.append("R'")
            elif i[1] == 2:
                while (cube[0][1][2][0] == "W"):
                    move.moves_dict["U"](cube)
                    white_daisy_moves.append("U")
                move.moves_dict["B"](cube)
                white_daisy_moves.append("B")
                move.moves_dict["R'"](cube)
                white_daisy_moves.append("R'")
                move.moves_dict["B'"](cube)
                white_daisy_moves.append("B'")
        # print(white_daisy_moves)
        # for i in range(3):
        #     for j in range(6):
        #         print(cube[j][i],end=" ")
        #     print()            
        # print()            
    
    print(white_daisy_moves)
    for i in range(3):
        for j in range(6):
            print(cube[j][i],end=" ")
        print()
    
    # if (cube[0][0][1][0] == "W") and (cube[0][1][0][0] == "W") and (cube[0][1][2][0] == "W") and (cube[0][2][1][0] == "W"):
        # return
    # else:
        # whiteCross(cube)

def solveCube(cube,cube_solved):
    print("SoLve the white cross : ")
    
    whiteCross(cube)
    
    return