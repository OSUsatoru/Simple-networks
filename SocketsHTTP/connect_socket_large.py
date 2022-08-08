# Refference
# -For socket API functions and methods
# https://realpython.com/python-sockets/#socket-api-overview
# https://docs.python.org/3/howto/sockets.html
# https://docs.python.org/3/library/socket.html
# Computer Networking: A Top-Down Approach, 7th Edition

# -For HTTP port number
# https://en.wikipedia.org/wiki/Port_(computer_networking)

# This program receive packets of size 1024 until no response

import socket

target_host = "gaia.cs.umass.edu"

# This port number is for HTTP
target_port = 80
# create a socket object
# AF_INET: IPv4
# SOCK_STREAM (TCP): conversation with two parties
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the client
client.connect((target_host,target_port))

# send request
request = "GET /wireshark-labs/HTTP-wireshark-file3.html HTTP/1.1\r\nHost:gaia.cs.umass.edu\r\n\r\n"
client.send(request.encode())
print("Request: %s" %request)

sum_response = ''
# each loop reveive one packet of size 1024
while True:

    #size of one packet
    response = client.recv(1024)

    # if there is no responsem, break while loop
    if not response:
        break
    # add response to sum_respons
    sum_response=sum_response+response.decode()

# length of sum_respons
sum_http_response_len = len(sum_response)
# display the sum_respons
print("[RECV] - length: %d" % sum_http_response_len)
print(sum_response)