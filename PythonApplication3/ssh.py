import netmiko

class SshConnection:
    def __init__(self, ip, username, password, secret):
        self.device = {
            'host': ip,
            'username': username,
            'password': password,
            'secret': secret,
            'device_type': 'cisco_ios'
        }

    def authorize(self):
        self.connection = netmiko.Netmiko(**self.device)

    def sendCommand(self, command):
        return self.connection.send_command(command)
    
    def gotoPrivilegedExec(self):
        self.connection.enable()

    def gotoConfig(self):
        self.gotoPrivilegedExec()
        self.connection.config_mode()

    def gotoInterface(self, interface):
        self.gotoConfig()
        self.sendCommand('interface ' + interface)