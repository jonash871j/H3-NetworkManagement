from colorama import Fore
import os
import oid

class ConsoleView:
    def __init__(self, sshConnection, snmpConnection):
        self.sshConnection = sshConnection
        self.snmpConnection = snmpConnection

    def show(self):
        while 1:
            os.system('cls')
            print('-- System info')
            print("Host name: " + self.snmpConnection.get([oid.SYS_NAME]))
            print("Details: " +  self.snmpConnection.get([oid.SYS_DESCRIPTION]))
            print();

            print('-- Network manager')
            print('a. Port interfaces')
            print('b. Change host name')
            print();
        
            choice = input('Choice: ');
            if choice == 'a':
                self.portInterfaces()
            elif choice == 'b':
                hostName = input('Host name: ')
                if len(hostName) > 0:
                    self.snmpConnection.set({oid.SYS_NAME: hostName})

    def portInterfaces(self):
        while 1:
            os.system('cls')
            print('-- Port interfaces')
            print(self.sshConnection.sendCommand('show ip int brief'))
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
                responseMsg = self.sshConnection.sendConfigCommand(["int " + interface, "no shutdown"])
            elif choice == 'b':
                interface = input('Interface: ')
                responseMsg = self.sshConnection.sendConfigCommand(["int " + interface, "shutdown"])
            elif choice == 'c':
                interface = input('Interface: ')
                ip = input('Ip: ')
                subnet = input('Subnet: ')
                responseMsg = self.sshConnection.sendConfigCommand(["int " + interface, "ip add " + ip + " " + subnet])
            elif choice == 'd':
                interface = input('Interface: ')
                responseMsg = self.sshConnection.sendConfigCommand(["int " + interface, "no ip add"])
            elif choice == 'e':
                return;

            self.showCommandResponse(responseMsg)

    def showCommandResponse(self, responseMsg):
        if responseMsg == ' ':
            return
        print(Fore.LIGHTYELLOW_EX + '- Response')
        print(responseMsg)
        print()
        input(Fore.WHITE + 'Press Enter to continue...');