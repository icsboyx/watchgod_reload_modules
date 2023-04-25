import importlib,os,sys,time
import modules
from multiprocessing import Process
from watchgod import arun_process
from watchgod import watch
#---- declare and initialize global variables -----#
global thread_processes

thread_processes = []
filename = os.path.basename(__file__)

#---- processes are created here -----#
def create_processes():
    thread_processes = []
    importlib.reload(modules.test01)
    thread_processes.append(Process(target=modules.test01.start, name="test01"))
    importlib.reload(modules.test02)
    thread_processes.append(Process(target=modules.test02.start, name="test02"))
    #---- any process can be started here -----#
    #---- reload modules before start -----#
    return thread_processes


#---- main part -----#
#---- create thread_processes list from create_processes function -----#
thread_processes = create_processes()

#---- start all processes -----#
for process in thread_processes:
    print(f"Starting {process=}")
    process.start()

#---- start waiting all processes -----#
print("Watching for changes inside " + "./modules") 
for changes in watch("./modules"):

#--- after something is changed event ---#
    print(changes)

#---- terminate all processes -----#
    for process in thread_processes:
        print(f"{process=}")
        process.terminate()
    time.sleep(1)

#---- create new thread_processes list from create_processes function -----#
    thread_processes = create_processes()

#---- restart all processes -----#
    for process in thread_processes:
        print(f"Starting {process=}")
        process.start()