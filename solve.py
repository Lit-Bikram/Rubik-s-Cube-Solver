import moves as move

def display(cube):
    for i in range(3):
        for j in range(6):
            print(cube[j][i],end=" ")
        print()
    print()
    
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

def findCorner(cube,x,y,z):
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
    
    for i in range(6):
        for j in range(3):
            for k in range(3):
                if cube[i][j][k] == z:
                    temp3 = []
                    temp3.append(i)
                    temp3.append(j)
                    temp3.append(k)
                     
    return temp1, temp2, temp3

def whiteDaisy(cube):
    white_edges = [["W2","G8"],["W4","R8"],["W6","O8"],["W8","B8"]]
    white_daisy_moves = []
    for edge in white_edges:
        i,j = findEdge(cube,edge[0],edge[1])
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
                
    
    print(" ".join(white_daisy_moves),end="\n\n")  
    
    
def whiteCross(cube):
    white_edges = [["W2","G8"],["W4","R8"],["W6","O8"],["W8","B8"]]
    white_cross_moves = []
    for edge in white_edges:
        i,j = findEdge(cube,edge[0],edge[1])
        val = cube[j[0]][j[1]][j[2]]
        if val == "G8":
            while (cube[2][0][1] != val):
                move.moves_dict["U"](cube)
                white_cross_moves.append("U")
            move.moves_dict["F2"](cube)
            white_cross_moves.append("F2")
        elif val == "R8":
            while (cube[4][0][1] != val):
                move.moves_dict["U"](cube)
                white_cross_moves.append("U")
            move.moves_dict["L2"](cube)
            white_cross_moves.append("L2")
        elif val == "O8":
            while (cube[1][0][1] != val):
                move.moves_dict["U"](cube)
                white_cross_moves.append("U")
            move.moves_dict["R2"](cube)
            white_cross_moves.append("R2")
        elif val == "B8":
            while (cube[5][0][1] != val):
                move.moves_dict["U"](cube)
                white_cross_moves.append("U")
            move.moves_dict["B2"](cube)
            white_cross_moves.append("B2")
            
                
        
    print(" ".join(white_cross_moves),end="\n\n")
   

