# BLE BEACON

from gattlib import BeaconService
from time import sleep

def main():
    service = BeaconService()

    service.start_advertising("11111111-2222-3333-4444-555555555555",
                          1, 1, 1, 200)
    
    input('Beacon running.')

    # sleep(15)
    service.stop_advertising()

    # print("Done.")


if __name__ == '__main__':
    main()