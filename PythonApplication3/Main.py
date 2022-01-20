import threading
import time
from ssh import SshConnection
from snmp import SnmpConnection
from gui.console_view import ConsoleView
from gui.graph_window import GraphWindow

def main():
    sshConnection = SshConnection('192.168.1.1', 'admin', 'cisco', 'cisco')
    sshConnection.authorize()
    snmpConnection = SnmpConnection('192.168.1.1', 'ciscolab', 'admin', 'cisco', 'cisco')
    snmpConnection.authorize()

    consoleView = ConsoleView(sshConnection, snmpConnection)
    consoleViewThread = threading.Thread(target=consoleView.show)
    consoleViewThread.start()
    time.sleep(1)
    graphWindow = GraphWindow(sshConnection, snmpConnection)
    graphWindow.show()
main();
