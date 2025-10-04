try :
	from PySide6 import QtCore, QtGui, QtWidgets
	from shiboken6 import wrapInstance
except:
	from PySide2 import QtCore, QtGui, QtWidgets
	from shiboken2 import wrapInstance
import maya.OpenMayaUI as omui

ROOT_RESOURCE_DIR = 'C:/Users/ICT68/Documents/maya/2025/scripts/myStyleTool/resource'

class MyStyleToolDialog(QtWidgets.QDialog):
	def __init__(self, parent=None):
		super().__init__(parent)


		self.setWindowTitle('My Tool')
		self.resize(300,300)

		self.mainLayout = QtWidgets.QVBoxLayout()
		self.setLayout(self.mainLayout)
		self.setStyleSheet('background-color: qLineargradient(x1:0,y1:0,x2:1, stop:0 #191970, stop:1 #483D8B);')

		self.imageLabel = QtWidgets.QLabel()
		self.imagePixmap = QtGui.QPixmap(f"{ROOT_RESOURCE_DIR}/image/matcha.png")
		self.imageLabel.setPixmap(self.imagePixmap)
		self.mainLayout.addWidget(self.imageLabel)



		self.nameLayout = QtWidgets.QHBoxLayout()
		self.mainLayout.addLayout(self.nameLayout)
		self.nameLabel = QtWidgets.QLabel('Name:')
		self.nameLineEdit = QtWidgets.QLineEdit()
		self.nameLayout.addWidget(self.nameLabel)
		self.nameLayout.addWidget(self.nameLineEdit)

		self.buttonLayout = QtWidgets.QHBoxLayout()
		self.mainLayout.addLayout(self.buttonLayout)
		self.createButton = QtWidgets.QPushButton('Create')
		self.createButton.setStyleSheet(
			'''
				QPushButton {
					background-color: #6A5ACD;
					color: white;
					border-radius: 10px;
					font-size: 16px;
					padding: 8px;
					font-family: Papyrus;
					font-weight: blod;
				}
				QPushButton:hover{
					background-color: #1E90FF;

				}
			'''
			)
		self.cancelButton = QtWidgets.QPushButton('Cancel')
		self.cancelButton.setStyleSheet(
			'''
				QPushButton {
					background-color: #B22222;
					color: white;
					border-radius: 10px;
					font-size: 16px;
					padding: 8px;
					font-family: Papyrus;
					font-weight: blod;
				}
				QPushButton:hover{
					background-color: #FFA500;

				}
			'''
			)
		self.buttonLayout.addWidget(self.createButton)
		self.buttonLayout.addWidget(self.cancelButton)

def run():
	global ui
	try:
		ui.close()
	except:
		pass

	ptr = wrapInstance(int(omui.MQtUtil.mainWindow()), QtWidgets.QWidget)
	ui = MyStyleToolDialog(parent=ptr)
	ui.show()

