import multiprocessing
import socket

def client_function(message_queue, message):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 12345)

    try:
        client_socket.connect(server_address)
        client_socket.send(message.encode())
        response = client_socket.recv(1024).decode()
        print(f"Received response from server: {response}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client_socket.close()

if __name__ == "__main__":
    message_queue = multiprocessing.Queue()

  
    messages = ["Hello, server!", "How are you?", "Goodbye!"]

    client_processes = []
    for message in messages:
        process = multiprocessing.Process(target=client_function, args=(message_queue, message))
        process.start()
        client_processes.append(process)

    for process in client_processes:
        process.join()
