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
        self.connection.enable()

    def sendCommand(self, command):
        return self.connection.send_command(command)
    
    def sendConfigCommand(self, command):
        return self.connection.send_config_set(command)
       