from gattlib import BeaconService

def main():
    service = BeaconService()

    devices = service.scan()  # Scan for 2 seconds

    for address, _, _, payload in devices:
        print("Beacon found!")
        print("Beacon MAC address:", address)
        print("Received data:", payload.decode())
        print()

    print("Done.")

if __name__ == '__main__':
    main()
