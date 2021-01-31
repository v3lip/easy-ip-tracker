import os
import time
import signal
import sys
from subprocess import call

while True:
    try:
        os.system('clear')
        
        print("x---------------------------------------x\n|   Logger is RUNNING (ctrl+c to exit)  |\nx---------------------------------------x\n\n")
        os.system('cat log.txt')
        
        time.sleep(2)
    except KeyboardInterrupt:
        rc = call("bash clr.sh", shell=True)
        sys.exit(128 + signal.SIGINT)
    
    