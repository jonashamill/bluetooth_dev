from gattlib import DiscoveryService

def main():

    
    service = DiscoveryService("hci0")
    devices = service.discover(2)

    for address, name in devices.items():
        print("name: {}, address: {}".format(name, address))

if __name__ == '__main__':
    main()
