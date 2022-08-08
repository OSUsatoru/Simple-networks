# Refference
# -For socket API functions and methods
# https://realpython.com/python-sockets/#socket-api-overview
# https://docs.python.org/3/howto/sockets.html
# https://docs.python.org/3/library/socket.html
# Computer Networking: A Top-Down Approach, 7th Edition

# This creates new socket and read the request on that and print
# then send the data on the new socket and close it
# NOTE: I am not using while loop for this assignemt
#       I create a socket once

import socket


IP = '127.0.0.1'
PORT = 1023

# TCP Client
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# associate the server IP, PORT with this socket
serverSocket.bind((IP, PORT))
# maximum number of queued connections
serverSocket.listen(1)

data = "HTTP/1.1 200 OK\r\n"\
 "Content-Type: text/html; charset=UTF-8\r\n\r\n"\
 "<html>Congratulations! You've downloaded the first Wireshark lab file!</html>\r\n"


# create new socket in the server
connectionSocket, addr = serverSocket.accept()

print("Connected by", addr, "\n")

# receive the data from new socket
reveive = connectionSocket.recv(8192)
print("Received: %s" %reveive)

print("\nSending>>>>>>>>\n%s" %data)
# send the data to new socket
connectionSocket.send(data.encode())
print("<<<<<<<<")
# close the new socket
connectionSocket.close()