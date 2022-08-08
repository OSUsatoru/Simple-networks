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

# The client creates a socket and connects to 'localhost' and port xxxx
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.connect(("localhost", port))

print("Connected to: localhost on port: ", port)
print("Type /q to quit")

# recv initial message
data = soc.recv(1024).decode()
print("Server>",data)

game_board = [''] * 9

quit = 0

while(1):

    # Input
    while(True):
        data = input("Client> ")
        # If the message is /q, the client quits
        if data == "/q":
            soc.send(data.encode())
            # sclose socket and program is executed
            quit = 1
            soc.close()
            break

        num = int(data)
        if game_board[num-1] == '':
            game_board[num-1] = 'O'
            break
    if quit:
        break
    # send the data
    soc.send(data.encode())

    # Display game screen
    print_board(game_board)
    # check if game is over
    if is_game(game_board) == 2:
        print("Client won!")
        soc.close()
        break

    if ('' in game_board) == False:
        print("Tie!")
        soc.close()
        break

    # The client calls recv to receive data
    data = soc.recv(1024).decode()
    num = int(data)
    game_board[num-1] = 'X'

    print_board(game_board)
    if is_game(game_board) == 1:
        print("Server won!")
        soc.close()
        break
    if ('' in game_board) == False:
        print("Tie!")
        soc.close()
        break

