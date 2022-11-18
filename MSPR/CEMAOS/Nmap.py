import nmap
#pip install python-nmap
import json
import os

#Scan la range de ports choisie sur l'ip renseignée
class ScanPort():
    def __init__(self):
        self.port = None
        self.ip = None
        self.scanner = nmap.PortScanner()
        
    
        self.scanning('172.16.71.1', '44880-44890')
        
    #récupere l'ip et la range de ports a regarder    
    def scanning(self,ip, portRange):
        Ports = None
        State = None
        self.scanner.scan(ip, portRange)
        #recupere l'etat ainsi que le nom de l'hote
        for host in self.scanner.all_hosts():
            print('Host : %s (%s)' % (host, self.scanner[host].hostname()))
            print('State : %s' % self.scanner[host].state())
            #affiche le protocole utilisé sur les ports ouverts
            for protocols in self.scanner[host].all_protocols():
                print('\n')
                print('Protocol : %s' % protocols)
                ports = self.scanner[host][protocols].keys()
                #affiche les ports ouverts
                for port in ports:
                    Ports = '%s %s '% (Ports, port)
                    print ('port : %s\tstate : %s' % (port, self.scanner[host][protocols][port]['state']))
                    
app = ScanPort
app()