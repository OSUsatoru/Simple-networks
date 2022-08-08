# Refference
# -For socket API functions and methods
# https://realpython.com/python-sockets/#socket-api-overview
# https://docs.python.org/3/howto/sockets.html
# https://docs.python.org/3/library/socket.html
# Computer Networking: A Top-Down Approach, 7th Edition

# -For HTTP port number
# https://en.wikipedia.org/wiki/Port_(computer_networking)

# This program only reveive one packet of size 1024
# And I assume that TA test this program for packet data less than 1024

import socket

target_host = "gaia.cs.umass.edu"

#This port number is for HTTP
target_port = 80
# create a socket object
# AF_INET: IPv4
# SOCK_STREAM (TCP): conversation with two parties
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the client
client.connect((target_host,target_port))

# send some data
request = "GET /wireshark-labs/INTRO-wireshark-file1.html HTTP/1.1\r\nHost:gaia.cs.umass.edu\r\n\r\n"
client.send(request.encode())
print("Request: %s" %request)

#size of packet
response = client.recv(1024)

#the length of response
http_response_len = len(response)

#display the response
print("[RECV] - length: %d" % http_response_len)
print(response.decode())