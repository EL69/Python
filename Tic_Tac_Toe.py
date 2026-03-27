# Project Noughts and Crosses
# square designations / variables
s1 = '1'
s2 = '2'
s3 = '3'
s4 = '4'
s5 = '5'
s6 = '6'
s7 = '7'
s8 = '8'
s9 = '9'

while True:
    print(f"|__{s1}__|__{s2}__|__{s3}__|")
    print(f"|__{s4}__|__{s5}__|__{s6}__|")
    print(f"|  {s7}  |  {s8}  |  {s9}  |")
    print()

    move = input('What is your move: ')

    if move == '1':
        s1 = 'x'
    if move == '2':
        s2 = 'x'
    if move == '3':
        s3 = 'x'
    if move == '4':
        s4 = 'x'
    if move == '5':
        s5 = 'x'
    if move == '6':
        s6 = 'x'
    if move == '7':
        s7 = 'x'
    if move == '8':
        s8 = 'x'
    if move == '9':
        s9 = 'x'

    # Computer move (simple: first available square)

    if s1 not in ['x', '0']:
        s1 = '0'
    elif s2 not in ['x', '0']:
        s2 = '0'
    elif s3 not in ['x', '0']:
        s3 = '0'
    elif s4 not in ['x', '0']:
        s4 = '0'
    elif s5 not in ['x', '0']:
        s5 = '0'
    elif s6 not in ['x', '0']:
        s6 = '0'
    elif s7 not in ['x', '0']:
        s7 = '0'
    elif s8 not in ['x', '0']:
        s8 = '0'
    elif s9 not in ['x', '0']:
        s9 = '0'

    # After computer move logic
    print(f"|__{s1}__|__{s2}__|__{s3}__|")
    print(f"|__{s4}__|__{s5}__|__{s6}__|")
    print(f"|  {s7}  |  {s8}  |  {s9}  |")
    print()


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

    continue  # Go to the next loop iteration



        # Set the correct variable to '0'
        # (You need to check which variable it is and update it)
    break
