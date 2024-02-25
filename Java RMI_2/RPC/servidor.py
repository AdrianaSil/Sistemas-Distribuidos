from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

# Registrar caminho para o servidor
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Create server
with SimpleXMLRPCServer(('localhost', 21212),requestHandler=RequestHandler) as server:
    server.register_introspection_functions()

    #Definição de funções
    def adder_function(x, y):
        return x + y
    
    mensagens = []
    
    def salvar(msg):
        mensagens.append(msg)
        return (True)
    
    def getMsg():
        return(mensagens)
    
    def prime(n):
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2
        return True
    
    #Registrar funções
    server.register_function(adder_function, 'add')
    server.register_function(prime, 'prime')
    server.register_function(salvar, 'armazenar')
    server.register_function(getMsg, 'getMensagens')

    # Iniciar servidor
    server.serve_forever()