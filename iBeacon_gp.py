from gattlib import BeaconService
from time import sleep

def main():
    service = BeaconService()

    # Define the iBeacon parameters
    uuid = "11111111-2222-3333-4444-555555555555"
    major = 1
    minor = 1
    power = 200

    # Convert the parameters to the byte representation
    payload = bytes([
        0x02, 0x01, 0x1A,  # iBeacon advertisement indicator
        0x1A,  # Length of the remaining payload
        0xFF, 0x4C, 0x00, 0x02, 0x15,  # iBeacon identifier
    ] + [int(x, 16) for x in uuid.split("-")] + [
        (major >> 8) & 0xFF, major & 0xFF,
        (minor >> 8) & 0xFF, minor & 0xFF,
        power
    ])

    service.start_advertising(payload)

    input('Beacon running.')

    service.stop_advertising()

    print("Done.")


if __name__ == '__main__':
    main()
