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


scan_ports("172.16.70.12")


'''def scan_network():
    active_hosts = []
    for host in range(1,256):
        ip = "172.16.70." + str(host)
        # Utilise la commande ping pour tester si l'hôte est actif
        response = os.system("ping -c 1 " + ip)
        if response == 0:
            active_hosts.append(ip)
            print(ip + " is active")
    return active_hosts
print(scan_network())'''


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



