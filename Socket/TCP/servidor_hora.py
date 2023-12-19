import socket
import threading
from datetime import datetime

def conexao_cliente(client_socket):

    request = client_socket.recv(1024).decode('utf-8')

    if request == 'get_time':
        current_time = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        client_socket.send(current_time.encode('utf-8'))

    client_socket.close()

def main():
    host = '127.0.0.1'
    port = 1234

    # Cria socket  TCP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #Conecta socket ao endereço
    server_address = (host, port) 
    print("Servidor: Conectando %s porta %s" % server_address)
    #Reservando porta
    sock.bind(server_address)
    #Escutando 
    sock.listen(1)

    print(f"[*] Escutando em {host}:{port}")

    while True:
        client, addr = sock.accept()
        print(f"[*] Conexão aceita  {addr[0]}:{addr[1]}")

        conexao = threading.Thread(target=conexao_cliente, args=(client,))
        conexao.start()

if __name__ == "__main__":
    main()
