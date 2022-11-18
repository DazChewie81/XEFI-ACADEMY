import os
import json
class Ping():
    def __init__(self):
        self.ip = "8.8.8.8"
        self.reseau = "172.16.71."
        self.pingstatus = None
        self.ipDeb = 1
        self.ipFin = 5
        
        self.TabOn =[]
        self.TabPing=[]

        #self.pingSimple(self.ip)
        self.pingReseau(self.reseau, self.ipDeb, self.ipFin+1)

        # self.testping={
        # "ip":self.ip,
        # "ping":self.pingstatus
        # }
        # with open('/home/axel/GITHUB/XEFI-ACADEMY/MSPR/CEMAOS/test.json', 'w') as mon_fichier:
        #     json.dump(self.testping, mon_fichier)

    def pingSimple(self, vHostname):
        response = os.system("ping -c 1  " + vHostname)
        if response == 0:
            self.pingstatus = "Network Active"
        else:
            self.pingstatus = "Network Error"
        print(self.pingstatus,"\n")
        
    def pingReseau(self, ip, debut, fin):
        for test in range (debut, fin):
            adresse = ip + str(test)
            response = os.system("ping -c 1 " + adresse)
            if response == 0:
                self.pingstatus = "Network OK"
                self.TabOn.append(adresse)
                self.TabPing.append(self.pingstatus)

            else:
                self.pingstatus = "Eteint"
        return self.TabOn[0]       
        





app = Ping
app()
    