#!/usr/bin/python

# experiment for building serial communication with arduino



import serial

fConnected = False
ser = "placeholder"


def sersend(data):
    global fConnected
    global ser

    # check incoming data
    resultok = (type(ser) == type(''))
    if not resultok:
        # log data about invalid value passed in to function
        raise

    # attempt to send
    try:
        ser.send(data)
    except:
        # if that failed, the port might have become disconnected
        try:
            ser.close()   # don't leave lose ends, just in case
        except:
            pass  # if close fails, it wasn't open yet

        # now we'll try connecting.
        try:
            ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
        except:
            # log data about the connect failure here
            raise
        try:
            ser.send(data)
        except:
            # log data about the send failure here
            raise
