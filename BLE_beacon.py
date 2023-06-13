# BLE BEACON

from gattlib import BeaconService
from time import sleep

def main():
    service = BeaconService()

    service.start_advertising("3a6e4db3-4ebe-49d4-b16c-3a537deef82f",
                          1, 1, 1, 200)
    
    
    input('Beacon running.')

    # sleep(15)
    service.stop_advertising()

    print("Done.")


if __name__ == '__main__':
    main()