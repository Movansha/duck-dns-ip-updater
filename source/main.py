from PySide6.QtWidgets import QApplication, QSystemTrayIcon, QMenu, QMainWindow
from PySide6.QtCore import QSize, QThread
from PySide6.QtGui import QIcon
from interface import Ui_MainWindow

import resources_rc, sys
import config, duck_dns, datetime, time

config.load_cfg()


class window_Class(QMainWindow):
    def __init__(self):
        super(window_Class, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.connect_buttons()

    def import_configs(self):
        self.ui.domains_LineEdit.setText(config.domains)
        self.ui.token_LineEdit.setText(config.token)
        self.ui.interval_LineEdit.setText(str(config.interval))

    def apply_configs(self):
        self.hide()
        config.enter_domain(self.ui.domains_LineEdit.text())
        config.enter_token(self.ui.token_LineEdit.text())
        config.enter_interval(self.ui.interval_LineEdit.text())
        tray_App.update_IP_adresses()

    def connect_buttons(self):
        self.ui.apply_Button.clicked.connect(self.apply_configs)
        self.ui.web_Button.clicked.connect(lambda: duck_dns.open_Site())

    def closeEvent(self, event):
        self.hide()
        event.ignore()


class tray_app_Class(QSystemTrayIcon):
    def __init__(self, parent=None):
        super().__init__(parent)

        tray_icon = QIcon()
        tray_icon.addFile(u":/icons/resources/32x.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.setIcon(tray_icon)

        self.window = window_Class()
        self.load_menu()
        
        self.activated.connect(lambda event: self.open_window() if event == QSystemTrayIcon.Trigger else None)


    def open_window(self):
        self.window.import_configs()
        self.window.show()

    def update_status(self, response):
        hour = datetime.datetime.now().strftime("%H:%M")
        ipv4_adress = duck_dns.get_IPv4()
        ipv6_adress = duck_dns.get_IPv6()

        self.setToolTip(
                        f"IPv4 adress: {ipv4_adress}" "\n"
                        f"IPv6 adress: {ipv6_adress}" "\n"
                        f"Last update: {hour}" "\n"
                        f"Update status: {response}" "\n"
                        f"Update interval: {config.interval} minute(s)"
                        )

    def update_IP_adresses(self):
        if config.token == "token":
            response = "Unknown"
        else:
            response = duck_dns.update_IP(config.domains, config.token)

        self.update_status(response)


    def load_menu(self):
        self.menu = QMenu()
        self.menu.setTitle("Duck DNS IP Updater")
        self.setContextMenu(self.menu)

        button_open = self.menu.addAction("Configurations")
        button_open.triggered.connect(self.open_window)

        button_update = self.menu.addAction("Update IP adresses now")
        button_update.triggered.connect(self.update_IP_adresses)

        button_exit = self.menu.addAction("Exit")
        button_exit.triggered.connect(self.close_App)

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
                tray_App.update_IP_adresses()
                self.counter = 0


app = QApplication(sys.argv)
tray_App = tray_app_Class()
updater = updater_Thread()

tray_App.update_IP_adresses()
updater.start()
tray_App.show()

sys.exit(app.exec())
