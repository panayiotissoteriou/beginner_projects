board = {'0':' ','1' : ' ', '2': ' ', '3':' ', '4': ' ', '5':' ', '6' : ' ', '7': ' ', '8':' ', '9':' '}

def BoardPrint(board):          # function that prints board
#making the board.keys() into a list
    entries_lst = []
    for i in board.values():
        entries_lst.append(i)

    line1 = ''
    line2 = ''
    line3 = ''
    for i in range(len(entries_lst)):
        if 1 <= i <=3 :
            line1 += entries_lst[i]
        if 4<= i <=6:
            line2 += entries_lst[i]
        if 7<= i <=9:
            line3 += entries_lst[i]

    line1 = (" | ".join(line1))
    line2 = (" | ".join(line2))
    line3 = (" | ".join(line3))
    line1 += ' '
    line2 += ' '
    line3 += ' '
    print("\u0332".join(line1))
    print("\u0332".join(line2))
    print(line3, '\n')

print('\n'+'Choose a position from 1-9 to insert O or X. Type exit to quit.', '\n')
BoardPrint(board)

def winning_function(list):
    winning_positions = [('1','2','3'), ('1','5','9'), ('1', '4', '7'), ('2', '5', '8'), ('3', '5', '7'), ('3', '6', '9'), ('4', '5', '6'), ('7', '8', '9')]
    list.sort()

    import itertools

    combos_list = []
    new_list = []
    for i in range(len(list)+1):
        for combos in itertools.combinations(list, i):
            combos_list.append(combos)
#print(combos_list)

    for i in combos_list:
        if len(i) == 3:
            new_list.append(i)
#print(new_list)

    for i in new_list:
        if i in winning_positions:
            return 'win'

def tictactoe():
    turn = 0
    x_list = []
    o_list = []
    board = {'0':' ','1' : ' ', '2': ' ', '3':' ', '4': ' ', '5':' ', '6' : ' ', '7': ' ', '8':' ', '9':' '}
    for i in board:
        if ' ' in board[i]:
            while ' ' in board[i]:
                if int(turn) == 9:
                    print("It's a draw!", '\n')
                    return

                elif int(turn) % 2 == 0:
                    player_1_input = str(input('input O position: '))
                #exit
                    if player_1_input == 'exit':
                        return

                #is.numeric test
                    if player_1_input.isnumeric() == False:
                        print('You must type a number.', '\n')
                        continue
                # number between 0-8
                    intg_P1 = int(player_1_input)
                    if 1 > intg_P1 or intg_P1 > 9:
                        print('You must type a number from 1-9.', '\n')
                        continue

                    if player_1_input not in x_list:
                        o_list.append(player_1_input)
                    else:
                        print('Position already taken. Type a different position.', '\n')
                        continue

                    turn += 1
                #print(o_list)
                    board[player_1_input] = 'O'
                    BoardPrint(board)

                    if winning_function(o_list) == 'win':
                        print('Win!', '\n')
                        return


                elif int(turn) % 2 == 1:
                    player_2_input = str(input('input X position: '))
                #exit
                    if player_2_input == 'exit':
                        return
                #is.numeric test
                    if player_2_input.isnumeric() == False:
                        print('You must type a number.', '\n')
                        continue
                #number between 1-9
                    intg_P2 = int(player_2_input)
                    if 1 > intg_P2 or intg_P2 > 9:
                        print('You must type a number from 1-9.', '\n')
                        continue

                    if player_2_input not in o_list:
                        x_list.append(player_2_input)
                    else:
                        print('Position already taken. Type a different position.', '\n')
                        continue

                    turn += 1
                    x_list.append(player_2_input)

                    board[player_2_input] = 'X'
                    BoardPrint(board)
                    if winning_function(x_list) == 'win':
                        print('Win!', '\n')           
                        return

tictactoe()
