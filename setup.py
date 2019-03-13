import os

class setup(object):
    def init():
        self.is_IPFS, self.is_IRI, self.is_pystuff = False, False, False
        if not os.path.isdir("/usr/bin/GiTangle"):
            os.system("sudo mkdir /usr/bin/GiTangle")
        if not os.path.isdir("/usr/bin/GiTangle/IRI"):
            self.is_IRI = True
        if not os.path.isdir("/usr/bin/GiTangle/IPFS"):
            self.is_IPFS = True
        if not os.path.isdir("/usr/bin/GiTangle/pygit"):
            self.is_pystuff = True
        
        

    def install_IRI(self):
        if not self.is_IRI:
            os.system("cd ~ && cd /usr/bin/GiTangle")
            os.system("sudo mkdir IRI && cd IRI")
            os.system("sudo git clone https://github.com/iotaledger/iri")
            os.system("cd iri")
            os.system("sudo mvn clean compile")
            os.system("sudo mvn package")

    def install_IPFS(self):
        if not self.is_IPFS:
            os.system("cd ~ && cd /usr/bin/GiTangle/")
            os.system("sudo mkdir IPFS")
            os.system("cd IPFS")
            os.system("sudo wget https://dist.ipfs.io/go-ipfs/v0.4.19/go-ipfs_v0.4.19_linux-amd64.tar.gz")
            os.system("sudo tar xvfz go-ipfs.tar.gz")
            os.system("sudo cd go-ipfs")
            os.system("./install.sh")
    
    def install_pystuff(self):
        if not self.is_pystuff:
            os.system("cd ~ && cd /usr/bin/GiTangle/")
            os.system("pip3 install ipfsapi")
            os.system("pip3 install github")
            os.system("pip3 install zerorpc")
            os.system("sudo mkdir pygit && cd pygit")
            os.system("sudo wget https://github.com/libgit2/libgit2/archive/v0.27.0.tar.gz")
            os.system("sudo tar xzf v0.27.0.tar.gz")
            os.system("cd libgit2-0.27.0/")
            os.system("sudo cmake .")
            os.system("sudo make")
            os.system("sudo make install")
            os.system("pip3 install pygit2")


    def initialize():
        os.system("cd ~")
        os.system("java -jar /usr/bin/GiTangle/IRI/iri*.jar -p 14265")
        os.system("ipfs daemon")

s = setup()
s.install_IRI()
s.install_IPFS()
s.install_pystuff()
s.initialize()
