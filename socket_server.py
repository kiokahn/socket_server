# 클라이언트의 Request 확인을 위한 소켓서버
# By KiokAhn
# 2024-06-05
#
# test for HTTP multipart
# curl -X POST -S -H "Authorization: JWT b181ce4155b7413ebd1d86f1379151a7e035f8bd" -F "author=1" -H 'Accept: application/json' -F "title=curl 테스트" -F "text=API curl로 작성된 AP 테스트 입력 입니다." -F "created_date=2024-06-10T18:34:00+09:00" -F "published_date=2024-06-10T18:34:00+09:00" -F "image=@/Users/kiokahn/Pictures/53297865145_aca24097c7_k.jpg;type=image/jpg" http://127.0.0.1:8000/api_root/Post/
#

import os
import socket
from datetime import datetime

class SocketServer:
    def __init__(self):
        self.bufsize = 1024  # 버퍼 크기 설정
        with open('./response.bin', 'rb') as file:
            self.RESPONSE = file.read()  # 응답 파일 읽기

        self.DIR_PATH = './request'
        self.createDir(self.DIR_PATH)

    def createDir(self, path):
        """디렉토리 생성"""
        try:
            if not os.path.exists(path):
                os.makedirs(path)
        except OSError:
            print("Error: Failed to create the directory.")

    def run(self, ip, port):
        """서버 실행"""
        # 소켓 생성
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((ip, port))
        self.sock.listen(10)
        print("Start the socket server...")
        print("\"Ctrl+C\" for stopping the server!\r\n")

        try:
            while True:
                # 클라이언트의 요청 대기
                clnt_sock, req_addr = self.sock.accept()
                clnt_sock.settimeout(5.0)  # 타임아웃 설정 (5초)
                print("Request message...\r\n")

                response = b""
                try:
                    while True:
                        data = clnt_sock.recv(self.bufsize)
                        if not data:
                            break
                        response += data
                except socket.timeout:
                    print("Connection timed out")

                now = datetime.now()
                filename = self.DIR_PATH + now.strftime('/%Y-%m-%d-%H-%M-%S.bin')
                with open(filename, 'wb') as file:
                    file.write(response)

                print("Received data:")
                print(response.decode('utf-8', errors='replace'))

                # 응답 전송
                clnt_sock.sendall(self.RESPONSE)

                # 클라이언트 소켓 닫기
                clnt_sock.close()
        except KeyboardInterrupt:
            print("\r\nStop the server...")

        # 서버 소켓 닫기
        self.sock.close()

if __name__ == "__main__":
    server = SocketServer()
    server.run("127.0.0.1", 8000)
