import socket
import time

def ping():
    t=0
    status=True
    while(1):
            status=internet_on()
            if status is True:
                t=1
            if status is False:
                t+=1

            time.sleep(t)
            status=internet_on()



def internet_on():

    try:
        socket.create_connection(("www.google.com",80))
        print('internet is running')
        return True
    except OSError:
        print('internet not running')


    return False
ping()

