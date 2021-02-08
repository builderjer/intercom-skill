import sys
from mycroft_bus_client import MessageBusClient, Message

intercomClient = input("Address or domain name for client:  ")

try:
    client = MessageBusClient(host=str(intercomClient))
    client.run_in_thread()
except WebSocketAddressException:
    print("Could not connect to {}".format(intercomClient))
    print("Exiting")
    sys.exit()

message = input("Message to send to {}:  ".format(intercomClient))

try:
    client.emit(Message("speak", data={"utterance": message}))
except Exception as e:
    print(e)
    sys.exit()
