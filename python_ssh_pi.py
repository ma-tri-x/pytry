import pxssh
import getpass

#class ip_Exception(Exception):
    #'''If wrong formatted ip was entered'''
    #def __init__(self,

class address:
    ip_prefix = "192.168.1"
    def __init__(self,user,hostip,pswd):
        self.suffix = 0
        self.user = user
        ip_prefix = hostip
        self.host_ip = "{}.{}".format(ip_prefix,self.suffix)
        self.password = pswd
    
    #def check(self):
    def next_ip(self):
        self.suffix+=1
        self.host_ip = "{}.{}".format(ip_prefix,self.suffix)
        
    def ip(self):
        return self.host_ip
        
    def us(self):
        return self.user
        
    def pwd(self):
        return self.pwd
        

def main():
    s = pxssh.pxssh()
    hostname = raw_input('host-ip (without last number): ')
    username = raw_input('username: ')
    password = getpass.getpass('password: ')
    cl = address(username,hostname,password)
    for i in range(256):
        print i,":"
        try:                                                            
            s.login (cl.us,cl.ip,cl.pwd)
        except pxssh.ExceptionPxssh, e:
            print "pxssh failed on login."
            print str(e)
            cl.next_ip
            pass
        print "Login Success"
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