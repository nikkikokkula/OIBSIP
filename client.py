import socket

host = "127.0.0.1"
port = 5000

client = socket.socket()
client.connect((host, port))

print("Connected to server")

while True:
    msg = input("You (Client): ")
    client.send(msg.encode())

    if msg.lower() == "exit":
        print("You ended the chat.")
        break

    reply = client.recv(1024).decode()

    if not reply:
        print("Server disconnected.")
        break

    print("Server:", reply)

    if reply.lower() == "exit":
        print("Server ended the chat.")
        break

client.close()
   
        