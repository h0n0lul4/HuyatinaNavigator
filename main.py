import sys

# ==============================
# Импорт библиотек Qt
# ==============================

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

# ==============================
# Создание приложения
# ==============================

app = QApplication(sys.argv)

# ==============================
# Главное окно браузера
# ==============================

window = QMainWindow()
window.setWindowTitle("Хуятина Навигатор")
window.resize(1200, 800)

# ================================
# Сам браузер и начальная страница
# ================================

browser = QWebEngineView()
browser.setUrl(QUrl("https://google.com"))

# ==============================
# Верхняя панель
# ==============================

address_bar = QLineEdit()
address_bar.setPlaceholderText("Введите адрес сайта...")

back_button = QPushButton("←")
forward_button = QPushButton("→")
go_button = QPushButton("експлорировать")

top_bar = QHBoxLayout()
top_bar.addWidget(back_button)
top_bar.addWidget(forward_button)
top_bar.addWidget(address_bar)
top_bar.addWidget(go_button)

# ==================================
# так называеиый 7-8 юзер интерфейс
# ==================================

layout = QVBoxLayout()
layout.addLayout(top_bar)
layout.addWidget(browser)

container = QWidget()
container.setLayout(layout)

window.setCentralWidget(container)

# ==============================
# Подключение событий
# ==============================

def open_site():
    browser.setUrl(QUrl(address_bar.text()))
go_button.clicked.connect(open_site)
back_button.clicked.connect(browser.back)
forward_button.clicked.connect(browser.forward)
address_bar.returnPressed.connect(open_site)
browser.urlChanged.connect(
    lambda url: address_bar.setText(url.toString())
)

# ==============================
# О браузере
# ==============================

def about():
    dialog = QDialog(window)
    dialog.setWindowTitle("О программе")
    dialog.resize(400, 300)

    layout = QVBoxLayout()

    pixmap = QPixmap("assets/images/logo.png")

    image = QLabel()
    image.setPixmap(
        pixmap.scaled(
            300,
            212,
        )
    )

    layout.addWidget(image)

    info = QLabel("""
    <h2>Хуятина Навигатор</h2>

    <b>Версия:</b> Type 0.0.0 "Tyrolean Music Station"<br>
    <b>Создал:</b> honolula<br>
    <b>Создан:</b> 2026<br>
    <b>Adress me:</b> honolula.neocities.org
    """)

    layout.addWidget(info)

    dialog.setLayout(layout)

    dialog.exec()
    
# ==============================
# Верхнее меню
# ==============================

menu = window.menuBar()

help_menu = menu.addMenu("Справка")

about_action = help_menu.addAction("О браузере")

about_action.triggered.connect(about)

# ==============================
# Запуск программы
# ==============================

window.show()

app.exec()