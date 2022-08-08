# https://docs.python.org/3.4/howto/sockets.html
# https://docs.python.org/3/howto/sockets.html
# https://docs.python.org/3/library/socket.html
# Computer Networking: A Top-Down Approach, 7th Edition

import socket

port = 50050

# The client creates a socket and connects to 'localhost' and port xxxx
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.connect(("localhost", port))

print("Connected to: localhost on port: ", port)
print("Type /q to quit")
print("Enter message to send...")
# Back to step 2
while(1):
    # When connected, the client prompts for a message to send
    data = input("Client> ")
    # The client sends the message
    soc.send(data.encode())
    # If the message is /q, the client quits
    if data == "/q":
        # sclose socket and program is executed
        soc.close()
        break
    # The client calls recv to receive data
    data = soc.recv(1024).decode()
    print("Server>",data)

