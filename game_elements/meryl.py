import socket
import pickle

class Meryl:
    CLIENT = 0
    SERVER = 1
    PORT0 = 3278
    PORT1 = 2635
    PORT2 = 1027
    PORT4 = 9999
    HEADER_SIZE = 7
    N_CONNECTIONS = 2
    def __init__(self, type_):
        self.s = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM
            )
        self.port = self.PORT0
        self.type = type_
        if type_ == self.SERVER:
            self.s.bind(
                (socket.gethostname(), self.PORT0)
                )
            self.s.listen(self.N_CONNECTIONS)
            print(f"Server is ready at port {self.PORT0}")
        elif self.type == self.CLIENT:
            self.s.connect(
                (socket.gethostname(), self.PORT0)  
                )
            print("client is ready")

    def wait_for_conn(self):
        if self.type == self.SERVER:
            self.client, addr = self.s.accept()
            print(f"Client connected on {addr}")

    def wait_for_act(self):
        if self.type == self.SERVER:
            msg = self.recv()
            return msg
    
    def reply(self, response):
        if self.type == self.SERVER:
            self.send(response)

    def send(self, msg):
        d_msg = pickle.dumps(msg)
        d_msg = bytes(f'{len(d_msg):<{self.HEADER_SIZE}}', 'utf-8') + d_msg
        send_obj = self.conn_obj()
        send_obj.send(d_msg)

    def recv(self):
        recv_obj = self.conn_obj()
        msglen = int(recv_obj.recv(self.HEADER_SIZE))
        msg = recv_obj.recv(msglen)
        msg = pickle.loads(msg)
        return msg

    def conn_obj(self):
        if self.type == self.SERVER:
            conn_obj = self.client
        elif self.type == self.CLIENT:
            conn_obj = self.s
        return conn_obj

    def close(self):
        if self.type == self.SERVER:
            self.client.close()