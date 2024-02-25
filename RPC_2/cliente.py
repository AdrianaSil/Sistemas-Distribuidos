import xmlrpc.client
import socket

server = xmlrpc.client.ServerProxy('http://10.0.84.199:21212')

server.salvar("Teste")
print(server.getMsgs())
print(server.getServerIP())
print(server.getServerDateTime())

print(server.system.listMethods())
