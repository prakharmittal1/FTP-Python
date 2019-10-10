from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer


authorizer = DummyAuthorizer()

authorizer.add_user("prakhar", "prakhar", "D:\Demo", perm="elradfmwMT")
authorizer.add_user("mittal", "mittal", "D:\Demo", perm="elradfmwMT")

authorizer.add_anonymous("D:\Demo") #path of the directory you want to the clients to access
handler = FTPHandler
handler.authorizer = authorizer
server = FTPServer(("172.16.105.58", 21), handler) #the IP address of your system, the one which is the server
server.serve_forever()
