import socket,requests
try:
    server_address =  ('127.0.0.1', 8374)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(server_address)
    s.listen(5)
    requests.get('http://127.0.0.1:5000/api/make_client')# Wake up handle logs client
    while True:
        connection, address = s.accept()
        while True:
            data = connection.recv(16)
            if data:
                print(data.decode('utf-8'))
except KeyboardInterrupt:
    requests.get('http://127.0.0.1:5000/api/close_client') # Close current client
    exit()
