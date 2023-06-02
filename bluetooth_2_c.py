# Client


import bluetooth

def main():
    
    bdAddr = '3C:21:9C:E0:88:54'

    port = 1

    sock = bluetooth.BluetoothSocket( bluetooth.RFCOMM )
    sock.connect ((bdAddr, port))

    for i in range(1,101):
        sock.send ("Hello Blue World!! ", i)

    sock.close()


if __name__ == '__main__':
    main()