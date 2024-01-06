import multiprocessing
import socket

def handle_client(client_socket, message_queue):
    while True:
        data = client_socket.recv(1024).decode()
        if not data:
            break
        print(f"Received message from client: {data}")

        message_queue.put(data)

        response = f"Server received: {data}"
        client_socket.send(response.encode())
    client_socket.close()

def start_server(message_queue):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 12345)
    server_socket.bind(server_address)
    server_socket.listen(5)

    print("Server is waiting for connections...")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connected to {client_address}")

        client_handler = multiprocessing.Process(target=handle_client, args=(client_socket, message_queue))
        client_handler.start()

if __name__ == "__main__":
    message_queue = multiprocessing.Queue()

    # Start the server process
    server_process = multiprocessing.Process(target=start_server, args=(message_queue,))
    server_process.start()
