import socket

from netTools import *
import threading
import time
import random

html = """<!DOCTYPE html>
<html>
<head> <title>Simple Server</title>
</head>
<body> 
**Content**
</body>
</html>
"""


class Server:
    addr = "0.0.0.0"

    def __init__(self):
        self.host = getIPAddress()
        self.port = 8080


    def run(self):
        # Open socket
        serversocket = socket()
        serversocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        print("Listening on: ", self.host, ":", self.port)
        serversocket.bind((self.host, self.port))
        serversocket.listen()

        while True:
            print("Waiting for connection....")
            clientsocket, addr = serversocket.accept()
            print("Connnection from", addr)
            threading.Thread(target=self.processRequest, args=(clientsocket,)).start()

        serversocket.close()

    def processRequest(self, cl):
        request = getMessage(cl)
        print("*" * 50, "\nNew Request\n", "*" * 50)

        resource = request.split(" ")[1]
        print(resource)
        if request[:3] == "GET":
            print("GET:" + resource)
            if resource == "/":
                homePage = html.replace("**Content**", "<h1> Simple Server </h1>")
                self.respondHTML(homePage, cl)
            elif resource[-4:].lower() == "html":
                try:
                    with open(resource, "r") as inFile:
                        response = inFile.read()
                    self.respondHTML(response, cl)
                except FileNotFoundError:
                    self.respondNotFound(cl)
            elif resource[-3:].lower() == "png":
                self.respondImg(resource, cl)

        

    def respondHTML(self, body, cl):
        header = 'HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n'
        sendMessage(cl, header)
        sendMessage(cl, body)
        cl.close()

    def respondImg(self, resource, cl):
        header = "HTTP/1.0 200 OK\r\n"
        header += "Content-Type: image/png\r\n"
        header += "\r\n"
        try:
            resource = "Image" + resource
            print("Resource: \n", resource)
            infile = open(resource, "rb")
            data = infile.read()
            infile.close()
            sendMessage(cl, header)
            cl.send(data)
            cl.close()
            print("Sent")

        except FileNotFoundError:
            print("bosh", resource)
            self.respondHTML(resource, cl)


    def respondNotFound(self,cl):
        header = "HTTP/1.0 404 NOT FOUND\r\n\r\n"
        body = homePage = html.replace("**Content**", "<h1> NOT FOUND </h1>")
        sendMessage(cl, header)
        sendMessage(cl, body)

        cl.close()
        print("Not Found")

s = Server()
s.run()