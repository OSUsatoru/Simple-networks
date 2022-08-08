# https://docs.python.org/3.4/howto/sockets.html
# https://docs.python.org/3/howto/sockets.html
# https://docs.python.org/3/library/socket.html
# Computer Networking: A Top-Down Approach, 7th Edition
# https://jtwp470.hatenablog.jp/entry/2016/03/30/000802

import socket

def print_board(board):
    print("{0:^3}|{1:^3}|{2:^3}".format(board[0], board[1], board[2]))
    print("---+---+---")
    print("{0:^3}|{1:^3}|{2:^3}".format(board[3], board[4], board[5]))
    print("---+---+---")
    print("{0:^3}|{1:^3}|{2:^3}".format(board[6], board[7], board[8]))
    print("")
# return 2 for client, retunr 1 for server. otherwise 0
def is_game(board):
    for i in range(3):
        if( board[i] == 'X' and board[i+1] == 'X' and board[i+2] == 'X' or
            board[i] == 'X' and board[i+3] == 'X' and board[i+6] == 'X'):
            return 1
        if( board[i] == 'O' and board[i+1] == 'O' and board[i+2] == 'O' or
            board[i] == 'O' and board[i+3] == 'O' and board[i+6] == 'O'):
            return 2
    if( board[0] == 'X' and board[4] == 'X' and board[8] == 'X' or
        board[2] == 'X' and board[4] == 'X' and board[6] == 'X'):
        return 1
    if( board[0] == 'O' and board[4] == 'O' and board[8] == 'O' or
        board[2] == 'O' and board[4] == 'O' and board[6] == 'O' ):
        return 2
    return 0

port = 50050
ini_message = "Welcome to 3*3 Tic-tac-toe!, Enter the number(1 - 9)"

# Create a socket and binds to localhost and port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("localhost", 50050))
print("Server listening on: localhost on port: 50050")
# There is only one socket fconnection
s.listen(1)


# Accept
soc, addr = s.accept()
print("Conneted by"+str(addr))
# send initial message
data = soc.send(ini_message.encode())

game_board = [''] * 9

while (1):

    data = soc.recv(1024).decode()
    # If the reply is /q, the server quits
    if data == "/q":
        print("Client quit\n")
        # close socket
        soc.close()
        break

    num = int(data)

    game_board[num-1] = 'O'

    # Display game screen
    print_board(game_board)
    # check if game is over
    if is_game(game_board) == 2:
        print("Client won!")
        soc.close()
        break

    # If there is no space
    if ('' in game_board) == False:
        print("Tie!")
        soc.close()
        break
    while(True):
        data = input("Server> ")
        num = int(data)
        if game_board[num-1] == '':
            game_board[num-1] = 'X'
            break

    soc.send(data.encode())

    print_board(game_board)
    if is_game(game_board) == 1:
        print("Server won!")
        soc.close()
        break
    if ('' in game_board) == False:
        print("Tie!")
        soc.close()
        break



# close the main socket
s.close()