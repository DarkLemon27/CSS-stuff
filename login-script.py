import threading
import time
import random
from pexpect import pxssh

def thread_function(username,password):
    
    while True:
        
        #SSH connection
        try:                                                            
            s = pxssh.pxssh()
            hostname = "???"   #Whatever host we want to do traffic
            s.login (hostname, username, password)
            
            #####optional sending commands
            s.sendline ('uptime')   # run a command
            s.prompt()             # match the prompt
            print(codecs.decode(s.before))          # print everything before the prompt.
            s.sendline ('ls -l')
            s.prompt()
            print(codecs.decode(s.before))
            #####
            
            s.logout()
        except(pxssh.ExceptionPxssh):
            print("pxssh failed on login.")

        #Random wait time
        sleppertime = random.randrange(30,300)
        time.sleet(sleppertime)
    
    return 

def main():
    random.seed(time.gmtime())
    user1 = threading.Thread(target=thread_function, args=("A","A",))
    user2 = threading.Thread(target=thread_function, args=("B","B",))
    user3 = threading.Thread(target=thread_function, args=("C","C",))
    user1.start()
    user2.start()
    user3.start()
    user1.join()
    user2.join()
    user3.join()

main()
