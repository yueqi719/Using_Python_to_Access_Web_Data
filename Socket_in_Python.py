import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#actually make the connection
mysock.connect(('data.pr4e.org',80)) #link is the host, 80 is the port