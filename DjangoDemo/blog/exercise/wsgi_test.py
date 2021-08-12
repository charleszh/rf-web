# coding :utf-8
import socket, threading
import errno
import time

EOLl = b'\n\n'
EOL2 = b'\n\r\n'
body = '''Hello , world ! <h1> from the5fire 《Django 企业开发实战》</h1>  from {thread_name}'''
response_params = [
    'HTTP/1. 0 200 OK ',
    'Date : Sun , 27 may 2018 01 : 01 : 01 GMT ',
    'Cotent-Type : text/html; chars et=utf-8',
    'Content-Length : {}\r\n'.format(len(body.encode())),
    body,
    ]
response = "\r\n".join(response_params)

def handle_connection(conn, addr):
    print('on, new conn', conn, addr)
    import time
    time.sleep(5)
    request = b""
    while EOLl not in request and EOL2 not in request:
        request += conn.recv(1024 )
    print(request)
    current_thread = threading.currentThread()
    content_length = len(body.format(thread_name=current_thread.name).encode())
    print(current_thread.name)
    conn.send(response.format(thread_name=current_thread.name,
                              lenght=content_length).encode()) #response 转为bytes 后传输
    conn.close()
def main() :
    # socket . AF_ INET 用于服务器与服务器之间的网络通信
    # socket . SOC K_STREAM 用于基于TCP 的流式socket 通信
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM )
    #设置棕口可复用，保证我们每次按Ctrl+C 组合键之后，快这主启
    serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    serversocket.bind(('127.0.0.1', 8000))
    serversocket.listen(5) #设置backlog-socket 连接最大排队数量
    print('http://127.0.0.1:8000')
    serversocket.setblocking(0)
    try :
        i = 0
        while True:
            try:
                conn , address= serversocket.accept()
                
            except socket.error as e:
                if e.args[0] != errno.EAGAIN:
                    raise
                continue
            i += 1
            print(i)
            t = threading.Thread(target=handle_connection, args=(conn, address), name='thread-%s' % i)
            t.start()
    finally:
        serversocket.close()
if __name__ == '__main__':
    main()