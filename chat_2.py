# client.py
import socket
import threading

# Server details
HOST = '127.0.0.1'  # Localhost
PORT = 65432        # Same port as the server

# Function to handle receiving messages
def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(message)
            else:
                break
        except:
            # Disconnect in case of an error
            print("[ERROR] An error occurred.")
            client_socket.close()
            break

# Main function to connect to server and send messages
def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))
    
    # Start a thread to listen for messages
    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.start()
    
    print("[CONNECTED] Type messages to send. Type 'exit' to disconnect.")
    
    while True:
        message = input()
        
        if message.lower() == 'exit':
            client_socket.send("User has left the chat.".encode('utf-8'))
            break
        
        client_socket.send(message.encode('utf-8'))
    
    client_socket.close()
    print("[DISCONNECTED] You have disconnected.")

if __name__ == "__main__":
    start_client()
