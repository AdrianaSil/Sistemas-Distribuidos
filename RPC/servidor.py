from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import datetime

# Restringe as conexões ao localhost
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Implementa as funções do servidor
class RPC_functions:
    def __init__(self):
        self.call_count = 0

    def get_current_datetime(self):
        self.call_count += 1
        return datetime.datetime.now().strftime('%d-%m-%Y | %H:%M:%S')

    def get_call_count(self):
        return self.call_count

def main():
    host = 'localhost'
    port = 1234

    # Configura e inicia o servidor
    server = SimpleXMLRPCServer((host, port), requestHandler=RequestHandler)
    server.register_introspection_functions()

    #Adiciona as funções do servidor
    server.register_instance(RPC_functions())

    print(f"[*] Servidor RPC iniciado em {host}:{port}...")
    server.serve_forever()

if __name__ == "__main__":
    main()
