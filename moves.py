def move_U2(cube):
    cube[1][0],cube[4][0] = cube[4][0],cube[1][0]
    cube[2][0],cube[5][0] = cube[5][0],cube[2][0]
    
    #swaping the yellow side
    cube[0][0][0],cube[0][2][2] = cube[0][2][2],cube[0][0][0]
    cube[0][0][2],cube[0][2][0] = cube[0][2][0],cube[0][0][2]
    cube[0][0][1],cube[0][2][1] = cube[0][2][1],cube[0][0][1]
    cube[0][1][0],cube[0][1][2] = cube[0][1][2],cube[0][1][0]
    return cube

def move_U(cube):
    temp = cube[2][0]
    cube[2][0] = cube[1][0]
    cube[1][0] = cube[5][0]
    cube[5][0] = cube[4][0]
    cube[4][0] = temp
    
    #rotating corner peices
    temp = cube[0][0][0]
    cube[0][0][0] = cube[0][2][0]
    cube[0][2][0] = cube[0][2][2]
    cube[0][2][2] = cube[0][0][2]
    cube[0][0][2] = temp
    
    #rotating the edge pieces
    temp = cube[0][0][1]
    cube[0][0][1] = cube[0][1][0]
    cube[0][1][0] = cube[0][2][1]
    cube[0][2][1] = cube[0][1][2]
    cube[0][1][2] = temp
    return cube

def move_Uprime(cube):
    temp = cube[2][0]
    cube[2][0] = cube[4][0]
    cube[4][0] = cube[5][0]
    cube[5][0] = cube[1][0]
    cube[1][0] = temp
    
    #rotating corner prices 
    temp = cube[0][0][0]
    cube[0][0][0] = cube[0][0][2]
    cube[0][0][2] = cube[0][2][2]
    cube[0][2][2] = cube[0][2][0]
    cube[0][2][0] = temp
    
    #rotating the edge pieces
    temp = cube[0][0][1]
    cube[0][0][1] = cube[0][1][2]
    cube[0][1][2] = cube[0][2][1]
    cube[0][2][1] = cube[0][1][0]
    cube[0][1][0] = temp
    return cube

def move_D2(cube):
    cube[1][2],cube[4][2] = cube[4][2],cube[1][2]
    cube[2][2],cube[5][2] = cube[5][2],cube[2][2]
    
    #swaping the yellow side
    cube[3][0][0],cube[3][2][2] = cube[3][2][2],cube[3][0][0]
    cube[3][0][2],cube[3][2][0] = cube[3][2][0],cube[3][0][2]
    cube[3][0][1],cube[3][2][1] = cube[3][2][1],cube[3][0][1]
    cube[3][1][0],cube[3][1][2] = cube[3][1][2],cube[3][1][0]
    return cube

def move_D(cube):
    temp = cube[2][2]
    cube[2][2] = cube[4][2]
    cube[4][2] = cube[5][2]
    cube[5][2] = cube[1][2]
    cube[1][2] = temp
    
    #rotating corner peices
    temp = cube[3][0][0]
    cube[3][0][0] = cube[3][2][0]
    cube[3][2][0] = cube[3][2][2]
    cube[3][2][2] = cube[3][0][2]
    cube[3][0][2] = temp
    
    #rotating the edge pieces
    temp = cube[3][0][1]
    cube[3][0][1] = cube[3][1][0]
    cube[3][1][0] = cube[3][2][1]
    cube[3][2][1] = cube[3][1][2]
    cube[3][1][2] = temp
    
    return cube

def move_Dprime(cube):
    temp = cube[2][2]
    cube[2][2] = cube[1][2]
    cube[1][2] = cube[5][2]
    cube[5][2] = cube[4][2]
    cube[4][2] = temp
    
    #rotating corner prices 
    temp = cube[3][0][0]
    cube[3][0][0] = cube[3][0][2]
    cube[3][0][2] = cube[3][2][2]
    cube[3][2][2] = cube[3][2][0]
    cube[3][2][0] = temp
    
    #rotating the edge pieces
    temp = cube[3][0][1]
    cube[3][0][1] = cube[3][1][2]
    cube[3][1][2] = cube[3][2][1]
    cube[3][2][1] = cube[3][1][0]
    cube[3][1][0] = temp
    
    return cube

def j(i):
        if i == 0 :
            return 2
        elif i == 1:
            return i
        else :
            return 0

def move_R2(cube):
    for i in range(0,3):
        cube[0][i][2],cube[3][i][2] = cube[3][i][2],cube[0][i][2]
        cube[2][j(i)][2],cube[5][i][0] = cube[5][i][0],cube[2][j(i)][2]
        
    #swaping the orange side
    cube[1][0][0],cube[1][2][2] = cube[1][2][2],cube[1][0][0]
    cube[1][0][2],cube[1][2][0] = cube[1][2][0],cube[1][0][2]
    cube[1][0][1],cube[1][2][1] = cube[1][2][1],cube[1][0][1]
    cube[1][1][0],cube[1][1][2] = cube[1][1][2],cube[1][1][0]
    return cube

def move_R(cube):
    for i in range(0,3):
        temp = cube[0][i][2]
        cube[0][i][2] = cube[2][i][2]
        cube[2][i][2] = cube[3][i][2]
        cube[3][i][2] = cube[5][j(i)][0]
        cube[5][j(i)][0] = temp
        
    #rotating corner peices
    temp = cube[1][0][0]
    cube[1][0][0] = cube[1][2][0]
    cube[1][2][0] = cube[1][2][2]
    cube[1][2][2] = cube[1][0][2]
    cube[1][0][2] = temp
    
    #rotating the edge pieces
    temp = cube[1][0][1]
    cube[1][0][1] = cube[1][1][0]
    cube[1][1][0] = cube[1][2][1]
    cube[1][2][1] = cube[1][1][2]
    cube[1][1][2] = temp
    
    return cube

