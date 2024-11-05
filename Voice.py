# server.py
import socket
import threading

# Server details
HOST = '127.0.0.1'  # Localhost
PORT = 65432        # Port to listen on

# List to hold connected client sockets
clients = []

# Function to handle incoming messages and relay to other client
def handle_client(client_socket, client_address):
    print(f"[NEW CONNECTION] {client_address} connected.")
    
    while True:
        try:
            # Receive message from client
            message = client_socket.recv(1024).decode('utf-8')
            
            if not message:  # Client disconnected
                break
            
            print(f"[{client_address}] {message}")
            
            # Send the message to the other client
            for client in clients:
                if client != client_socket:
                    client.send(f"[{client_address}] {message}".encode('utf-8'))
        except:
            # Remove client if an error occurs
            clients.remove(client_socket)
            client_socket.close()
            break
    
    print(f"[DISCONNECT] {client_address} disconnected.")
    clients.remove(client_socket)
    client_socket.close()

# Main function to start the server
def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(2)  # Server listening for 2 clients
    
    print(f"[STARTING] Server is starting on {HOST}:{PORT}")
    
    while True:
        client_socket, client_address = server.accept()
        clients.append(client_socket)
        
        # Start a new thread to handle the client
        thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        thread.start()
        
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

if __name__ == "__main__":
    start_server()
