# BLE BEACON

from gattlib import BeaconService
from time import sleep

def main():
    service = BeaconService()

    service.start_advertising(1, 1, 1, 200, "Hello, World!")
    
    input('Beacon running.')

    # sleep(15)
    service.stop_advertising()

    print("Done.")


if __name__ == '__main__':
    main()