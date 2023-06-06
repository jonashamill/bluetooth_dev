# BLE SCAN


from gattlib import DiscoveryService
from time import sleep

def main():
    service = DiscoveryService("hcio")
    devices = service.discover(2)

    for address, name in devices.items():
        print("name: {}, address: {}".format(name, address))

    


if __name__ == '__main__':
    main()