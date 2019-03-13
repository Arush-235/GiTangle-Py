import os

class setup(object):
    def init():
        self.is_IPFS, self.is_IRI, self.is_pystuff = False, False, False
        if not os.path.isdir("/home/GiTangle"):
            os.system("mkdir /home/GiTangle")
        if not os.path.isdir("/home/GiTangle/IRI"):
            self.is_IRI = True
        if not os.path.isdir("/home/GiTangle/IPFS"):
            self.is_IPFS = True
        if not os.path.isdir("/home/GiTangle/pygit"):
            self.is_pystuff = True
        
        

    def install_IRI(self):
        if not self.is_IRI:
            os.system("cd ~ && cd /home/GiTangle")
            os.system("mkdir IRI && cd IRI")
            os.system("git clone https://github.com/iotaledger/iri")
            os.system("cd iri")
            os.system("mvn clean compile")
            os.system("mvn package")

    def install_IPFS(self):
        if not self.is_IPFS:
            os.system("cd ~ && cd /home/GiTangle/")
            os.system("mkdir IPFS")
            os.system("cd IPFS")
            os.system("wget https://dist.ipfs.io/go-ipfs/v0.4.19/go-ipfs_v0.4.19_linux-amd64.tar.gz")
            os.system("tar xvfz go-ipfs.tar.gz")
            os.system("cd go-ipfs")
            os.system("./install.sh")
    
    def install_pystuff(self):
        if not self.is_pystuff:
            os.system("cd ~ && cd /home/GiTangle/")
            os.system("pip3 install ipfsapi")
            os.system("pip3 install github")
            os.system("pip3 install zerorpc")
            os.system("mkdir pygit && cd pygit")
            os.system("wget https://github.com/libgit2/libgit2/archive/v0.27.0.tar.gz")
            os.system("tar xzf v0.27.0.tar.gz")
            os.system("cd libgit2-0.27.0/")
            os.system("cmake .")
            os.system("make")
            os.system("sudo make install")
            os.system("pip3 install pygit2")


    def initialize():
        os.system("java -jar /home/IRI/iri*.jar -p 14265")
        os.system("ipfs daemon")

s = setup()
s.install_IRI()
s.install_IPFS()
s.install_pystuff()
s.initialize()
