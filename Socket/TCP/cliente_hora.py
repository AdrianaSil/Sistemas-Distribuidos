import socket

def main():
    host = '127.0.0.1'
    port = 1234

    # Cria socket TCP
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Conectar socket ao endereço para estabelecer conexão com o servidor
    client_address = (host, port) 
    print("Conectando %s porta %s" % client_address) 
    sock.connect(client_address)

    #Enviando e recebendo pacote
    sock.send('get_time'.encode('utf-8'))
    response = sock.recv(1024).decode('utf-8')

    print(f"[*] Hora atual: {response}")

    sock.close()

if __name__ == "__main__":
    main()