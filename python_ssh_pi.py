import pxssh
import getpass

#class ip_Exception(Exception):
    #'''If wrong formatted ip was entered'''
    #def __init__(self,

class address:
    def __init__(self,user,hostip,pswd):
        self.suffix = 0
        self.user = user
        self.host_ip = "{}{}".format(hostip,self.suffix)
        self.password = pswd
    
    #def check(self):
    def next_ip(self):
        self.suffix+=1
        self.host_ip = "{}{}".format(hostip,self.suffix)
        

def main():
    s = pxssh.pxssh()
    hostname = raw_input('host-ip (without last number): ')
    username = raw_input('username: ')
    password = getpass.getpass('password: ')
    for i in range(256):
        print i,":"
        try:                                                            
            s.login (hostname, username, password)
        except pxssh.ExceptionPxssh, e:
            print "pxssh failed on login."
            print str(e)
            pass
        s.sendline ('uptime')   # run a command
        s.prompt()             # match the prompt
        print s.before          # print everything before the prompt.
        s.sendline ('ls -l')
        s.prompt()
        print s.before
        s.sendline ('df')
        s.prompt()
        print s.before
        s.logout()
    
if __name__ == "__main__":
    main()