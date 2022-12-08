import json


class Contact:
    contactList=[]
    def __init__(self,Data):
        file = open(Data, "r")
        for line in file.readlines():
            contact = json.loads(str(line))
            self.contactList.append(contact)
        self.Data=Data
    def Details(self,s):
        for i in self.contactList:
            if(i["Name"]==s):
                return i
        return
    def refactor(self):
        file=open(self.Data,"w")
        file.write(json.dumps(self.contactList[0])+"\n")
        file.close()
        with open(self.Data,"a") as file:
            for i in self.contactList[1:]:
                file.write(json.dumps(i)+"\n")
    def delete(self,dets):
        self.contactList.remove(dets)
        self.refactor()
    def update(self,dets,detsUpdate):
        self.contactList.remove(dets)
        self.contactList.append(detsUpdate)
        self.refactor()
    def append(self,dets):
        self.contactList.append(dets)
        self.refactor()

    def retNameList(self):
        names=[i["Name"] for i in self.contactList]
        return names
def doNoth():
    pass
