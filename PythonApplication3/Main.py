from colorama import Fore
import snmp
import ssh
import os
import graph
import threading
import random

sshConnection = ssh.SshConnection('192.168.1.1', 'admin', 'cisco', 'cisco')
snmpConnection = snmp.SnmpConnection('192.168.1.1', 'ciscolab', 'admin', 'cisco', 'cisco')

def showCommandResponse(responseMsg):
    if responseMsg == ' ':
        return
    print(Fore.LIGHTYELLOW_EX + '- Response')
    print(responseMsg)
    print()
    input(Fore.WHITE + 'Press Enter to continue...');

def portInterfaces():
    while 1:
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
        responseMsg = ' ';
        if choice == 'a':
            interface = input('Interface: ')
            responseMsg = sshConnection.sendConfigCommand(["int " + interface, "no shutdown"])
        elif choice == 'b':
            interface = input('Interface: ')
            responseMsg = sshConnection.sendConfigCommand(["int " + interface, "shutdown"])
        elif choice == 'c':
            interface = input('Interface: ')
            ip = input('Ip: ')
            subnet = input('Subnet: ')
            responseMsg = sshConnection.sendConfigCommand(["int " + interface, "ip add " + ip + " " + subnet])
        elif choice == 'd':
            interface = input('Interface: ')
            responseMsg = sshConnection.sendConfigCommand(["int " + interface, "no ip add"])
        elif choice == 'e':
            return;

        showCommandResponse(responseMsg)
        os.system('cls')

graphWindow = graph.Graph()

def thread_function():
    sshConnection.authorize()
    #snmpConnection.authorize()

    i = 0
    while 1:
        print('-- System info')
        #print(snmpConnection.get('.1.3.6.1.2.1.1.3.0'))
        #print(snmpConnection.get('.1.3.6.1.2.1.1.1.0'))
        print();

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
       
        os.system('cls')
        i = random.randrange(0, 100);
        graphWindow.addValue(i)

def main():
    x = threading.Thread(target=thread_function)
    x.start();
    
    graphWindow.initialize()
    graphWindow.show()
main();
