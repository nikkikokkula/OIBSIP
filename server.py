import socket

def start_server():
    host = "127.0.0.1"
    port = 5000

    server = socket.socket()
    server.bind((host, port))
    server.listen()

    print("Server started. Waiting for connection...")

    conn, addr = server.accept()
    print("Client connected:", addr)

    while True:
        msg = conn.recv(1024).decode()

        if not msg:
            print("Client disconnected.")
            break

        print("User:", msg)

        if msg.lower() == "exit":
            print("User ended the chat.")
            break

        reply = input("Nikhita (Server): ")
        conn.send(reply.encode())

        if reply.lower() == "exit":
            print("You ended the chat.")
            break

    conn.close()
    server.close()

if __name__ == "__main__":
   start_server()