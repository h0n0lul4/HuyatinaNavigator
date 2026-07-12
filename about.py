from PySide6.QtWidgets import (
    QDialog,
    QLabel,
    QVBoxLayout,
    QWidget,
    QTabWidget,
)

from PySide6.QtGui import QPixmap


def show_about(parent):
    dialog = QDialog(parent)
    dialog.setWindowTitle("О программе")
    dialog.resize(450, 450)

    layout = QVBoxLayout()

    tabs = QTabWidget()

    # ==============================
    # Вкладка "Информация"

    info_tab = QWidget()
    info_layout = QVBoxLayout()
    info_tab.setLayout(info_layout)

    pixmap = QPixmap("assets/images/logo.png")

    image = QLabel()
    image.setPixmap(
        pixmap.scaled(
            300,
            212,
        )
    )
# колобок повесился
    info_layout.addWidget(image)

    info = QLabel("""
<h2>Хуятина Навигатор</h2>

<b>Версия:</b> Type 0.0.1 "Swedish Rhapsody"<br>
<b>Создал:</b> honolula<br>
<b>Создан:</b> 2026<br>
<b>E-mail:</b> honolula@tutanota.de
""")

    info.setWordWrap(True)
    info_layout.addWidget(info)

    # ==============================
    # Вкладка "Благодарности"

    thanks_tab = QWidget()
    thanks_layout = QVBoxLayout()
    thanks_tab.setLayout(thanks_layout)

    thanks = QLabel("""
<h2>Особая благоларность за советы, моральную поддержку и т.д</h2>

• <a href="https://thefreo.moe">Artem "TheFreo" Ushakov</a><br>
• <a href="https://bitsel.xyz/">Dennis Bitsel</a>
• <a href="https://openvk.org/gamberetto">Antonio Gamberetto</a><br>
• <a href="https://openvk.org/nek0">Pashk Neko</a>


<h3>Open Source Software</h3>

• Python — Guido van Rossum, Python Software Foundation<br>
• Qt — The Qt Company<br>
• PySide6 (Qt for Python) — Qt for Python Team, The Qt Company<br>
• Qt WebEngine — The Qt Company

<h3>Использованные инструменты</h3>

• VSCodium<br>
• Git<br>
• GitHub

<h3>Ссылки проекта</h3>

• <a href="https://github.com/h0n0lul4/HuyatinaNavigator">GitHub Repository</a><br>
""")

    thanks.setWordWrap(True)
    thanks.setOpenExternalLinks(True)

    thanks_layout.addWidget(thanks)

    # ==============================
    # вкладки

    tabs.addTab(info_tab, "Информация")
    tabs.addTab(thanks_tab, "Благодарности")

    layout.addWidget(tabs)

    dialog.setLayout(layout)

    dialog.exec()