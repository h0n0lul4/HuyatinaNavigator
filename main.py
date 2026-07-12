import sys
import json

# ==============================
# Импорт библиотек Qt


from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLineEdit,
    QPushButton,
    QMessageBox,
    QDialog,
    QLabel,
)
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtCore import QUrl
from PySide6.QtGui import QPixmap
from about import show_about

# ==============================
# Константы браузера


HOME_PAGE = "https://google.com"
with open("settings.json", "r", encoding="utf-8") as file:
    settings = json.load(file)

HOME_PAGE = settings["home_page"]
def save_settings():
    with open("settings.json", "w", encoding="utf-8") as file:
        json.dump(
            settings,
            file,
            ensure_ascii=False,
            indent=4
        )

# ==============================
# Создание приложения


app = QApplication(sys.argv)

# ==============================
# Главное окно браузера


window = QMainWindow()
window.setWindowTitle("Хуятина Навигатор")
window.resize(1200, 800)

# ================================
# Сам браузер и начальная страница


browser = QWebEngineView()
browser.setUrl(QUrl(HOME_PAGE))

# ==============================
# Верхняя панель


address_bar = QLineEdit()
address_bar.setPlaceholderText("Пойти на...")

back_button = QPushButton("←")
forward_button = QPushButton("→")
reload_button = QPushButton("⟳")
home_button = QPushButton("⌂")
go_button = QPushButton("експлорировать")

top_bar = QHBoxLayout()
top_bar.addWidget(back_button)
top_bar.addWidget(forward_button)
top_bar.addWidget(reload_button)
top_bar.addWidget(home_button)
top_bar.addWidget(address_bar)
top_bar.addWidget(go_button)

# ==================================
# так называеиый 7-8 юзер интерфейс


layout = QVBoxLayout()
layout.addLayout(top_bar)
layout.addWidget(browser)

container = QWidget()
container.setLayout(layout)

window.setCentralWidget(container)

# ==============================
# Подключение событий


def open_site():
    browser.setUrl(QUrl(address_bar.text()))

go_button.clicked.connect(open_site)

back_button.clicked.connect(browser.back)
forward_button.clicked.connect(browser.forward)
reload_button.clicked.connect(browser.reload)

home_button.clicked.connect(
    lambda: browser.setUrl(QUrl(settings["home_page"]))
)

address_bar.returnPressed.connect(open_site)

browser.urlChanged.connect(
    lambda url: address_bar.setText(url.toString())
)

# ==============================
# Настройке


def open_settings():
    dialog = QDialog(window)
    dialog.setWindowTitle("Настройки")
    dialog.resize(450, 120)

    layout = QVBoxLayout()

    home_page_edit = QLineEdit()
    home_page_edit.setText(settings["home_page"])

    save_button = QPushButton("Сохранить")

    layout.addWidget(QLabel("Домашняя страница:"))
    layout.addWidget(home_page_edit)
    layout.addWidget(save_button)

    dialog.setLayout(layout)

    def save():
        settings["home_page"] = home_page_edit.text()
        save_settings()
        dialog.accept()

    save_button.clicked.connect(save)

    dialog.exec()
    
# ==============================
# Верхнее меню


menu = window.menuBar()

settings_menu = menu.addMenu("ОпцЫи")

settings_action = settings_menu.addAction("Открыть опцЫи")

settings_action.triggered.connect(open_settings)

help_menu = menu.addMenu("Справка")

about_action = help_menu.addAction("О браузере")

about_action.triggered.connect(
    lambda: show_about(window)
)

# ==============================
# Запуск программы


window.show()

app.exec()