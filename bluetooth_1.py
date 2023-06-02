# Server


import bluetooth

def main():
    
    serverSock = bluetooth.BluetoothSocket( bluetooth.RFCOMM)

    port = 1 
    serverSock.bind(("", port))
    serverSock.listen(1)

    clientSock, address = serverSock.accept()
    print ("Accepted connection from: ", address)

    data = clientSock.recv(1024)
    print ("recieved [%s]" % data)

    clientSock.close()
    serverSock.close()


if __name__ == '__main__':
    main()