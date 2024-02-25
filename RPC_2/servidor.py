from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
from datetime import datetime

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

with SimpleXMLRPCServer(('10.0.84.199', 21212), requestHandler=RequestHandler) as server:
    server.register_introspection_functions()

    mensagens = []

    def getServerIP():
        return server.server_address[0]

    def salvar(msg):
        mensagens.append(msg)
        return True

    def getMsgs():
        return mensagens

    def getServerDateTime():
        now = datetime.now()
        formatted_date_time = now.strftime("%Y-%m-%d %H:%M")
        return formatted_date_time

    def clearMsg():
        mensagens.clear()
        return True

    server.register_function(getServerIP, 'Get Server IP')
    server.register_function(salvar, 'Salvar msg')
    server.register_function(getMsgs, 'Get msg')
    server.register_function(getServerDateTime, 'Get DateTime')
    server.register_function(clearMsg, 'Clear msgs')

    server.serve_forever()
