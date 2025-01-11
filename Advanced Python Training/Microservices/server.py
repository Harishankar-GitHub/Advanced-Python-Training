# Microservices is a design pattern

import socket
import threading

def writeFile(n):
    '''persist n in a byte file'''
    print('writing bytefile')
    with open('my_byte_log', 'ab') as fout:
        if type(n) == bytes:
            fout.write(n)
        elif type(n) == str:
            fout.write(n.encode)

def server():
    '''This is a simple socket server. It will respond to client requests'''

    # here are some common sensible defaults
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    setup_t = ('localhost', 9876) # IP and Port
    server.bind(setup_t)
    
    # begin listing for clients
    server.listen(4) # this may handle up to 4 concurrent requests
    print(f'Server is listening on {setup_t[0]}:{setup_t[1]}')

    while True:
        # we can accept any client request
        (client, addr) = server.accept()
        
        buf = client.recv(1024) # receive the first 1024 bytes from the client
        buf_str = buf.decode() # convert to string
        print(f'Server received {buf_str}')

        # we may choose to call a handler function on a new thread
        t = threading.Thread(target=writeFile, kwargs={'n': buf})
        t.start()

        if buf in (b'quit', b'Quit', b'QUIT'):  # b'quit' is shorthand for 'quit'.encode
            # Server is closing
            break
        else:
            # respond to the client
            repsonse_str = buf_str.upper()
            client.send(repsonse_str.encode())


if __name__ == '__main__':
    server()