def firstLayer(cube):
    white_corners = [
        ["W1","G7","R9"],
        ["W3","O7","G9"],
        ["W7","R7","B9"],
        ["W9","B7","O9"]
    ]
    first_layer_moves = []
    
    for corner in white_corners:
        def solveFirstLayer(cube,corner):
            corner_position = []
            i,j,k = findCorner(cube,corner[0],corner[1],corner[2])
            corner_position.append(i[0])
            corner_position.append(j[0])
            corner_position.append(k[0])
            corner_position.sort()
            
            if corner_position[0] == 0:
                if corner[0] == "W3":
                    corner_position_temp = corner_position
                    while (corner_position_temp != [0,1,2]):
                        move.moves_dict["U"](cube)
                        first_layer_moves.append("U")
                        corner_position_temp.clear()
                        i,j,k = findCorner(cube,corner[0],corner[1],corner[2])
                        corner_position_temp.append(i[0])
                        corner_position_temp.append(j[0])
                        corner_position_temp.append(k[0])
                        corner_position_temp.sort()
                        
                    while (cube[3][0][2] != "W3"):
                        move.moves_dict["R"](cube)
                        first_layer_moves.append("R")
                        move.moves_dict["U"](cube)
                        first_layer_moves.append("U")
                        move.moves_dict["R'"](cube)
                        first_layer_moves.append("R'")
                        move.moves_dict["U'"](cube)
                        first_layer_moves.append("U'")  
                
                elif corner[0] == "W1":
                    corner_position_temp = corner_position
                    while (corner_position_temp != [0,2,4]):
                        move.moves_dict["U"](cube)
                        first_layer_moves.append("U")
                        corner_position_temp.clear()
                        i,j,k = findCorner(cube,corner[0],corner[1],corner[2])
                        corner_position_temp.append(i[0])
                        corner_position_temp.append(j[0])
                        corner_position_temp.append(k[0])
                        corner_position_temp.sort()
                        
                    while (cube[3][0][0] != "W1"):
                        move.moves_dict["L'"](cube)
                        first_layer_moves.append("L'")
                        move.moves_dict["U'"](cube)
                        first_layer_moves.append("U'")
                        move.moves_dict["L"](cube)
                        first_layer_moves.append("L")
                        move.moves_dict["U"](cube)
                        first_layer_moves.append("U")
                
                elif corner[0] == "W7":
                    corner_position_temp = corner_position
                    while (corner_position_temp != [0,4,5]):
                        move.moves_dict["U"](cube)
                        first_layer_moves.append("U")
                        corner_position_temp.clear()
                        i,j,k = findCorner(cube,corner[0],corner[1],corner[2])
                        corner_position_temp.append(i[0])
                        corner_position_temp.append(j[0])
                        corner_position_temp.append(k[0])
                        corner_position_temp.sort()
                        
                    while (cube[3][2][0] != "W7"):
                        move.moves_dict["L"](cube)
                        first_layer_moves.append("L")
                        move.moves_dict["U"](cube)
                        first_layer_moves.append("U")
                        move.moves_dict["L'"](cube)
                        first_layer_moves.append("L'")
                        move.moves_dict["U'"](cube)
                        first_layer_moves.append("U'")
                    
                elif corner[0] == "W9":
                    corner_position_temp = corner_position
                    while (corner_position_temp != [0,1,5]):
                        move.moves_dict["U"](cube)
                        first_layer_moves.append("U")
                        corner_position_temp.clear()
                        i,j,k = findCorner(cube,corner[0],corner[1],corner[2])
                        corner_position_temp.append(i[0])
                        corner_position_temp.append(j[0])
                        corner_position_temp.append(k[0])
                        corner_position_temp.sort()
                        
                    while (cube[3][2][2] != "W9"):
                        move.moves_dict["R'"](cube)
                        first_layer_moves.append("R'")
                        move.moves_dict["U'"](cube)
                        first_layer_moves.append("U'")
                        move.moves_dict["R"](cube)
                        first_layer_moves.append("R")
                        move.moves_dict["U"](cube)
                        first_layer_moves.append("U")
                
            else:
                if (corner_position == [2,3,4]):
                    move.moves_dict["L'"](cube)
                    first_layer_moves.append("L'")
                    move.moves_dict["U'"](cube)
                    first_layer_moves.append("U'")
                    move.moves_dict["L"](cube)
                    first_layer_moves.append("L")
                    solveFirstLayer(cube,corner)
                elif (corner_position == [1,2,3]):
                    move.moves_dict["R"](cube)
                    first_layer_moves.append("R")
                    move.moves_dict["U"](cube)
                    first_layer_moves.append("U")
                    move.moves_dict["R'"](cube)
                    first_layer_moves.append("R'")
                    solveFirstLayer(cube,corner)
                elif (corner_position == [3,4,5]):
                    move.moves_dict["L"](cube)
                    first_layer_moves.append("L")
                    move.moves_dict["U"](cube)
                    first_layer_moves.append("U")
                    move.moves_dict["L'"](cube)
                    first_layer_moves.append("L'")
                    solveFirstLayer(cube,corner)
                elif (corner_position == [1,3,5]):
                    move.moves_dict["R'"](cube)
                    first_layer_moves.append("R'")
                    move.moves_dict["U'"](cube)
                    first_layer_moves.append("U'")
                    move.moves_dict["R"](cube)
                    first_layer_moves.append("R")
                    solveFirstLayer(cube,corner)
            
            return first_layer_moves

        solveFirstLayer(cube,corner)
    
    
    print(" ".join(first_layer_moves),"\n")
                    
    return


