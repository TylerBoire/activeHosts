import multiprocessing
import scapy
import netaddr
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-i","--inFile", help="scope file")
parser.add_argument("-o","--outFile", help="active hosts")

ipPool = []

def getHosts()
    with open ("") as ipList:
        #Take in IP w/ CIDR and parse into single IPs
        for line in ipList:
            for ip in IPNetwork("'" + line + "'"):
                ipPool.append(ip)

def PingHost()
    #Take host from pool and send ping

def listener()
    #Listener thread to catch icmp reponses

if __name__ == __main__

