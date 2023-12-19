import socket
from datetime import datetime

def main():
    host = '127.0.0.1'
    port = 1234

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host, port))

    print(f"[*] Escutando em {host}:{port}")

    while True:
        data, addr = server_socket.recvfrom(1024)
        request = data.decode('utf-8')

        if request == 'get_time':
            current_time = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
            server_socket.sendto(current_time.encode('utf-8'), addr)

if __name__ == "__main__":
    main()
