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
    payload = [
        0x02, 0x01, 0x1A,  # iBeacon advertisement indicator
        0x1A,  # Length of the remaining payload
        0xFF, 0x4C, 0x00, 0x02, 0x15,  # iBeacon identifier
    ]
    payload += [int(x, 16) for x in uuid.split("-")]
    payload += [major >> 8, major & 0xFF]
    payload += [minor >> 8, minor & 0xFF]
    payload += [power]

    service.start_advertising(payload)

    input('Beacon running.')

    service.stop_advertising()

    print("Done.")


if __name__ == '__main__':
    main()
