# Project Noughts and Crosses
# square designations / variables
# Initialize squares
s1 = '1'
s2 = '2'
s3 = '3'
s4 = '4'
s5 = '5'
s6 = '6'
s7 = '7'
s8 = '8'
s9 = '9'

def print_board():
    print(f"|__{s1}__|__{s2}__|__{s3}__|")
    print(f"|__{s4}__|__{s5}__|__{s6}__|")
    print(f"|__{s7}__|__{s8}__|__{s9}__|")
    print()

while True:
    print_board()

    # Player move
    move = input('What is your move: ')
    if move == '1' and s1 not in ['x', '0']:
        s1 = 'x'
    elif move == '2' and s2 not in ['x', '0']:
        s2 = 'x'
    elif move == '3' and s3 not in ['x', '0']:
        s3 = 'x'
    elif move == '4' and s4 not in ['x', '0']:
        s4 = 'x'
    elif move == '5' and s5 not in ['x', '0']:
        s5 = 'x'
    elif move == '6' and s6 not in ['x', '0']:
        s6 = 'x'
    elif move == '7' and s7 not in ['x', '0']:
        s7 = 'x'
    elif move == '8' and s8 not in ['x', '0']:
        s8 = 'x'
    elif move == '9' and s9 not in ['x', '0']:
        s9 = 'x'
    else:
        print("That square is already taken. Try again.")
        continue

    # Check for player win/draw
    
    wins = [
    [s1, s2, s3],
    [s4, s5, s6],
    [s7, s8, s9],
    [s1, s4, s7],
    [s2, s5, s8],
    [s3, s6, s9],
    [s1, s5, s9],
    [s3, s5, s7]
]

    for combo in wins:
        if combo == ['x', 'x', 'x']:
            print("Player wins!")
            break

        if combo == ['0', '0', '0']:
            print("Computer wins!")
            break

        if all(square in ['x', '0'] for square in [s1, s2, s3, s4, s5, s6, s7, s8, s9]):
            print("Draw!")
            break
