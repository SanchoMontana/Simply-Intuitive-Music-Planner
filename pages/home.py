from PyQt6.QtWidgets import *
from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtCore import Qt


class HomeScreen(QMainWindow):
    def __init__(self, dimensions):
        super().__init__()
        self.dimensions = dimensions
        self.resize(dimensions[0], dimensions[1])
        self.setWindowTitle("S.I.M.P")
        page_layout = QVBoxLayout()
        self.stacklayout = QStackedLayout()
        menu_buttons_layout = QHBoxLayout()
        menu_buttons_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        
        io_layout = QHBoxLayout()
        
        input_textbox = QPlainTextEdit()
        io_layout.addWidget(input_textbox)
        output_display = QWidget()
        io_layout.addWidget(output_display)
        page_layout.addLayout(menu_buttons_layout)
        page_layout.addLayout(self.stacklayout)
        io_widget = QWidget()
        io_widget.setLayout(io_layout)
        self.stacklayout.addWidget(io_widget)
        self.stacklayout.addWidget(Color("blue"))
        self.stacklayout.addWidget(Color("green"))
        ########## MENU BUTTONS ##########
        button = QPushButton("Create")
        button.pressed.connect(self.activate_tab_io)
        menu_buttons_layout.addWidget(button)

        button = QPushButton("Retrieve")
        button.pressed.connect(self.activate_tab_retrieval)
        menu_buttons_layout.addWidget(button)

        button = QPushButton("HulaHoop")
        button.pressed.connect(self.activate_tab_print)
        menu_buttons_layout.addWidget(button)
        ##################################
        widget = QWidget()
        widget.setLayout(page_layout)
        self.setCentralWidget(widget)

    def activate_tab_io(self):
        self.stacklayout.setCurrentIndex(0)
    
    def activate_tab_retrieval(self):
        self.stacklayout.setCurrentIndex(1)
    
    def activate_tab_print(self):
        self.stacklayout.setCurrentIndex(2)
        

class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)