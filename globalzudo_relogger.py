##################################################
## Globalzudo Client Relogger
##################################################

__author__ = "Gabs the Creator"
__copyright__ = "Copyright 2021, Gabs the Creator"
__credits__ = ["Gabriel Cerioni"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Gabriel Cerioni"
__email__ = "gabsthesre@gmail.com"
__status__ = "Production"

# Generic/Built-in
import subprocess
from time import sleep
import psutil
import logging

# Custom
import keyboard
from pynput.keyboard import Key, Controller

# Configs (if this gets bigger, i'll provide a config file... or even Hashicorp Vault)
logging.basicConfig(filename='globalzudo_relogger.log', filemode='a', format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)
CLIENT_LOCATION_WIN="C:\\Users\\Gabriel\\Desktop\\Globalzudo13"
CLIENT_OTC_OPTION="GlobalzudoKhaleesi.exe"


CHAR_TO_BE_BOUNCED="Khaleesi"
CHAR_ON_ACC_TOTAL=3
POSITION_ON_CHAR_LIST=2

def open_new_client(client_full_path):
    #subprocess.call(client_full_path)
    p = subprocess.Popen(client_full_path,
                     stdout=subprocess.PIPE,
                     stderr=subprocess.STDOUT)
    logging.info("This is the new client pid: {0}".format(p.pid))


def quick_client_bounce():
    return 1

def login_process(client_full_path, char_on_acc_total, position_on_char_list):
    open_new_client(client_full_path)

    sleep(3)
    keyboard.press("enter")
    keyboard.release("enter")    
    sleep(3)
    #for i in range(char_on_acc_total):
    #    keyboard.press("up") # Presses "up" key
    #    keyboard.release("up") # Releases "up" key
    #    sleep(1)

    keyboard.press("enter")
    keyboard.release("enter")
    sleep(1)

def kill_older_client_process(client_name):

    process_candidates = []

    for proc in psutil.process_iter():
      if client_name in proc.name():
          candidate_dict = {}
          candidate_dict["pid"] = proc.pid
          candidate_dict["creation_epoch"] = proc.create_time()
          process_candidates.append(candidate_dict)
    
    sorted_list = sorted(process_candidates, key=lambda k: k['creation_epoch'])
    
    oldest_pid = sorted_list[0]["pid"]
    logging.info("This is the oldest pid: {0}".format(oldest_pid))

    logging.warning("safety check - making sure that there is more than one client open...")
    if len(sorted_list) > 1:
        p = psutil.Process(oldest_pid)
        p.terminate()



def main():
    logging.info("#########################################")
    logging.info("######## Starting the program... ########")
    logging.info("#########################################")
    full_client_name = "{0}\\{1}".format(CLIENT_LOCATION_WIN, CLIENT_OTC_OPTION)
    logging.info("Full client name: {0}".format(full_client_name))

    logging.info("Starting the login process, on parallel client")
    login_process(full_client_name, CHAR_ON_ACC_TOTAL, POSITION_ON_CHAR_LIST)

    logging.info("Killing the older Client")
    kill_older_client_process(CLIENT_OTC_OPTION)

    logging.info("######## Done! ########")

if __name__ == '__main__':
    main()
