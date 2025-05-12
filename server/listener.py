import socket

def start_listener(host, port):
    # Create a socket object
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)
    print(f"[*] Listening on {host}:{port}...")

    while True:
        client_socket, client_address = server.accept()
        print(f"[*] Connection from {client_address} has been established!")

        # Get and send data from server to client
        while True:
            command = input("Shell> ")

            if command.lower() == 'exit':
                client_socket.send(b'exit') # Close the connection
                break

            if command:
                client_socket.send(command.encode()) # Send the command
                response = client_socket.recv(4096).decode() # Receive the response
                print(response) # Print the response
            
            client_socket.close()

if __name__ == "__main__":
    start_listener('0.0.0.0', 9999) # deafult server port(9999)