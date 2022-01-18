import snmp
import ssh

sshConnection = ssh.SshConnection('192.168.1.1', 'admin', 'cisco')
sshConnection.authorize();
print(sshConnection.sendCommand("show arp"));

snmpConnection = snmp.SnmpConnection('192.168.1.1', 'ciscolab', 'admin', 'cisco', 'cisco')
snmpConnection.authorize();

print(snmpConnection.get(['1.3.6.1.2.1.2.2.1.2.2']))
