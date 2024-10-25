from PySide6.QtWidgets import QApplication, QSystemTrayIcon, QMenu, QMainWindow
from PySide6.QtCore import QSize, QThread
from PySide6.QtGui import QIcon
from interface import Ui_MainWindow

import resources_rc, sys
import duck_dns, config, datetime, time

config.setUp()


class window_Class(QMainWindow):
    def __init__(self):
        super(window_Class, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.connect_Buttons()

    def import_Config(self):
        self.ui.domain_LineEdit.setText(str(config.domain))
        self.ui.token_LineEdit.setText(str(config.token))
        self.ui.interval_LineEdit.setText(str(config.interval))

    def apply_Configurations(self):
        self.hide()
        config.enter_Domain(self.ui.domain_LineEdit.text())
        config.enter_Token(self.ui.token_LineEdit.text())
        config.enter_Interval(self.ui.interval_LineEdit.text())
        tray_App.update_IP_Adress()

    def connect_Buttons(self):
        self.ui.apply_Button.clicked.connect(self.apply_Configurations)
        self.ui.web_Button.clicked.connect(lambda: duck_dns.open_Site())

    def closeEvent(self, event):
        self.hide()
        event.ignore()


class tray_App_Class(QSystemTrayIcon):
    def __init__(self, parent=None):
        super().__init__(parent)

        tray_icon = QIcon()
        tray_icon.addFile(u":/images/resources/tray.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.setIcon(tray_icon)

        self.window = window_Class()
        self.set_Up_Menu()
        
        self.activated.connect(lambda event: self.open_Window() if event == QSystemTrayIcon.DoubleClick else None)

    def open_Window(self):
        self.window.import_Config()
        self.window.show()

    def update_Status(self, public_IP, response):
        hour = datetime.datetime.now().strftime("%H:%M")
        self.setToolTip(f"IP adress: {public_IP}" "\n"
                        f"Last update: {hour}" "\n"
                        f"Update status: {response}" "\n"
                        f"Update interval: {config.interval} minute(s)")

    def update_IP_Adress(self):
        if config.token == "token":
            response = "Unknown"
        else:
            response = duck_dns.update_IP(config.domain, config.token)
        self.update_Status(duck_dns.get_IP(), response)

    def set_Up_Menu(self):
        self.menu = QMenu()
        self.menu.setTitle("Duck DNS IP Updater")
        self.setContextMenu(self.menu)

        button_Open = self.menu.addAction("Configurations")
        button_Open.triggered.connect(self.open_Window)

        button_Update = self.menu.addAction("Update IP now")
        button_Update.triggered.connect(self.update_IP_Adress)

        button_Exit = self.menu.addAction("Exit")
        button_Exit.triggered.connect(self.close_App)

    def close_App(self):
        self.window.hide()
        updater.stop()
        updater.wait()
        QApplication.quit()

class updater_Thread(QThread):
    def __init__(self):
        super().__init__()
        self.program = True
        self.counter = 0

    def stop(self):
        self.program = False

    def run(self):
        while self.program == True:
            time.sleep(2)
            self.counter += 2
            if self.counter >= (config.interval * 60):
                tray_App.update_IP_Adress()
                self.counter = 0

app = QApplication(sys.argv)
tray_App = tray_App_Class()
updater = updater_Thread()

tray_App.update_IP_Adress()
updater.start()
tray_App.show()

sys.exit(app.exec())