import os
class Ping():
    def __init__(self):
        self.ip = "8.8.20.3"
        self.pingstatus = None
        
        self.pingSimple(self.ip)
        
    def pingSimple(self, vHostname):
        response = os.system("ping -c 1 " + vHostname)
        if response == 0:
            self.pingstatus = "Network Active"
        else:
            self.pingstatus = "Network Error"
        print(self.pingstatus)

app = Ping
app()
    