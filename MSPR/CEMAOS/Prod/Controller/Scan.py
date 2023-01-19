import nmap
#pip install python-nmap
import json
import os
import socket


#récupere l'ip et la range de ports a regarder    
def scan_ports(host):
    nm = nmap.PortScanner()
    nm.scan(host, '1-65535')
    for host in nm.all_hosts():
        print('Host : %s (%s)' % (host, nm[host].hostname()))
        print('State : %s' % nm[host].state())
        for proto in nm[host].all_protocols():
            print('----------')
            print('Protocol : %s' % proto)
            lport = nm[host][proto].keys()
            lport.sort()
            for port in lport:
                print ('port : %s\tstate : %s' % (port, nm[host][proto][port]['state']))

#print(scan_ports("172.16.71.1"))


def scan_network():
    MachineScan={}
    nm = nmap.PortScanner()
    nm.scan(hosts='172.16.70.0/24', arguments='-sP')
    hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]
    for host,value in hosts_list:
        hostname = socket.gethostbyaddr(host)[0]
        print(host + " : " + hostname)
        MachineScan[host]= hostname
    return MachineScan