def secondLayer(cube):
    second_layer_edges = [
        ["G6","O4"],
        ["G4","R6"],
        ["B4","O6"],
        ["B6","R4"]
    ]
    second_layer_moves = []
    
    for edge in second_layer_edges:
        edge_position = []        
        i,j = findEdge(cube,edge[0],edge[1])
        edge_position.append(i[0])
        edge_position.append(j[0])
        edge_position.sort()
        if edge[0] == "G6" and edge[1] == "O4":
            def insertGreenOrangeEdge():
                i,j = findEdge(cube,edge[0],edge[1])
                if i > j:
                    while(cube[2][0][1] != "G6"):
                        move.moves_dict["U"](cube)
                        second_layer_moves.append("U")
                    move.moves_dict["U"](cube)
                    second_layer_moves.append("U")
                    move.moves_dict["R"](cube)
                    second_layer_moves.append("R")
                    move.moves_dict["U"](cube)
                    second_layer_moves.append("U")
                    move.moves_dict["R'"](cube)
                    second_layer_moves.append("R'")
                    move.moves_dict["U'"](cube)
                    second_layer_moves.append("U'")
                    move.moves_dict["F'"](cube)
                    second_layer_moves.append("F'")
                    move.moves_dict["U'"](cube)
                    second_layer_moves.append("U'")
                    move.moves_dict["F"](cube)
                    second_layer_moves.append("F")
                else:
                    while(cube[1][0][1] != "O4"):
                        move.moves_dict["U"](cube)
                        second_layer_moves.append("U")
                    move.moves_dict["U'"](cube)
                    second_layer_moves.append("U'")
                    move.moves_dict["F'"](cube)
                    second_layer_moves.append("F'")
                    move.moves_dict["U'"](cube)
                    second_layer_moves.append("U'")
                    move.moves_dict["F"](cube)
                    second_layer_moves.append("F")
                    move.moves_dict["U"](cube)
                    second_layer_moves.append("U")
                    move.moves_dict["R"](cube)
                    second_layer_moves.append("R")
                    move.moves_dict["U"](cube)
                    second_layer_moves.append("U")
                    move.moves_dict["R'"](cube)
                    second_layer_moves.append("R'")
            if edge_position[0] == 0:
                insertGreenOrangeEdge()
            elif edge_position[0] == 1 and edge_position[1] == 2:
                if cube[2][1][2] == "G6" and cube[1][1][0] == "O4":
                    continue
                else:
                    move.moves_dict["R"](cube)
                    second_layer_moves.append("R")
                    move.moves_dict["U"](cube)
                    second_layer_moves.append("U")
                    move.moves_dict["R'"](cube)
                    second_layer_moves.append("R'")
                    move.moves_dict["U'"](cube)
                    second_layer_moves.append("U'")
                    move.moves_dict["F'"](cube)
                    second_layer_moves.append("F'")
                    move.moves_dict["U'"](cube)
                    second_layer_moves.append("U'")
                    move.moves_dict["F"](cube)
                    second_layer_moves.append("F")
                    insertGreenOrangeEdge()
            elif edge_position[0] == 2 and edge_position[1] == 4:
                move.moves_dict["L'"](cube)
                second_layer_moves.append("L'")
                move.moves_dict["U'"](cube)
                second_layer_moves.append("U'")
                move.moves_dict["L"](cube)
                second_layer_moves.append("L")
                move.moves_dict["U"](cube)
                second_layer_moves.append("U")
                move.moves_dict["F"](cube)
                second_layer_moves.append("F")
                move.moves_dict["U"](cube)
                second_layer_moves.append("U")
                move.moves_dict["F'"](cube)
                second_layer_moves.append("F'")
                insertGreenOrangeEdge()
            elif edge_position[0] == 4 and edge_position[1] == 5:
                move.moves_dict["L"](cube)
                second_layer_moves.append("L")
                move.moves_dict["U"](cube)
                second_layer_moves.append("U")
                move.moves_dict["L'"](cube)
                second_layer_moves.append("L'")
                move.moves_dict["U'"](cube)
                second_layer_moves.append("U'")
                move.moves_dict["B'"](cube)
                second_layer_moves.append("B'")
                move.moves_dict["U'"](cube)
                second_layer_moves.append("U'")
                move.moves_dict["B"](cube)
                second_layer_moves.append("B")
                insertGreenOrangeEdge()
            elif edge_position[0] == 1 and edge_position[1] == 5:
                move.moves_dict["R'"](cube)
                second_layer_moves.append("R'")
                move.moves_dict["U'"](cube)
                second_layer_moves.append("U'")
                move.moves_dict["R"](cube)
                second_layer_moves.append("R")
                move.moves_dict["U"](cube)
                second_layer_moves.append("U")
                move.moves_dict["B"](cube)
                second_layer_moves.append("B")
                move.moves_dict["U"](cube)
                second_layer_moves.append("U")
                move.moves_dict["B'"](cube)
                second_layer_moves.append("B'")
                insertGreenOrangeEdge()
        elif edge[0] == "G4" and edge[1] == "R6":
            def insertGreenRedEdge():
                i,j = findEdge(cube,edge[0],edge[1])
                if i > j:
                    while (cube[2][0][1] != "G4"):
                        move.moves_dict["U"](cube)
                        second_layer_moves.append("U")
                    move.moves_dict["U'"](cube)
                    second_layer_moves.append("U'")
                    move.moves_dict["L'"](cube)
                    second_layer_moves.append("L'")
                    move.moves_dict["U'"](cube)
                    second_layer_moves.append("U'")
                    move.moves_dict["L"](cube)
                    second_layer_moves.append("L")
                    move.moves_dict["U"](cube)
                    second_layer_moves.append("U")
                    move.moves_dict["F"](cube)
                    second_layer_moves.append("F")
                    move.moves_dict["U"](cube)
                    second_layer_moves.append("U")
                    move.moves_dict["F'"](cube)
                    second_layer_moves.append("F'")
                else:
                    while (cube[4][0][1] != "R6"):
                        move.moves_dict["U"](cube)
                        second_layer_moves.append("U")
                    move.moves_dict["U"](cube)
                    second_layer_moves.append("U")
                    move.moves_dict["F"](cube)
                    second_layer_moves.append("F")
                    move.moves_dict["U"](cube)
                    second_layer_moves.append("U")
                    move.moves_dict["F'"](cube)
                    second_layer_moves.append("F'")
                    move.moves_dict["U'"](cube)
                    second_layer_moves.append("U'")
                    move.moves_dict["L'"](cube)
                    second_layer_moves.append("L'")
                    move.moves_dict["U'"](cube)
                    second_layer_moves.append("U'")
                    move.moves_dict["L"](cube)
                    second_layer_moves.append("L")
                    move.moves_dict["U"](cube)
                    second_layer_moves.append("U")
            if edge_position[0] == 0:
                insertGreenRedEdge()
            elif edge_position[0] == 2 and edge_position[1] == 4:
                if cube[2][1][0] == "G4" and cube[4][1][2] == "R6":
                    continue
                else:
                    move.moves_dict["F"](cube)
                    second_layer_moves.append("F")
                    move.moves_dict["U"](cube)
                    second_layer_moves.append("U")
                    move.moves_dict["F'"](cube)
                    second_layer_moves.append("F'")
                    move.moves_dict["U'"](cube)
                    second_layer_moves.append("U'")
                    move.moves_dict["L'"](cube)
                    second_layer_moves.append("L'")
                    move.moves_dict["U'"](cube)
                    second_layer_moves.append("U'")
                    move.moves_dict["L"](cube)
                    second_layer_moves.append("L")
                    move.moves_dict["U"](cube)
                    second_layer_moves.append("U")
                    insertGreenRedEdge()
            elif edge_position[0] == 1 and edge_position[1] == 2:
                move.moves_dict["R"](cube)
                second_layer_moves.append("R")
                move.moves_dict["U"](cube)
                second_layer_moves.append("U")
                move.moves_dict["R'"](cube)
                second_layer_moves.append("R'")
                move.moves_dict["U'"](cube)
                second_layer_moves.append("U'")
                move.moves_dict["F'"](cube)
                second_layer_moves.append("F'")
                move.moves_dict["U'"](cube)
                second_layer_moves.append("U'")
                move.moves_dict["F"](cube)
                second_layer_moves.append("F")
                insertGreenRedEdge()
            elif edge_position[0] == 4 and edge_position[1] == 5:
                move.moves_dict["L"](cube)
                second_layer_moves.append("L")
                move.moves_dict["U"](cube)
                second_layer_moves.append("U")
                move.moves_dict["L'"](cube)
                second_layer_moves.append("L'")
                move.moves_dict["U'"](cube)
                second_layer_moves.append("U'")
                move.moves_dict["B'"](cube)
                second_layer_moves.append("B'")
                move.moves_dict["U'"](cube)
                second_layer_moves.append("U'")
                move.moves_dict["B"](cube)
                second_layer_moves.append("B")
                insertGreenRedEdge()
            elif edge_position[0] == 1 and edge_position[1] == 5:
                move.moves_dict["R'"](cube)
                second_layer_moves.append("R'")
                move.moves_dict["U'"](cube)
                second_layer_moves.append("U'")
                move.moves_dict["R"](cube)
                second_layer_moves.append("R")
                move.moves_dict["U"](cube)
                second_layer_moves.append("U")
                move.moves_dict["B"](cube)
                second_layer_moves.append("B")
                move.moves_dict["U"](cube)
                second_layer_moves.append("U")
                move.moves_dict["B'"](cube)
                second_layer_moves.append("B'")
                insertGreenRedEdge()
        elif edge[0] == "B4" and edge[1] == "O6":
            def insertBlueOrangeEdge():
                i,j = findEdge(cube,edge[0],edge[1])
                if i > j:
                    while (cube[5][0][1] !=  "B4"):
                        move.moves_dict["U"](cube)
                        second_layer_moves.append("U")
                    move.moves_dict["U'"](cube)
                    second_layer_moves.append("U'")
                    move.moves_dict["R'"](cube)
                    second_layer_moves.append("R'")
                    move.moves_dict["U'"](cube)
                    second_layer_moves.append("U'")
                    move.moves_dict["R"](cube)
                    second_layer_moves.append("R")
                    move.moves_dict["U"](cube)
                    second_layer_moves.append("U")
                    move.moves_dict["B"](cube)
                    second_layer_moves.append("B")
                    move.moves_dict["U"](cube)
                    second_layer_moves.append("U")
                    move.moves_dict["B'"](cube)
                    second_layer_moves.append("B'")
                else:
                    while (cube[1][0][1] !=  "O6"):
                        move.moves_dict["U"](cube)
                        second_layer_moves.append("U")
                    move.moves_dict["U"](cube)
                    second_layer_moves.append("U")
                    move.moves_dict["B"](cube)
                    second_layer_moves.append("B")
                    move.moves_dict["U"](cube)
                    second_layer_moves.append("U")
                    move.moves_dict["B'"](cube)
                    second_layer_moves.append("B'")
                    move.moves_dict["U'"](cube)
                    second_layer_moves.append("U'")
                    move.moves_dict["R'"](cube)
                    second_layer_moves.append("R'")
                    move.moves_dict["U'"](cube)
                    second_layer_moves.append("U'")
                    move.moves_dict["R"](cube)
                    second_layer_moves.append("R")       
            if edge_position[0] == 0:
                insertBlueOrangeEdge()
            elif edge_position[0] == 1 and edge_position[1] == 5:
                if cube[5][1][0] == "B4" and cube[1][1][2] == "O6":
                    continue
                else:
                    move.moves_dict["R'"](cube)
                    second_layer_moves.append("R'")
                    move.moves_dict["U'"](cube)
                    second_layer_moves.append("U'")
                    move.moves_dict["R"](cube)
                    second_layer_moves.append("R")
                    move.moves_dict["U"](cube)
                    second_layer_moves.append("U")
                    move.moves_dict["B"](cube)
                    second_layer_moves.append("B")
                    move.moves_dict["U"](cube)
                    second_layer_moves.append("U")
                    move.moves_dict["B'"](cube)
                    second_layer_moves.append("B'")
                    insertBlueOrangeEdge()
            elif edge_position[0] == 1 and edge_position[1] == 2:
                move.moves_dict["R"](cube)
                second_layer_moves.append("R")
                move.moves_dict["U"](cube)
                second_layer_moves.append("U")
                move.moves_dict["R'"](cube)
                second_layer_moves.append("R'")
                move.moves_dict["U'"](cube)
                second_layer_moves.append("U'")
                move.moves_dict["F'"](cube)
                second_layer_moves.append("F'")
                move.moves_dict["U'"](cube)
                second_layer_moves.append("U'")
                move.moves_dict["F"](cube)
                second_layer_moves.append("F")
                insertBlueOrangeEdge()
            elif edge_position[0] == 2 and edge_position[1] == 4:
                move.moves_dict["L'"](cube)
                second_layer_moves.append("L'")
                move.moves_dict["U'"](cube)
                second_layer_moves.append("U'")
                move.moves_dict["L"](cube)
                second_layer_moves.append("L")
                move.moves_dict["U"](cube)
                second_layer_moves.append("U")
                move.moves_dict["F"](cube)
                second_layer_moves.append("F")
                move.moves_dict["U"](cube)
                second_layer_moves.append("U")
                move.moves_dict["F'"](cube)
                second_layer_moves.append("F'")
                insertBlueOrangeEdge()
            elif edge_position[0] == 4 and edge_position[1] == 5:
                move.moves_dict["L"](cube)
                second_layer_moves.append("L")
                move.moves_dict["U"](cube)
                second_layer_moves.append("U")
                move.moves_dict["L'"](cube)
                second_layer_moves.append("L'")
                move.moves_dict["U'"](cube)
                second_layer_moves.append("U'")
                move.moves_dict["B'"](cube)
                second_layer_moves.append("B'")
                move.moves_dict["U'"](cube)
                second_layer_moves.append("U'")
                move.moves_dict["B"](cube)
                second_layer_moves.append("B")
                insertBlueOrangeEdge()
        elif edge[0] == "B6" and edge[1] == "R4":
            def insertBlueRedEdge():
                i,j = findEdge(cube,edge[0],edge[1])
                if i > j:
                    while (cube[5][0][1] != "B6"):
                        move.moves_dict["U"](cube)
                        second_layer_moves.append("U")
                    move.moves_dict["U"](cube)
                    second_layer_moves.append("U")
                    move.moves_dict["L"](cube)
                    second_layer_moves.append("L")
                    move.moves_dict["U"](cube)
                    second_layer_moves.append("U")
                    move.moves_dict["L'"](cube)
                    second_layer_moves.append("L'")
                    move.moves_dict["U'"](cube)
                    second_layer_moves.append("U'")
                    move.moves_dict["B'"](cube)
                    second_layer_moves.append("B'")
                    move.moves_dict["U'"](cube)
                    second_layer_moves.append("U'")
                    move.moves_dict["B"](cube)
                    second_layer_moves.append("B")
                else:
                    while (cube[4][0][1] != "R4"):
                        move.moves_dict["U"](cube)
                        second_layer_moves.append("U")
                    move.moves_dict["U'"](cube)
                    second_layer_moves.append("U'")
                    move.moves_dict["B'"](cube)
                    second_layer_moves.append("B'")
                    move.moves_dict["U'"](cube)
                    second_layer_moves.append("U'")
                    move.moves_dict["B"](cube)
                    second_layer_moves.append("B")
                    move.moves_dict["U"](cube)
                    second_layer_moves.append("U")
                    move.moves_dict["L"](cube)
                    second_layer_moves.append("L")
                    move.moves_dict["U"](cube)
                    second_layer_moves.append("U")
                    move.moves_dict["L'"](cube)
                    second_layer_moves.append("L'")                    
            if edge_position[0] == 0:
                insertBlueRedEdge()
            elif edge_position[0] == 4 and edge_position[1] == 5:
                if cube[5][1][2] == "B6" and cube[4][1][0] == "R4":
                    continue
                else:
                    move.moves_dict["L"](cube)
                    second_layer_moves.append("L")
                    move.moves_dict["U"](cube)
                    second_layer_moves.append("U")
                    move.moves_dict["L'"](cube)
                    second_layer_moves.append("L'")
                    move.moves_dict["U'"](cube)
                    second_layer_moves.append("U'")
                    move.moves_dict["B'"](cube)
                    second_layer_moves.append("B'")
                    move.moves_dict["U'"](cube)
                    second_layer_moves.append("U'")
                    move.moves_dict["B"](cube)
                    second_layer_moves.append("B")
                    insertBlueRedEdge()
            elif edge_position[0] == 1 and edge_position[1] == 2:
                move.moves_dict["R"](cube)
                second_layer_moves.append("R")
                move.moves_dict["U"](cube)
                second_layer_moves.append("U")
                move.moves_dict["R'"](cube)
                second_layer_moves.append("R'")
                move.moves_dict["U'"](cube)
                second_layer_moves.append("U'")
                move.moves_dict["F'"](cube)
                second_layer_moves.append("F'")
                move.moves_dict["U'"](cube)
                second_layer_moves.append("U'")
                move.moves_dict["F"](cube)
                second_layer_moves.append("F")
                insertBlueRedEdge()
            elif edge_position[0] == 2 and edge_position[1] == 4:
                move.moves_dict["L'"](cube)
                second_layer_moves.append("L'")
                move.moves_dict["U'"](cube)
                second_layer_moves.append("U'")
                move.moves_dict["L"](cube)
                second_layer_moves.append("L")
                move.moves_dict["U"](cube)
                second_layer_moves.append("U")
                move.moves_dict["F"](cube)
                second_layer_moves.append("F")
                move.moves_dict["U"](cube)
                second_layer_moves.append("U")
                move.moves_dict["F'"](cube)
                second_layer_moves.append("F'")
                insertBlueRedEdge()
            elif edge_position[0] == 1 and edge_position[1] == 5:
                move.moves_dict["R'"](cube)
                second_layer_moves.append("R'")
                move.moves_dict["U'"](cube)
                second_layer_moves.append("U'")
                move.moves_dict["R"](cube)
                second_layer_moves.append("R")
                move.moves_dict["U"](cube)
                second_layer_moves.append("U")
                move.moves_dict["B"](cube)
                second_layer_moves.append("B")
                move.moves_dict["U"](cube)
                second_layer_moves.append("U")
                move.moves_dict["B'"](cube)
                second_layer_moves.append("B'")
                insertBlueRedEdge()
    print(" ".join(second_layer_moves),"\n")
                    
    return
    
