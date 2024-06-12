# 클라이언트의 Request 확인을 위한 소켓서버
# By KiokAhn
# 2024-06-05
#
# test for HTTP multipart
# curl -X POST -S -H "Authorization: JWT b181ce4155b7413ebd1d86f1379151a7e035f8bd" -F "author=1" -H 'Accept: application/json' -F "title=curl 테스트" -F "text=API curl로 작성된 AP 테스트 입력 입니다." -F "created_date=2024-06-10T18:34:00+09:00" -F "published_date=2024-06-10T18:34:00+09:00" -F "image=@/Users/kiokahn/Pictures/53297865145_aca24097c7_k.jpg;type=image/jpg" http://127.0.0.1:8000/api_root/Post/
#

import os
import time
import socket
from datetime import datetime

class SocketServer:
    def __init__(self):
        self.bufsize = 1024
        file = open('./response.bin', 'rb')
        self.RESPONSE = file.read()
        file.close()

        self.DIR_PATH = './request'
        self.createDir(self.DIR_PATH)
        
    def createDir(self, path):
        try:
            if not os.path.exists(path):
                os.makedirs(path)
        except OSError:
            print("Error: Failed to create the directory.")

    def run(self, ip, port):
        # create socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("Start the socket server...")
        print("\"Ctrl+C\" for stopping the server!\r\n")

        self.sock.bind((ip, port))
        self.sock.listen(10)

        try:
            while True:
                # wait request
                clnt_sock, req_addr = self.sock.accept()

                print("Request message...\r\n")
                # read and print request
                response = b""
                while True:
                    data = clnt_sock.recv(self.bufsize)
                    if len(data)<self.bufsize :
                        response += data
                        break
                    else:
                        response += data
                        time.sleep(0.01)

                now = datetime.now()
                filename = self.DIR_PATH + now.strftime('/%Y-%m-%d-%H-%M-%S.bin')
                file = open(filename, 'wb')
                file.write(response)
                file.close()
                print(response)

                # send response
                clnt_sock.sendall(self.RESPONSE)

                # close clnt_sock
                clnt_sock.close()
        except KeyboardInterrupt:
            print("\r\nStop the server...")

        # close socket
        self.sock.close()

if __name__ == "__main__":
    server = SocketServer()
    server.run("127.0.0.1", 8000)