import socket
import random
import os
import requests
import re
import googlesearch
import wolfram
import github
import string
import sys
HOST = "chat.freenode.net"
PORT = 6667
NICK = "Portal"
PASSWORD = os.getenv("PASSWORD")
CHANNEL = "##techdudeserver"
#CHANNEL = "##BlockySurvival"
SERVER = ""
readbuffer = ""
def send(message):
    s.send(message)
    print(message)
s = socket.socket()
s.connect((HOST, PORT))
send(bytes("NICK %s\r\n" % NICK, "UTF-8"))
send(bytes("USER %s %s %s :%s\r\n" % (NICK, NICK, NICK, NICK), "UTF-8"))
#s.send(bytes("PRIVMSG NickServ regain {} {}\r\n".format(NICK, PASSWORD), "UTF-8"))
#s.send(bytes("PRIVMSG NickServ identify {} {}\r\n".format(NICK,PASSWORD), "UTF-8"))
send(bytes("JOIN {}\r\n".format(CHANNEL), "UTF-8"))
s.send(bytes("PRIVMSG NickServ :identify {}\r\n".format(PASSWORD), "UTF-8"))
readbuffer = readbuffer + s.recv(1024).decode("UTF-8")
temp = str.split(readbuffer, "\n")
readbuffer = temp.pop()
for line in temp:
    SERVER = str.rstrip(line)[1:].split()[0]
    print(str.rstrip(line))
while 1:
    readbuffer = readbuffer + s.recv(1024).decode("UTF-8")
    temp = str.split(readbuffer, "\n")
    readbuffer = temp.pop()
    for line in temp:
        print(str.rstrip(line))
        message = str.rstrip(line).split(" PRIVMSG {} :".format(CHANNEL))
        if "PING" in line:
            send("PONG :{}\r\n".format(SERVER).encode("utf-8"))
        msg = message[-1]
        tokens = msg.split()
        if msg == "$hello":
            send("PRIVMSG {} :Hello!\r\n".format(CHANNEL).encode("utf-8"))
        if msg == "$ping":
            send("PRIVMSG {} :Pong!\r\n".format(CHANNEL).encode("utf-8"))
        if msg == "$random":
            send("PRIVMSG {} :{}\r\n".format(CHANNEL, random.randint(
                0, 100)).encode("utf-8"))
        if msg.startswith("$youtube "):
            html = requests.get(
                "https://www.youtube.com/results?search_query=" +
                " ".join(msg.split()[1:])).content
            video_ids = re.findall(r"watch\?v=(\S{11})", html.decode())
            send("PRIVMSG {} :https://www.youtube.com/watch?v={}\r\n".format(
                CHANNEL, video_ids[0]).encode("utf-8"))
        if msg.startswith("$google "):
            send("PRIVMSG {} :{}\r\n".format(
                CHANNEL,
                googlesearch.search(" ".join(msg.split()[1:]))[0]).encode("utf-8"))
        if msg.startswith("$wolfram "):
            send("PRIVMSG {} :{}\r\n".format(
                CHANNEL,
                wolfram.get(" ".join(msg.split()[1:]))).encode("utf-8"))
        if msg.startswith("$github "):
            if tokens[1] == "url":
                send("PRIVMSG {} :https://github.com/{}/{}\r\n".format(
                    CHANNEL, tokens[2], tokens[3]).encode("utf-8"))
            if tokens[1] == "issues":
                send("PRIVMSG {} :#{}: {}\r\n".format(
                    CHANNEL, tokens[4],
                    github.get_issue_title(tokens[2], tokens[3],
                                           tokens[4])).encode("utf-8"))
        if msg == "$help":
            send("PRIVMSG {} :Avalible commands: $hello, $ping, $youtube, $google, $github, $wolfram.\r\n".format(CHANNEL).encode("utf-8"))
        if msg.startswith("$help "):
            if tokens[1] == "hello":
                send("PRIVMSG {} :Syntax: $hello  Action: Says \"Hello!\".\r\n".format(CHANNEL).encode("utf-8"))
            if tokens[1] == "ping":send("PRIVMSG {} :Syntax: $ping  Action: Says \"Ping!\".\r\n".format(CHANNEL).encode("utf-8"))
            if tokens[1] == "youtube":
                send("PRIVMSG {} :Syntax: $youtube <keyword> Action: Sends the URL of a YouTube video matching the keyword given.\r\n".format(CHANNEL).encode("utf-8"))
            if tokens[1] == "google":
                send("PRIVMSG {} :Syntax: $google <keyword> Action: Sends the URL of a google search with the keyword given\r\n".format(CHANNEL).encode("utf-8"))
            if tokens[1] == "github":
                send("PRIVMSG {} :Syntax: $github <topic> <user> <repo> <number> Action: Returns data about a github repo.\r\n".format(CHANNEL).encode("utf-8"))
            if tokens[1] == "wolfram":
                send("PRIVMSG {} :Syntax: $wolfram <query> Action: Asks Wolfram|Alpha the query given.\r\n".format(CHANNEL).encode("utf-8"))