from infi.systray import SysTrayIcon
import sys
import subprocess
import os

class Tray:
    def __init__(self):
        pass

    @staticmethod
    def bye(sysTrayIcon):
        print("Program is closed")
        os.system('cmd /c "taskkill /f /im pygui_networkwidelicense.exe"')

    def initializeSystray(self):
        # menu_options = (('Say Hello', "hello.ico", self.say_hello),
        #                 )
        systray = SysTrayIcon("G:\\RAT-Automation-src\\Network_Wide_License\\images\\download.ico", "networkwidelicense", None, on_quit=self.bye, default_menu_index=0)
        return systray