def yellowCross(cube):
    yellow_cross_moves = []
    def solveYellowCross():
        if cube[0][0][1][0] == "Y" and cube[0][2][1][0] == "Y" and cube[0][1][0][0] =="Y" and cube[0][1][2][0] == "Y":
            return
        elif (cube[0][0][1][0] == "Y" and cube[0][2][1][0] == "Y") or (cube[0][1][0][0] =="Y" and cube[0][1][2][0] == "Y"):
            while (cube[0][1][0][0] !="Y" and cube[0][1][2][0] != "Y"):
                move.moves_dict["U"](cube)
                yellow_cross_moves.append("U")
            move.moves_dict["F"](cube)
            yellow_cross_moves.append("F")
            move.moves_dict["R"](cube)
            yellow_cross_moves.append("R")
            move.moves_dict["U"](cube)
            yellow_cross_moves.append("U")
            move.moves_dict["R'"](cube)
            yellow_cross_moves.append("R'")
            move.moves_dict["U'"](cube)
            yellow_cross_moves.append("U'")
            move.moves_dict["F'"](cube)
            yellow_cross_moves.append("F'")
        elif (cube[0][0][1][0] == "Y" and cube[0][1][2][0] == "Y") or (cube[0][1][2][0] == "Y" and cube[0][2][1][0] == "Y") or (cube[0][2][1][0] == "Y" and cube[0][1][0][0] =="Y") or (cube[0][1][0][0] =="Y" and cube[0][0][1][0] == "Y"):
            if (cube[0][0][1][0] == "Y" and cube[0][1][2][0] == "Y"):
                move.moves_dict["U'"](cube)
                yellow_cross_moves.append("U'")
            elif (cube[0][1][2][0] == "Y" and cube[0][2][1][0] == "Y"):
                move.moves_dict["U2"](cube)
                yellow_cross_moves.append("U2")
            elif (cube[0][2][1][0] == "Y" and cube[0][1][0][0] =="Y"):
                move.moves_dict["U"](cube)
                yellow_cross_moves.append("U")
            else:
                pass
            move.moves_dict["F"](cube)
            yellow_cross_moves.append("F")
            for i in range(2):
                move.moves_dict["R"](cube)
                yellow_cross_moves.append("R")
                move.moves_dict["U"](cube)
                yellow_cross_moves.append("U")
                move.moves_dict["R'"](cube)
                yellow_cross_moves.append("R'")
                move.moves_dict["U'"](cube)
                yellow_cross_moves.append("U'")
            move.moves_dict["F'"](cube)
            yellow_cross_moves.append("F'")
        else:
            move.moves_dict["F"](cube)
            yellow_cross_moves.append("F")
            move.moves_dict["R"](cube)
            yellow_cross_moves.append("R")
            move.moves_dict["U"](cube)
            yellow_cross_moves.append("U")
            move.moves_dict["R'"](cube)
            yellow_cross_moves.append("R'")
            move.moves_dict["U'"](cube)
            yellow_cross_moves.append("U'")
            move.moves_dict["F'"](cube)
            yellow_cross_moves.append("F'")
            solveYellowCross()
    solveYellowCross()
    print(" ".join(yellow_cross_moves),"\n")


