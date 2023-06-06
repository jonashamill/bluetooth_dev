# BLE SCAN


from bluetooth.ble import DiscoveryService
from time import sleep

def main():
    service = DiscoveryService()
    devices = service.discover(2)

    for address, name in devices.items():
        print("name: {}, address: {}".format(name, address))

    return


if __name__ == '__main__':
    main()