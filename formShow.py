from PySide import QtCore,QtGui
from ui_caculation import Ui_Dialog
import sys


class uiShow(QtGui.QDialog):

    def __init__(self,parent=None):
        QtGui.QDialog.__init__(self,parent)
        self.ui=Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton1.clicked.connect(self.pushbutton1Clicked)
        
    def pushbutton1Clicked(self):
        self.ui.textEdit.setText('1')

    
def main():
    app = QtGui.QApplication(sys.argv)
    window = uiShow()
    window.show()
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    main()
