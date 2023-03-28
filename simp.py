import sys
from pages import home
from PyQt6.QtWidgets import QApplication

DISPLAY_WIDTH = 1000 # Pickle unload from state file
DISPLAY_HEIGHT = 800 # Pickle unload from state file

app = QApplication(sys.argv)

window = home.HomeScreen((DISPLAY_WIDTH, DISPLAY_HEIGHT))
window.show()
app.exec()