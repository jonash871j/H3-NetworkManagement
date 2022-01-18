import snmp
import ssh
import os

sshConnection = ssh.SshConnection('192.168.1.1', 'admin', 'cisco', 'cisco')
snmpConnection = snmp.SnmpConnection('192.168.1.1', 'ciscolab', 'admin', 'cisco', 'cisco')

def portInterfaces():
    while 1:
        sshConnection.gotoPrivilegedExec()

        print('-- Port interfaces')
        print(sshConnection.sendCommand('show ip int brief'))
        print()

        print('a. Open port')
        print('b. Close port')
        print('c. Assign port ip')
        print('d. Remove port ip')
        print('e. Go back')
        print()
        
        choice = input('Choice: ');
        if choice == 'a':
            interface = input('Interface: ')
            sshConnection.gotoInterface(interface)
            sshConnection.sendCommand("no shutdown")
        elif choice == 'b':
            interface = input('Interface: ')
            sshConnection.gotoInterface(interface)
            sshConnection.sendCommand("shutdown")
        elif choice == 'e':
            return;
        else:    
            print("Invalid choice " + choice)

        os.system('cls')

def main():
    sshConnection.authorize();
    snmpConnection.authorize();

    while 1:
        print('-- Network manager')
        print('a. Port interfaces')
        print('b. Exit')
        print();
        
        choice = input('Choice: ');
        os.system('cls')

        if choice == 'a':
            portInterfaces()
        elif choice == 'b':
            return;
        else:    
            print("Invalid choice " + choice)
            input();
       
        os.system('cls')
main();


#

#print(snmpConnection.get(['1.3.6.1.2.1.2.2.1.2.2']))
