import os
import threading
import logging
import PySimpleGUI as sg
import subprocess
import platform
from urllib.parse import urlsplit


layout = [
            [
                sg.Button("Connect", key="connect_button", pad=(10, 20), button_color=('white', '#007339'), disabled=False),
                sg.Button("Close", button_color=('white', 'firebrick4')),
                sg.Text("Offline",
                        pad=(50, 23),
                        text_color="white",
                        background_color="red",
                        justification="center",
                        border_width=1,
                        visible=False,
                        key="-STATUS-",
                        size=(14, 1),
                        )

            ],
        ]

window = sg.Window("Connector", layout)



def construct_pingable_host(host: str) -> str:
    """Receives a hostname and returns a pingable hostname

    Eg: in: 'https://ec2-3-223-150-210.compute-1.amazonaws.com/'
        out: 'ec2-3-223-150-210.compute-1.amazonaws.com

        Eg: in: 'https://ec2-3-223-150-210.compute-1.amazonaws.com'
        out: 'ec2-3-223-150-210.compute-1.amazonaws.com

        Eg: in: '//ec2-3-223-150-210.compute-1.amazonaws.com/'
        out: 'ec2-3-223-150-210.compute-1.amazonaws.com

        in: test.example.com
        out: test.example.com
    """
    url = urlsplit(host)
    netloc = url.netloc
    path = url.path[:-1] if url.path.endswith("/") else url.path
    return f"{netloc}{path}"


def ping(host):
    """
    Returns True if host responds to a ping request
    """
    # Ping parameters as function of OS
    ping_str = "-n 1" if platform.system().lower() == "windows" else "-c 1"
    args = "ping " + " " + ping_str + " " + construct_pingable_host(host)
    need_sh = platform.system().lower() != "windows"
    # Ping
    #return subprocess.call(args, shell=need_sh, stdout=subprocess.PIPE, stderr=subprocess.STDOUT) == 0
    retval = subprocess.call(args, shell=need_sh, stdout=subprocess.PIPE, stderr=subprocess.STDOUT) == 0
    window.write_event_value('-PINGDONE-', retval)


def threaded_ping(host):
    threading.Thread(target=ping, args=(host,), daemon=True).start()


class GUI:
    def __init__(self, window):
        self.window = window

        self._status_config = {
            "online": {"msg": "Online", "bg": "green", "text_color": "white"},
            "offline": {"msg": "Offline", "bg": "red", "text_color": "white"},
            "reconnecting": {"msg": "Reconnecting..", "bg": "white", "text_color": "black"},
            "connecting": {"msg": "Connecting...", "bg": "white", "text_color": "black"},
        }

    def enable_element(self, key):
        el = self.window.FindElement(key, silent_on_error=True)
        if el:
            el.update(disabled=False)

    def set_layout_connecting_state(self):
        self.update_status_message("connecting")
        self.disable_element("connect_button")

    def update_status_message(self, status: str):
        el = self.window["-STATUS-"]
        status_data = self._status_config.get(status)
        el.update(status_data.get("msg"))
        el.update(background_color=status_data.get("bg"))
        el.update(text_color=status_data.get("text_color"))
        el.update(visible=True)

    def disable_element(self, key):
        el = self.window.FindElement(key, silent_on_error=True)
        if el:
            el.update(disabled=True)

    def set_layout_disconnected_state(self):
        self.enable_element("connect_button")
        self.update_status_message("offline")

    def close(self):
        self.window.close()

    @staticmethod
    def open_popup(message):
        sg.Popup("Error", message, modal=True)


class Handler:
    def __init__(self, gui):
        self.gui = gui

    def set_connecting_state(self):
        self.gui.set_layout_connecting_state()

    def set_disconnected_state(self):
        self.gui.set_layout_disconnected_state()

    def on_destroy(self, *args):
        self.gui.close()

    def is_server_reachable(self, host):
        # If there is ping, check if connector can connect
        return ping(host)
        #return threaded_ping(host)

    def show_error(self, message):
        self.gui.open_popup(message)


def main():
    gui = GUI(window)
    handler = Handler(gui)

    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        # If there are no GUI interactions, loop every amount of ms specified in timeout
        event, values = gui.window.read(timeout=5000)

        if event in (sg.WIN_CLOSED, "Close"):
            handler.on_destroy()
            break
        elif event == "connect_button":
            # TODO: This is not updating before executing is_server_reachable
            handler.set_connecting_state()
            window.refresh()
            handler.is_server_reachable("3.3.3.3")
        elif event == "-PINGDONE-":
            if values.get(event):
                handler.show_error("Server Reachable")
            else:
                handler.show_error("Server not Reachable")
                handler.set_disconnected_state()

if __name__ == "__main__":
    main()

