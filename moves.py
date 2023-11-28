def move_U2(cube):
    cube[1][0],cube[4][0] = cube[4][0],cube[1][0]
    cube[2][0],cube[5][0] = cube[5][0],cube[2][0]
    return cube

def move_U(cube):
    temp = cube[2][0]
    cube[2][0] = cube[1][0]
    cube[1][0] = cube[5][0]
    cube[5][0] = cube[4][0]
    cube[4][0] = temp
    return cube

def move_Uprime(cube):
    temp = cube[2][0]
    cube[2][0] = cube[4][0]
    cube[4][0] = cube[5][0]
    cube[5][0] = cube[1][0]
    cube[1][0] = temp
    return cube

def move_D2(cube):
    cube[1][2],cube[4][2] = cube[4][0],cube[1][2]
    cube[2][2],cube[5][2] = cube[5][0],cube[2][2]
    return cube

def move_D(cube):
    temp = cube[2][2]
    cube[2][2] = cube[4][2]
    cube[4][2] = cube[5][2]
    cube[5][2] = cube[1][2]
    cube[1][2] = temp
    return cube

def move_Dprime(cube):
    temp = cube[2][2]
    cube[2][2] = cube[1][2]
    cube[1][2] = cube[5][2]
    cube[5][2] = cube[4][2]
    cube[4][2] = temp
    return cube

def move_R2(cube):
    for i in range(0,3):
        # swap yellow and white pieces
        cube[0][i][2],cube[3][i][2] = cube[3][i][2],cube[0][i][2]
        #swap blue and green prices
        cube[2][i][2],cube[5][i][2] = cube[5][i][2],cube[2][i][2]

    return cube

def move_R(cube):
    for i in range(0,3):
        temp = cube[0][i][2]
        cube[0][i][2] = cube[2][i][2]
        cube[2][i][2] = cube[3][i][2]
        cube[3][i][2] = cube[5][i][2]
        cube[5][i][2] = temp
    return cube

def move_Rprime(cube):
    for i in range(0,3):
        temp = cube[0][i][2]
        cube[0][i][2] = cube[5][i][2]
        cube[5][i][2] = cube[3][i][2]
        cube[3][i][2] = cube[2][i][2]
        cube[2][i][2] = temp
    return cube

def move_L2(cube):
    for i in range(0,3):
        # swap yellow and white pieces
        cube[0][i][0],cube[3][i][0] = cube[3][i][1],cube[0][i][0]
        #swap blue and green prices
        cube[2][i][0],cube[5][i][0] = cube[5][i][1],cube[2][i][0]
    return cube

def move_L(cube):
    for i in range(0,3):
        temp = cube[0][i][0]
        cube[0][i][0] = cube[5][i][0]
        cube[5][i][0] = cube[3][i][0]
        cube[3][i][0] = cube[2][i][0]
        cube[2][i][0] = temp
    return cube

def move_Lprime(cube):
    for i in range(0,3):
        temp = cube[0][i][0]
        cube[0][i][0] = cube[2][i][0]
        cube[2][i][0] = cube[3][i][0]
        cube[3][i][0] = cube[5][i][0]
        cube[5][i][0] = temp
    return cube

def move_F2(cube):
    cube[0][2],cube[3][2] = cube[3][2],cube[0][2]
    cube[1][2],cube[4][2] = cube[4][2],cube[1][2]
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
    "B'" : move_Bprime,
    
}