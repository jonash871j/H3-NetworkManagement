import netmiko

class SshConnection:
    def __init__(self, ip, username, password):
        self.device = {
            'host': ip,
            'username': username,
            'password': password,
            'device_type': 'cisco_ios'
        }

    def authorize(self):
        self.connection = netmiko.Netmiko(**self.device)

    def sendCommand(self, command):
        return self.connection.send_command(command)