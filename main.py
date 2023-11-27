import scramble as scramble

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

solved_state_sring = "YYYYYYYYYOOOOOOOOOGGGGGGGGGWWWWWWWWWRRRRRRRRRBBBBBBBBB"


Solved_state = [
    [
        "Y","Y","Y",
        "Y","Y","Y",
        "Y","Y","Y"
    ],
    [
        "O","O","O",
        "O","O","O",
        "O","O","O"
    ],
    [
        "G","G","G",
        "G","G","G",
        "G","G","G"
    ],
    [
        "W","W","W",
        "W","W","W",
        "W","W","W"
    ],
    [
        "R","R","R",
        "R","R","R",
        "R","R","R"
    ],
    [
        "B","B","B",
        "B","B","B",
        "B","B","B"
    ]
]

moves_list = [
    "U","U'","U2","D","D'","D2",
    "R","R'","R2","L","L'","L2",
    "F","F'","F2","B","B'","B2"
]

print(scramble.scrambler(moves_list))