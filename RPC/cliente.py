import xmlrpc.client

def main():

    #Conecta ao servidor local
    local_server = xmlrpc.client.ServerProxy('http://localhost:1234/RPC2')
   
    #Acessa funções do servidor local
    print("[*] Servidor local:")
    print("Data | Hora:", local_server.get_current_datetime())
    print("Qtd de chamadas recebidas:", local_server.get_call_count())

if __name__ == "__main__":
    main()