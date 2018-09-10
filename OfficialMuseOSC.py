import argparse
import math
import socket

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


DataSet = box()
def eeg_handler(unused_addr, args, ch1, ch2, ch3, ch4):
    # print("EEG (uV) per channel: ", ch1, ch2, ch3, ch4)
    DataSet.add([ch1,ch2,ch3,ch4])


#this is the socket server, just treat it as a blackbox
if __name__ == "__main__":
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
                        default=7032, #  <---------------- make sure this matches this -----------------> muse-player -f Blinks30.muse -s osc.udp://127.0.0.1:7010
                        help="The port to listen on")
    args = parser.parse_args()

    dispatcher = dispatcher.Dispatcher()
    dispatcher.map("/debug", print)
    dispatcher.map("/muse/notch_filtered_eeg", eeg_handler, "EEG") #   <-------------- this also kind of matter, you basically choose what you want to listen to here
    server = osc_server.ThreadingOSCUDPServer((args.ip, args.port), dispatcher)
    print("Serving on {}".format(server.server_address))
    server.serve_forever()