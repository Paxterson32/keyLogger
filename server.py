
import threading
import socket

IP = "1.1.1.1"
PORT = 1234
DATA_MINIMUM_SIZE = 1024


def start_server():
    # this function will read the data from the file and send it to the external server
    global s
    
    # We will use IPv4 addresses and TCP
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # we will set additionnal socket options : SOL_SOCKET = the options is set for the socket itself, SO_REUSEADDR = the socket can be reuse immediately after closing it 
    # 1 = value given to the SO_REUSEADDR
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # Make a binding with the given IP and port
    s.bind((IP,PORT))
    # set the max number of connexions we will accept. 
    s.listen(2)
    # for each connexion we accept, we will get the addr and a connexion object
    conn, addr = s.accept()


    if conn != None:
        print(f"\nConnection Succesfully Established from {addr}")
        # For each successful connexion we will create a new thread to handle the received data's
        t = threading.Thread(target=get_data, args=[conn,addr[0]])
        t.deamon = True
        t.start()

        
def get_data(conn,ip_string):
    with open(ip_string,'a+') as f:
        while True:
            data = conn.recv(DATA_MINIMUM_SIZE)
            # we have to use the decode utf-8 in order to correctly format the data. 
            print(data.decode('utf-8'))
            f.write(data.decode('utf-8'))


if __name__ == "__main__":
    start_server()
