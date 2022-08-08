# https://docs.python.org/3.4/howto/sockets.html
# https://docs.python.org/3/howto/sockets.html
# https://docs.python.org/3/library/socket.html
# Computer Networking: A Top-Down Approach, 7th Edition

import socket

port = 50050
# Create a socket and binds to localhost and port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("localhost", 50050))
print("Server listening on: localhost on port: 50050")
# There is only one socket fconnection
s.listen(1)


# Accept
soc, addr = s.accept()
print("Conneted by"+str(addr))

print("Waiting for message...")
# Back to step 3
while (1):
    # WheUn connected, the server calls recv to receive data
    data = soc.recv(1024).decode()
    # If the reply is /q, the server quits
    if data == "/q":
        print("Client quit\n")
        # close socket and wait for new connection
        soc.close()
        break
    # The server prints the data, then prompts for a reply
    print("Client>", data)
    # The server sends the reply
    data = input("Server> ")
    soc.send(data.encode())

# close the main socket
s.close()


