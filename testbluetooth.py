import time
import bluetooth
import subprocess

def search():
    devices = bluetooth.discover_devices(duration=20, lookup_names = True)
    return devices

if __name__=="__main__":
    while True:
        results = search()
        if (results!=None):
            for addr, name in results:
                print ("{0} - {1}".format(addr, name))
            #endfor
        #endif
        time.sleep(15)



    #endwhile
