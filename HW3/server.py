import socket

# Server and client run on the same host, so only accept local connections
HOST = '127.0.0.1'
PORT = 50000

def digest(data):
    digest = 0
    for i in data:
        digest += i
    return digest

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen(1)

        # Wait for a connection from a new client
        while True:
            conn, addr = s.accept()
            with conn:
                while True:
                    # Receive data from the client
                    data = conn.recv(1024)

                    # If no data is read or data is 'exit', break loop
                    if (not data) or (data.decode('utf-8') == 'exit'): 
                        break

                    # Calculate and print digest
                    result = str(digest(data))
                    print('client', addr, 'sent', '\'' + data.decode('utf-8') + '\'', 'and we sent back', result)

                    # Send the digest to the client
                    conn.sendall(result.encode('utf-8'))

if __name__ == '__main__':
    main()