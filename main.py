#!/usr/local/bin/python3
import sys
from netmiko import ConnectHandler
from getpass import getpass
print("Enter the username to access the servers ?")
username=input()
print("Enter the password to access the servers ?")
userpassword=getpass()
print("Enter the new password for user "+username+" ?")
newuserpassword=getpass()
print("Enter the new password for root ?")
newrootpassword=getpass()
with open('Servers IPs') as f:
    while True:
        line = f.readline()
        if not line:
            break
        try:
             net_connect = ConnectHandler(device_type='linux',
                                         ip=line,
                                         username=username, password=userpassword,
                                         port='22', secret=userpassword, verbose=False)
             net_connect.enable(cmd="sudo -i", pattern='password')
        except Exception:
             print("SSH connection failed")
        try:
             # echo 'user:passwd' | sudo chpasswd
             changerootpassword = net_connect.send_command("echo 'root:"+newrootpassword+"' | sudo chpasswd")
             print("root password changed successfully.")
             changeuserpassword = net_connect.send_command("echo '"+username+":" + newuserpassword + "' | sudo chpasswd")
             print("user password changed successfully.")
             net_connect.disconnect()
             print("Done on server: "+line)
        except:
             print("Command failed")