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
    
    return cube