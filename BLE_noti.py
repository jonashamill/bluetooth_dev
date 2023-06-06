from gattlib import GATTRequester

def main():
    
    class Requester (GATTRequester):
        def onNotif(self, handle, data):
            print("- notification on handle: {}\n".format(handle))

    


if __name__ == '__main__':
    main()