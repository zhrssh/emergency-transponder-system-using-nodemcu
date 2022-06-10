import urllib.request
import http

from base import Base
from time import sleep

# start of the code
def start():
    url = "http://192.168.1.13/"

    base = Base()

    while True:
        # check for sos messages
        mydict = base.receive_sos()
        print(f"SOS Received: {mydict}")

        # receive data first
        response = request_conn(url)

        # if there is no data to receive from node and there is sos messages
        if "None" in response and len(mydict) > 0:
            keys = mydict.keys()

            # key are ids of the node that need sos
            for key in keys:
                data = f"SOS/{mydict[key]}/{key}"

                # will listen to the data sent
                response = request_conn(url + data)

                # if received a response
                if "C" in response:
                    break

        # if there is sos response will try relay to the sos sender
        if "C" in response:
            try:
                # message format: C/LOCATION/ID
                # location = data_list[1]
                id = response[2]
                base.respond_sos(id)

            except IndexError as err:
                pass

        sleep(3)

    #### FOR TESTING ###
    # test_comms = Comms(2011118, "Quezon City")
    # test_comms.send_sos()
    # test_base = Base()
    # while True:
    #     mydict = test_base.receive_sos()
    #     if len(mydict) <= 0:
    #         print("No SOS received.")
    #     else:
    #         keys = mydict.keys()
    #         for id in keys:
    #             print(f"SOS at {mydict[id]}!")
    #             test_base.respond_sos(id)
    #     sleep(30)
    ####################


def request_conn(url):
    try:
        x = urllib.request.urlopen(url).read()
        x = x.decode("utf-8")
        x = x.split("/")

        return x  # returns list

    except http.client.BadStatusLine as err:
        err = str(err).split("/")
        return err  # returns list


if __name__ == "__main__":
    start()
