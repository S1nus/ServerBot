import getpass
import mcrcon
import time
from threading import Thread
print 'Op-bot version 1.0'
print "Connecting..."
r = mcrcon.MCRcon("127.0.0.1", 25575, "server")
print "Logged in successfully"
print "opening the log..."
print "log file opened succesfully"
def find_length(file):
    lines = 0
    buffer = bytearray(2048)
    with file as f:
        while f.readinto(buffer) > 0:
            lines += buffer.count('\n')
    return (int)(lines - 1)
def imprison(user):
    r.send("tp " + user + " 162.99519 95.000 328.82663")
    r.send("gamemode 2 " + user)
    time.sleep(30)
    r.send("gamemode 0 " + user)
    r.send("tp " + user + " 0 0 0")
while True:
    log = open("logs/latest.log", "r")
    linecheck = log.readlines()[find_length(log)].split()
    if (len(linecheck) > 8) :
        #six and seven
        #five is target
        if (linecheck[6] == "game" and linecheck[7] == "mode"):
            if (linecheck[5] == "own"):
                r.send("gamemode 0 " + linecheck[3][1:(len(linecheck[3])-1)])
            else:
                r.send("gamemode 0 " + linecheck[5][:(len(linecheck[5])-2)])
            r.send("say " + linecheck[3][1:(len(linecheck[3])-1)] + " tried and failed to change someone's game mode")
        if (linecheck[4].lower() == "given"):
            Thread(target=imprison, args=[linecheck[3][1:(len(linecheck[3])-1)]]).start()
    time.sleep(3)
