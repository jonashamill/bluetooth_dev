# Client


import bluetooth

def main():
    
    bdAddr = '3C:21:9C:E0:88:54'

    port = 1

    sock = bluetooth.BluetoothSocket( bluetooth.RFCOMM )
    sock.connect ((bdAddr, port))

    while (1):
        sock.send ("Hello Blue World!!")

    sock.close()


if __name__ == '__main__':
    main()