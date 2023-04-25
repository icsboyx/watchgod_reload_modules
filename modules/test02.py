import time , os

filename = os.path.basename(__file__)


def start():
    i=0
    while True:  
        i +=1
        #print(f"\033[0;31m New line inserted to {filename} \033[00m")
        print(f"print from {filename}, This file is running since {i} seconds.")
        time.sleep(1)

