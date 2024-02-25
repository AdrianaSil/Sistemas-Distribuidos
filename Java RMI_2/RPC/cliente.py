import xmlrpc.client
import socket

s = xmlrpc.client.ServerProxy('http://localhost:21212')

print(s.add(2,3))
s.salvar(socket.gethostname())
s.salvar("Teste")
print(s.getMsg())

print(s.system.listMethods())
