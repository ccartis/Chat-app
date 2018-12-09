import socket
import sys
import time

s=socket.socket()
# socket.getaddrinfo('localhost', 8080)

host=input(str("Please enter the hostname of the server: "))
port=8080
s.connect((host,port))
print("Connecting to the chat server")
while 1:
    incoming_message=s.recv(1024)

    #now we need to decode the incoming_message
    incoming_message=incoming_message.decode()
    print("Server: ",incoming_message)
    print("")
    message=input(str(">>"))
    message=message.encode()
    s.send(message)
    print("message has been sent")
    print(" ")
