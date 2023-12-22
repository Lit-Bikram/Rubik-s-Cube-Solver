import scramble as scramble
import moves as move
import solve as solve
# Positions
# Top = yellow
# Front = greem
# Right = orange
# Left = red
# Back = blue
# Down = white
#              |------------|
#              |-U1--U2--U3-|
#              |------------|
#              |-U4--U5--U6-|
#              |------------|
#              |-U7--U8--U9-|
# |------------|------------|------------|------------|
# |-L1--L2--L3-|-F1--F2--F3-|-R1--R2--R3-|-B1--B2--B3-|
# |------------|------------|------------|------------|
# |-L4--L5--L6-|-F4--F5--F6-|-R4--R5--R6-|-B4--B5--B6-|
# |------------|------------|------------|------------|
# |-L7--L8--L9-|-F7--F8--F9-|-R7--R8--R9-|-B7--B8--B9-|
# |------------|------------|------------|------------|
#              |-D1--D2--D3-|
#              |------------|
#              |-D4--D5--D6-|
#              |------------|
#              |-D7--D8--D9-|
#              |------------|

solved_state_string = "YYYYYYYYYOOOOOOOOOGGGGGGGGGWWWWWWWWWRRRRRRRRRBBBBBBBBB"


Solved_state = [
    [
        ["Y1", "Y2", "Y3"],  # [0][0]
        ["Y4", "Y5", "Y6"],  # [0][1]
        ["Y7", "Y8", "Y9"]  # [0][2]
    ],
    [
        ["O1", "O2", "O3"],  # [1][0]
        ["O4", "O5", "O6"],  # [1][1]
        ["O7", "O8", "O9"]  # [1][2]
    ],
    [
        ["G1", "G2", "G3"],  # [2][0]
        ["G4", "G5", "G6"],  # [2][1]
        ["G7", "G8", "G9"]  # [2][2]
    ],
    [
        ["W1", "W2", "W3"],  # [3][0]
        ["W4", "W5", "W6"],  # [3][1]
        ["W7", "W8", "W9"]  # [3][2]
    ],
    [
        ["R1", "R2", "R3"],  # [4][0]
        ["R4", "R5", "R6"],  # [4][1]
        ["R7", "R8", "R9"]  # [4][2]
    ],
    [
        ["B1", "B2", "B3"],  # [5][0]
        ["B4", "B5", "B6"],  # [5][1]
        ["B7", "B8", "B9"]  # [5][2]
    ]
]

Unsolved_cube = Solved_state
scramble_arr = ["R'", 'D', 'R', 'U2', 'B2', 'U', 'D2', 'B', 'L2',"R'", 'B2', 'R', 'B2', 'D2', 'L2', 'F2', 'D2', 'L', 'B2', 'L']

# scramble_arr = scramble.scrambler()


print("Scramble is: \n", " ".join(scramble_arr), "\n")
for i in scramble_arr:
    move.moves_dict[i](Unsolved_cube)


for i in range(3):
    for j in range(6):
        print(Unsolved_cube[j][i], end=" ")
    print()


solve.solveCube(Unsolved_cube, Solved_state)