def yellowEdge(cube):
    yellow_edge_moves = []
    edges = [["Y6","O2"],["Y8","G2"],["Y4","R2"],["Y2","B2"]]

    def sexyMove():
        move.moves_dict["R"](cube)
        yellow_edge_moves.append("R")
        move.moves_dict["U"](cube)
        yellow_edge_moves.append("U")
        move.moves_dict["R'"](cube)
        yellow_edge_moves.append("R'")
        move.moves_dict["U"](cube)
        yellow_edge_moves.append("U")
        move.moves_dict["R"](cube)
        yellow_edge_moves.append("R")
        move.moves_dict["U2"](cube)
        yellow_edge_moves.append("U2")
        move.moves_dict["R'"](cube)
        yellow_edge_moves.append("R'")
    
    def solveYellowEdge():
        edges_position = []
        for edge in edges:
            i,j = findEdge(cube,edge[0],edge[1])
            edges_position.append(j[0])
        
        if edges_position == [1,2,4,5]:
            print("All edges are in position ")
            return
        elif edges_position == [1,2,5,4]:
            move.moves_dict["U'"](cube)
            yellow_edge_moves.append("U'")
            sexyMove()
            move.moves_dict["U2"](cube)
            yellow_edge_moves.append("U2")
        elif edges_position == [5,2,4,1]:
            move.moves_dict["U2"](cube)
            yellow_edge_moves.append("U2")
            sexyMove()
            move.moves_dict["U'"](cube)
            yellow_edge_moves.append("U'")
        elif edges_position == [2,1,4,5]:
            move.moves_dict["U"](cube)
            yellow_edge_moves.append("U")
            sexyMove()
        elif edges_position == [1,4,2,5]:
            sexyMove()
            move.moves_dict["U"](cube)
            yellow_edge_moves.append("U")
        elif edges_position == [1,5,4,2]:
            sexyMove()
            solveYellowEdge()
        elif edges_position == [4,2,1,5]:
            move.moves_dict["U2"](cube)
            yellow_edge_moves.append("U2")
            sexyMove()
            solveYellowEdge()
        else:
            move.moves_dict["U"](cube)
            yellow_edge_moves.append("U")
            solveYellowEdge()
            
    solveYellowEdge()
    print(" ".join(yellow_edge_moves),"\n")
    return

