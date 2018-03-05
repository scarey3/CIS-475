import socket

HOST = '127.0.0.1'
PORT = 50000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Connect to the server
    s.connect((HOST, PORT))
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    while True:
        # Read a sequence of characters from the user
        message = input('Input sentence: ')

        # Send input to server
        s.sendall(message.encode('utf-8'))
        print('Sent', '\'' + message + '\'', 'on port', s.getsockname()[1], 'to server', s.getpeername())

        if message == 'exit': break

        # Receive digest from server
        data = s.recv(1024)
        print('Received digest', '\'' + data.decode('utf-8') + '\'', 'on port', s.getsockname()[1], 'from server', )

    s.close()