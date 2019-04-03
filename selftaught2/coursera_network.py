# send and receive data using sockets
# network layered architecture
# application, transport, internet, network
# write program to communicate with transport layer
# communication between two applications
# the connection is called a socket
# applications associate themselves with ports
# port 80 is web port and 443 is the secure server

# built in support for TCP sockets

# import socket


# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#       //creates socket or endpoint on computer
# mysock.connect( ('data.pr4e.org', 80) )
#       //creates connection to domain on port 80 using file handle
# every time user clicks anchor tag with an href= value to switch
# new page browser connects to server issues a 'get' request to port 80
# called the request response cycle
# telnet used to connect to server and port
# http sends back metadata
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))  # create mysock object connect to domain
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
#  .encode converst unicode to utf8
mysock.send(cmd)  # send get request

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode())  # decode converst to unicode

mysock.close()
