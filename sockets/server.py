import socket
import threading


def handle_client(client_socket, addr):
    # Function to handle each client connection
    print(f"Accepted connection from {addr}")

    while True:
        data = client_socket.recv(1024)
        if not data:
            break

        message = data.decode('utf-8')
        print(f"Received from {addr}: {message}")

        # Echo the message back to the client
        client_socket.send(data)

    print(f"Connection with {addr} closed")
    client_socket.close()


def main():
    host = socket.gethostname()
    port = 8000

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)

    print(f"Server listening on {host}:{port}")

    while True:
        client_socket, client_address = server_socket.accept()

        # Create a new thread for each client
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()


if __name__ == "__main__":
    main()
