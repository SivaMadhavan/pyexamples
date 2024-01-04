import socket


def main():
    host = socket.gethostname()  # since both client and server are running in the same machine
    port = 8000

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    print(f"Connection established with the {host}:{port}")
    print("Enter message here : \n")
    while True:
        data = input()
        if not data:
            break
        client_socket.send(data.encode('utf-8'))

        data = client_socket.recv(1024)
        print(f"Received from server: {data.decode('utf-8')}")

    # Close the connection
    client_socket.close()
    print(f"Connection closed!")


if __name__ == "__main__":
    main()
