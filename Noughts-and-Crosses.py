# Project Noughts and Crosses
# square designations / variables
s1 = '1'
s2 = '2'
s3 = '3'
s4 = '4'
s5 = '0'
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

    if 'x' == '9':
        s3 = '0'
    if 'x' == '7':
        s1 = '0'
    #if 'x' == '5':
        #s5 = '0'
    if 'x' == '1':
        s4 = '0'
    if 'x' == '2':
        s8 = '0'
    if 'x' == '3':
        s6 = '0'
    if 'x' == '4':
        s7 = '0'
    if 'x' == '6':
        s2 = '0'
    #if 'x' == '8':
        #s8 = '0'
