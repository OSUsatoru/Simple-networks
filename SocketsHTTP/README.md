## Connect Socket
How do internet browsers work? They all manage networking “sockets” to contact a web
server and download HTML files and resources. In this part you will make a bare-bones
socket program to do some of what your internet browser does.
Create a simple python program that uses a socket to interact with a server.

Your program shall make a socket connection to the host: “gaia.cs.umass.edu” and send
the GET request for the URI: “/wireshark-labs/INTRO-wireshark-file1.html”.

## Command
```sh
python connect_socket.py
```

## Connect Socket Large
Write a socket program to receive arbitrarily large files.

Your program will make a socket connection to the host: “gaia.cs.umass.edu” and send the
GET request for the URI: “/wireshark-labs/HTTP-wireshark-file3.html”.

## Command
```sh
python connect_socket_large.py
```

## http server
Create an HTTP server using the python socket api. Your program
will create a listening socket bound to ‘127.0.0.1’ or ‘localhost’, and a random port
number > 1023. You will then use your web browser to connect to your server and
receive data.
### URL
http://127.0.0.1:1023/

## Command
```sh
python http_server.py
```