def move_Rprime(cube):
    for i in range(0,3):
        temp = cube[0][i][2]
        cube[0][i][2] = cube[5][j(i)][0]
        cube[5][j(i)][0] = cube[3][i][2]
        cube[3][i][2] = cube[2][i][2]
        cube[2][i][2] = temp
        
    #rotating corner prices 
    temp = cube[1][0][0]
    cube[1][0][0] = cube[1][0][2]
    cube[1][0][2] = cube[1][2][2]
    cube[1][2][2] = cube[1][2][0]
    cube[1][2][0] = temp
    
    #rotating the edge pieces
    temp = cube[1][0][1]
    cube[1][0][1] = cube[1][1][2]
    cube[1][1][2] = cube[1][2][1]
    cube[1][2][1] = cube[1][1][0]
    cube[1][1][0] = temp
    
    return cube

def move_L2(cube):
    for i in range(0,3):
        # swap yellow and white pieces
        cube[0][i][0],cube[3][i][0] = cube[3][i][0],cube[0][i][0]
        #swap blue and green prices
        cube[2][i][0],cube[5][j(i)][2] = cube[5][j(i)][2],cube[2][i][0]
    
    #swaping the red side
    cube[4][0][0],cube[4][2][2] = cube[4][2][2],cube[4][0][0]
    cube[4][0][2],cube[4][2][0] = cube[4][2][0],cube[4][0][2]
    cube[4][0][1],cube[4][2][1] = cube[4][2][1],cube[4][0][1]
    cube[4][1][0],cube[4][1][2] = cube[4][1][2],cube[4][1][0]
    
    return cube

def move_L(cube):
    for i in range(0,3):
        temp = cube[0][i][0]
        cube[0][i][0] = cube[5][j(i)][2]
        cube[5][j(i)][2] = cube[3][i][0]
        cube[3][i][0] = cube[2][i][0]
        cube[2][i][0] = temp
        
    #rotating corner peices
    temp = cube[4][0][0]
    cube[4][0][0] = cube[4][2][0]
    cube[4][2][0] = cube[4][2][2]
    cube[4][2][2] = cube[4][0][2]
    cube[4][0][2] = temp
    
    #rotating the edge pieces
    temp = cube[4][0][1]
    cube[4][0][1] = cube[4][1][0]
    cube[4][1][0] = cube[4][2][1]
    cube[4][2][1] = cube[4][1][2]
    cube[4][1][2] = temp
    
    return cube

def move_Lprime(cube):
    for i in range(0,3):
        temp = cube[0][i][0]
        cube[0][i][0] = cube[2][i][0]
        cube[2][i][0] = cube[3][i][0]
        cube[3][i][0] = cube[5][j(i)][2]
        cube[5][j(i)][2] = temp
    
    #rotating corner prices 
    temp = cube[4][0][0]
    cube[4][0][0] = cube[4][0][2]
    cube[4][0][2] = cube[4][2][2]
    cube[4][2][2] = cube[4][2][0]
    cube[4][2][0] = temp
    
    #rotating the edge pieces
    temp = cube[4][0][1]
    cube[4][0][1] = cube[4][1][2]
    cube[4][1][2] = cube[4][2][1]
    cube[4][2][1] = cube[4][1][0]
    cube[4][1][0] = temp
    
    return cube

def move_F2(cube):
    
    cube[0][2],cube[3][2] = cube[3][2],cube[0][2]
    cube[1][2],cube[4][2] = cube[4][2],cube[1][2]
    
    #swaping the red side
    cube[2][0][0],cube[2][2][2] = cube[2][2][2],cube[2][0][0]
    cube[2][0][2],cube[2][2][0] = cube[2][2][0],cube[2][0][2]
    cube[2][0][1],cube[2][2][1] = cube[2][2][1],cube[2][0][1]
    cube[2][1][0],cube[2][1][2] = cube[2][1][2],cube[2][1][0]
    
    return cube

def move_F(cube):
    temp = cube[0][2]
    cube[0][2] = cube[4][2]
    cube[4][2] = cube[3][2]
    cube[3][2] = cube[1][2]
    cube[1][2] = temp
    return cube

def move_Fprime(cube):
    temp = cube[0][2]
    cube[0][2] = cube[1][2]
    cube[1][2] = cube[3][2]
    cube[3][2] = cube[4][2]
    cube[4][2] = temp
    return cube

def move_B2(cube):
    cube[0][0],cube[3][0] = cube[3][0],cube[0][0]
    cube[1][0],cube[4][0] = cube[4][0],cube[1][0]
    return cube

def move_B(cube):
    temp = cube[0][0]
    cube[0][0] = cube[1][0]
    cube[1][0] = cube[3][0]
    cube[3][0] = cube[4][0]
    cube[4][0] = temp
    return cube

def move_Bprime(cube):
    temp = cube[0][0]
    cube[0][0] = cube[4][0]
    cube[4][0] = cube[3][0]
    cube[3][0] = cube[1][0]
    cube[1][0] = temp
    return cube

moves_dict = {
    
    "U" : move_U,
    "U2" : move_U2,
    "U'" : move_Uprime,
    
    "D" : move_D,
    "D2" : move_D2,
    "D'" : move_Dprime,
    
    "R" : move_R,
    "R2" : move_R2,
    "R'" : move_Rprime,
    
    "L" : move_L,
    "L2" : move_L2,
    "L'" : move_Lprime,
    
    "F" : move_F,
    "F2" : move_F2,
    "F'" : move_Fprime,
    
    "B" : move_B,
    "B2" : move_B2,
    "B'" : move_Bprime
    
}