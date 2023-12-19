import socket

def main():
    host = '127.0.0.1'
    port = 1234

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    client_socket.sendto('get_time'.encode('utf-8'), (host, port))
    response, _ = client_socket.recvfrom(1024)

    print(f"[*] Hora atual: {response.decode('utf-8')}")

    client_socket.close()

if __name__ == "__main__":
    main()
