import bluetooth

def main():

    targetName = 'panda'
    targetAddress = None

    nearbyDevices = bluetooth.discover_devices()

    for bdaddr in nearbyDevices:
        if targetName == bluetooth.lookup_name(bdaddr):
            targetAddress = bdaddr
            break
    if targetAddress is not None:
        print ("found target bt device with addr: ", targetAddress)
    else:
        print("Device not found nearby")


if __name__ == '__main__':
    main()