def yellowCorner(cube):
    yellow_corner_moves = []
    yellow_corners = [
        ["Y1","R1","B3"],
        ["Y3","B1","O3"],
        ["Y7","G1","R3"],
        ["Y9","O1","G3"]
    ]
    def leftRightmove():
        move.moves_dict["U"](cube)
        yellow_corner_moves.append("U")
        move.moves_dict["R"](cube)
        yellow_corner_moves.append("R")
        move.moves_dict["U'"](cube)
        yellow_corner_moves.append("U'")
        move.moves_dict["L'"](cube)
        yellow_corner_moves.append("L'")
        move.moves_dict["U"](cube)
        yellow_corner_moves.append("U")
        move.moves_dict["R'"](cube)
        yellow_corner_moves.append("R'")
        move.moves_dict["U'"](cube)
        yellow_corner_moves.append("U'")
        move.moves_dict["L"](cube)
        yellow_corner_moves.append("L")
    
    def solveYellowCorner():
        corner_position = []
        for corner in yellow_corners:
            temp = []
            i,j,k = findCorner(cube,corner[0],corner[1],corner[2])
            temp = [i[0],j[0],k[0]]
            temp.sort()
            corner_position.append(temp)
        
        if corner_position == [[0,4,5],[0,1,5],[0,2,4],[0,1,2]]:
            return
        elif corner_position[0] == [0,4,5]:
            move.moves_dict["U2"](cube)
            yellow_corner_moves.append("U2")
            leftRightmove()
            move.moves_dict["U2"](cube)
            yellow_corner_moves.append("U2")
            solveYellowCorner()
        elif corner_position[1] == [0,1,5]:
            move.moves_dict["U"](cube)
            yellow_corner_moves.append("U")
            leftRightmove()
            move.moves_dict["U'"](cube)
            yellow_corner_moves.append("U'")
            solveYellowCorner()
        elif corner_position[2] == [0,2,4]:
            move.moves_dict["U'"](cube)
            yellow_corner_moves.append("U'")
            leftRightmove()
            move.moves_dict["U"](cube)
            yellow_corner_moves.append("U")
            solveYellowCorner()
        elif corner_position[3] == [0,1,2]:
            leftRightmove()
            solveYellowCorner()
        else:
            leftRightmove()
            solveYellowCorner()
    
    solveYellowCorner()
    print(" ".join(yellow_corner_moves),"\n")
    return

