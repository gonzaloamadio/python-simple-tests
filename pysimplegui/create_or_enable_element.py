import json
import PySimpleGUI as sg
REMOTE_HOSTS = '{"host1": "192.160.1.1", "host2": "192.168.0.2"}'


layout = [  [sg.Text('My Window')],
            [sg.Text('Click to add remote hosts information'), sg.B('+', key='-B1-')],
            [sg.Text('Click to delete remote hosts information'), sg.B('+', key='-B2-')],
            [sg.Button('Button'), sg.Button('Exit')]  ]


def enable_or_create_remote_hosts(self, remote_hosts):
    # This is the right way
    if "frame_remote_hosts" in self.window.AllKeysDict:
        el = self.window.FindElement("frame_remote_hosts")
        el.update(visible=True)
    else:
        remote_hosts_text_elements = [[sg.T(f'{host}: {ip}')] for host, ip in remote_hosts.items()]
        remote_hosts_element = [sg.Frame('Remote Hosts', remote_hosts_text_elements, key='frame_remote_hosts')]
        self.window.extend_layout(self.window, [remote_hosts_element])

def enable_or_create_remote_hosts(window, remote_hosts):
    # OLD VERSION
    el = window.FindElement("frame_remote_hosts", silent_on_error=True)
    if not el.Type == "error":
        el.update(visible=True)
    else:
        remote_hosts = json.loads(remote_hosts)
        remote_hosts_text_elements = [[sg.T(f'{host}: {ip}')] for host, ip in remote_hosts.items()]
        remote_hosts_element = [sg.Frame('Remote Hosts', remote_hosts_text_elements, key='frame_remote_hosts')]
        window.extend_layout(window, [remote_hosts_element])

def visibilize_element(self, key, visible):
    # This one is the correct way
    if key in self.window.AllKeysDict:
        el = self.window.FindElement(key)
        el.update(visible=visible)

def unvisibilize_element(window, key):
#    window[key](visible=False)
    el = window.FindElement(key, silent_on_error=True)
    el.update(visible=False)


window = sg.Window('Window Title', layout)
while True:             # Event Loop
    event, values = window.read()
    print(event, values)
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    if event == '-B1-':
        enable_or_create_remote_hosts(window, REMOTE_HOSTS)
    if event == '-B2-':
        unvisibilize_element(window, "frame_remote_hosts")
window.close()


