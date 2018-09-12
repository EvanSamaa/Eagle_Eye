import argparse
import math
import socket
import os 
from pythonosc import dispatcher
from pythonosc import osc_server
from pythonosc import udp_client
from pythonosc import osc_message_builder
# to read from .muse file (aka the recordings). Simply use cmd to go to the folder your recordings are located. THen type in this 
# muse-player -f <file_name>.muse -s osc.udp://127.0.0.1:<port of choices>
# e.g. muse-player -f blink.muse -s osc.udp://127.0.0.1:7042
# then make sure the socket server is listening to the same port and hit run!

# to read from actual muse. Connect using muse direct, and make the port 5001, then run

class box(): # the eeg handler will store the data into this python class. Have fun
    def __init__ (self):
        self.store = [[],[],[],[]]
    def add(self, signals):
        for i in range (0, 4):
            self.store[i] = self.store[i] + [signals[i]]
    def printThing(self):
        print(self.store)
    def ExportInterval(self, interval = 100):
        thing = [self.store[0][-interval:],self.store[1][-interval:],self.store[2][-interval:],self.store[3][-interval:]]
        return thing
    def searchBlink(self, length = 100):
        try:
            workedOrNah = findBlink(self.ExportInterval())
            if workedOrNah == 0:
                self.store = [[],[],[],[]]
                return 0
            else:
                return -1
        except:
            nothing = "nothing"
            return False


def findBlink(portList):    # portlist = [port1, port2, port3, port4], each port# is actually a list of n voltage readings, so this
                            # portlist object is a 4xn 2d array
    #all the code here

    UpwardSpike = 0
    DownwardSpike = 0
    for dataPoint in portList: # iterate through in interval
        for i in range (4, 5):
            try:
                # print(UpwardSpike, DownwardSpike)
                # if DownwardSpike > 0 and UpwardSpike > 0:
                if UpwardSpike > 0:
                    print("Blink registered!")
                    #flapMywings() # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<---------------------------------------------------------------------- put wing flapping function here
                    return 0
                elif (float(dataPoint[i]) > 1000):
                    DownwardSpike = 1
                elif (float(dataPoint[i]) < 840) and (DownwardSpike > 0):
                    UpwardSpike = UpwardSpike + 1
            except:
                return -1
                kk = 3


DataSet = box()
def eeg_handler(unused_addr, args, ch1, ch2, ch3, ch4):
    # print("EEG (uV) per channel: ", ch1, ch2, ch3, ch4)
    DataSet.add([ch1,ch2,ch3,ch4])
    DataSet.searchBlink()


#this is the socket server, just treat it as a blackbox
if __name__ == "__main__":
    port = "7009" # <--------------------------------------------------Change this when there is a bug. Increase the number by one lol
    host = socket.gethostname()
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip",
                        default="127.0.0.1",
                        help="The ip to listen on")
    # parser.add_argument("--ip",
                        # default=host,
                        # help="The ip to listen to")
    parser.add_argument("--port",
                        type=int,
                        default=7009, # <-------------------- change this often, but make sure it matches "muse-player -f blinks30.muse -s osc.udp://127.0.0.1:7009"
                        help="The port to listen on")
    args = parser.parse_args()

    dispatcher = dispatcher.Dispatcher()
    dispatcher.map("/debug", print)
    dispatcher.map("/muse/notch_filtered_eeg", eeg_handler, "EEG") #   <-------------- this also kind of matter, you basically choose what you want to listen to here
    server = osc_server.ThreadingOSCUDPServer((args.ip, args.port), dispatcher)
    print("Serving on {}".format(server.server_address))
    server.serve_forever()
