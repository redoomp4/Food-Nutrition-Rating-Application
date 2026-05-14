import sys
import os
import webbrowser
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QVBoxLayout, QWidget, QHBoxLayout, QFrame, QSpacerItem, QSizePolicy
from PyQt5.QtCore import QFile, QTextStream, QSize, Qt
from PyQt5.QtGui import QFont, QIcon, QCursor, QPixmap

from sidebar_ui import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.stackedWidget.setCurrentIndex(3)
        self.ui.home_btn_2.setChecked(True)

        # ==========================================
        # 1. FIX TOP BAR (ABSOLUTE CENTER, AMAN 100%)
        # ==========================================
        self.ui.widget.setFixedHeight(120)
        
        # Perbesar Hamburger Menu yang ASLI (Tanpa menyentuh layout sama sekali)
        self.ui.change_btn.setFixedSize(70, 70)
        self.ui.change_btn.setIconSize(QSize(40, 40))

        # Sembunyikan Logo & Judul bawaan agar tidak double
        self.ui.logo_label_6.hide()
        self.ui.logo_label_7.hide()
        self.ui.logo_label_8.hide()

        # Buat container BARU sebagai overlay untuk Judul agar PASTI di tengah
        self.center_container = QWidget(self)
        center_layout = QHBoxLayout(self.center_container)
        center_layout.setSpacing(20)
        center_layout.setContentsMargins(0, 0, 0, 0)

        self.new_logo_6 = QLabel()
        self.new_logo_6.setPixmap(self.ui.logo_label_6.pixmap())
        self.new_logo_6.setScaledContents(True)
        self.new_logo_6.setFixedSize(80, 80)
        center_layout.addWidget(self.new_logo_6)

        self.new_title = QLabel("Selamat Datang Di Ngilers")
        self.new_title.setFont(QFont("Segoe UI", 32, QFont.Bold))
        self.new_title.setAlignment(Qt.AlignCenter)
        self.new_title.setStyleSheet("color: #2C3E50;")
        center_layout.addWidget(self.new_title)

        self.new_logo_8 = QLabel()
        self.new_logo_8.setPixmap(self.ui.logo_label_8.pixmap())
        self.new_logo_8.setScaledContents(True)
        self.new_logo_8.setFixedSize(80, 80)
        center_layout.addWidget(self.new_logo_8)
        
        self.center_container.show()
        self.center_container.raise_()

        # ==========================================
        # 2. FIX SIDEBAR & EXIT BUTTON
        # ==========================================
        self.ui.full_menu_widget.setMinimumWidth(320)
        self.ui.full_menu_widget.setMaximumWidth(320)
        
        icon_size = QSize(35, 35)
        self.ui.home_btn_2.setIconSize(icon_size)
        self.ui.customers_btn_2.setIconSize(icon_size)
        
        self.ui.exit_btn_2.setParent(self.ui.full_menu_widget)
        self.ui.exit_btn_2.setIconSize(icon_size)
        self.ui.exit_btn_2.setMinimumHeight(60)
        if self.ui.verticalLayout_4.indexOf(self.ui.exit_btn_2) == -1:
            self.ui.verticalLayout_4.addWidget(self.ui.exit_btn_2)

        # Scaling Dashboard
        scale = 1.8
        for child in self.ui.widget_2.children():
            if hasattr(child, 'geometry'):
                g = child.geometry()
                child.setGeometry(int(g.x()*scale), int(g.y()*scale), int(g.width()*scale), int(g.height()*scale))
            if isinstance(child, QPushButton):
                isize = child.iconSize()
                child.setIconSize(QSize(int(isize.width()*scale), int(isize.height()*scale)))

        # ==========================================
        # 3. ABOUT ME (RIDHO ALFAROD EDITION)
        # ==========================================
        self.about_btn = QPushButton("About Me")
        self.about_btn.setCheckable(True)
        self.about_btn.setAutoExclusive(True)
        
        about_icon = QIcon()
        about_icon.addPixmap(QPixmap(":/icon/icon/group-32.ico"), QIcon.Normal, QIcon.Off)
        about_icon.addPixmap(QPixmap(":/icon/icon/group-48.ico"), QIcon.Normal, QIcon.On)
        self.about_btn.setIcon(about_icon)
        
        self.about_btn.setIconSize(icon_size)
        self.ui.verticalLayout_2.addWidget(self.about_btn)

        if hasattr(self.ui, 'gridLayout_6'):
            while self.ui.gridLayout_6.count():
                item = self.ui.gridLayout_6.takeAt(0)
                if item.widget(): item.widget().deleteLater()
            
            about_widget = QWidget()
            vbox = QVBoxLayout(about_widget)
            vbox.setContentsMargins(60, 60, 60, 60)
            vbox.setSpacing(35)

            name_label = QLabel("Muhammad Ridho Alfarod")
            name_label.setFont(QFont("Segoe UI", 42, QFont.Bold))
            name_label.setStyleSheet("color: #2C3E50;")
            vbox.addWidget(name_label)

            sub_title = QLabel("🚀 IT Enthusiast | ITK Student")
            sub_title.setFont(QFont("Segoe UI", 20))
            sub_title.setStyleSheet("color: #E67E22; font-style: italic;")
            vbox.addWidget(sub_title)

            line = QFrame()
            line.setFrameShape(QFrame.HLine)
            line.setFixedHeight(3)
            line.setStyleSheet("background-color: #BDC3C7;")
            vbox.addWidget(line)

            # Social Section - MENGGUNAKAN EMOJI KARENA ICON TIDAK TERBACA
            social_layout = QHBoxLayout()
            social_layout.setSpacing(30)
            social_layout.setAlignment(Qt.AlignLeft)

            # LINKEDIN
            btn_li = self.create_social_btn("LinkedIn", ":/icon/icon/linkedin.png", "https://www.linkedin.com/in/muhridhoalfarod/")
            social_layout.addWidget(btn_li)

            # INSTAGRAM
            btn_ig = self.create_social_btn("Instagram", ":/icon/instagram.jpg", "https://instagram.com/rdhoalfrd")
            social_layout.addWidget(btn_ig)

            # YOUTUBE
            btn_yt = self.create_social_btn("YouTube", ":/icon/youtube.png", "https://youtube.com/@rdhoalfrd")
            social_layout.addWidget(btn_yt)

            vbox.addLayout(social_layout)
            
            desc = QLabel(
                "Halo! Nama saya Ridho Alfarod. Saya adalah mahasiswa Institut Teknologi Kalimantan "
                "yang memiliki passion besar dalam pengembangan aplikasi berbasis Python dan "
                "desain antarmuka pengguna (UI/UX).\n\nAplikasi Ngilers ini adalah proyek portofolio "
                "saya untuk mata kuliah Algoritma Pemrograman. Senang bisa terhubung dengan Anda!"
            )
            desc.setFont(QFont("Segoe UI", 16))
            desc.setWordWrap(True)
            desc.setStyleSheet("color: #34495E; line-height: 160%;")
            vbox.addWidget(desc)
            vbox.addStretch()

            self.ui.gridLayout_6.addWidget(about_widget, 0, 0)

        # Koneksi navigasi
        self.ui.home_btn_2.toggled.connect(lambda c: self.ui.stackedWidget.setCurrentIndex(3) if c else None)
        self.ui.customers_btn_2.toggled.connect(lambda c: self.ui.stackedWidget.setCurrentIndex(3) if c else None)
        self.about_btn.toggled.connect(lambda c: self.ui.stackedWidget.setCurrentIndex(4) if c else None)

    def create_social_btn(self, name, icon_path, url):
        btn = QPushButton(f" {name}")
        btn.setIcon(QIcon(icon_path))
        btn.setIconSize(QSize(45, 45))
        btn.setCursor(QCursor(Qt.PointingHandCursor))
        btn.setMinimumSize(220, 80)
        btn.setStyleSheet("""
            QPushButton {
                background-color: #2C3E50;
                color: white;
                font-size: 18px;
                font-weight: bold;
                border-radius: 20px;
            }
            QPushButton:hover {
                background-color: #E67E22;
                border: 2px solid #D35400;
            }
        """)
        btn.clicked.connect(lambda: webbrowser.open(url))
        return btn

    def resizeEvent(self, event):
        super().resizeEvent(event)
        if hasattr(self, 'center_container'):
            self.center_container.adjustSize()
            # Kita ingin posisinya tepat di tengah MainWindow.
            # Lebar MainWindow = self.width()
            # Tengah layar global = self.width() // 2
            # Posisi x ideal
            target_x = (self.width() // 2) - (self.center_container.width() // 2)
            
            self.center_container.move(target_x, 20)


if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    app = QApplication(sys.argv)
    
    style_file = QFile("style.qss")
    if style_file.exists():
        style_file.open(QFile.ReadOnly | QFile.Text)
        app.setStyleSheet(QTextStream(style_file).readAll())

    window = MainWindow()
    window.showMaximized()
    sys.exit(app.exec())