def yellowCornerOrientation(cube):
    yellow_corner_orientation_moves = []
    for i in range(4):
        if cube[0][2][2][0] == "Y":
            move.moves_dict["U"](cube)
            yellow_corner_orientation_moves.append("U")
            continue
        else:
            while (cube[0][2][2][0] != "Y"):
                move.moves_dict["R'"](cube)
                yellow_corner_orientation_moves.append("R'")
                move.moves_dict["D'"](cube)
                yellow_corner_orientation_moves.append("D'")
                move.moves_dict["R"](cube)
                yellow_corner_orientation_moves.append("R")
                move.moves_dict["D"](cube)
                yellow_corner_orientation_moves.append("D")
            move.moves_dict["U"](cube)
            yellow_corner_orientation_moves.append("U")
    print(" ".join(yellow_corner_orientation_moves),"\n")

def solveCube(cube):
    
    print("SoLve the White Daisy : ")
    whiteDaisy(cube)
    
    print("SoLve the White Cross : ")
    whiteCross(cube)
    
    print("SoLve the First Layer : ")
    firstLayer(cube)
    
    print("Solve the second layer : ")
    secondLayer(cube)
    
    print("Solve the Yellow Cross : ")
    yellowCross(cube)
    
    print("Solve the Yellow Edges : ")
    yellowEdge(cube)
    
    print("Solve the Yellow Corners :")
    yellowCorner(cube)

    print("Orient the Yellow Corners : ")
    yellowCornerOrientation(cube)
    
    display(cube)
    
    return