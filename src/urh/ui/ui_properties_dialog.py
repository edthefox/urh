#
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_DialogLabels(object):
    def setupUi(self, DialogLabels):
        DialogLabels.setObjectName("DialogLabels")
        DialogLabels.resize(714, 463)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(DialogLabels)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.splitter = QtWidgets.QSplitter(parent=DialogLabels)
        self.splitter.setStyleSheet("QSplitter::handle:vertical {\n"
"margin: 4px 0px;\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0, \n"
"stop:0 rgba(255, 255, 255, 0), \n"
"stop:0.5 rgba(100, 100, 100, 100), \n"
"stop:1 rgba(255, 255, 255, 0));\n"
"    image: url(:/icons/icons/splitter_handle_horizontal.svg);\n"
"}")
        self.splitter.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.splitter.setHandleWidth(6)
        self.splitter.setChildrenCollapsible(False)
        self.splitter.setObjectName("splitter")
        self.groupBoxSettings = QtWidgets.QGroupBox(parent=self.splitter)
        self.groupBoxSettings.setObjectName("groupBoxSettings")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBoxSettings)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tblViewProtoLabels = ProtocolLabelTableView(parent=self.groupBoxSettings)
        self.tblViewProtoLabels.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.ExtendedSelection)
        self.tblViewProtoLabels.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectItems)
        self.tblViewProtoLabels.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.tblViewProtoLabels.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.tblViewProtoLabels.setShowGrid(False)
        self.tblViewProtoLabels.setObjectName("tblViewProtoLabels")
        self.verticalLayout.addWidget(self.tblViewProtoLabels)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(parent=self.groupBoxSettings)
        font = QtGui.QFont()
        font.setUnderline(False)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.cbProtoView = QtWidgets.QComboBox(parent=self.groupBoxSettings)
        self.cbProtoView.setObjectName("cbProtoView")
        self.cbProtoView.addItem("")
        self.cbProtoView.addItem("")
        self.cbProtoView.addItem("")
        self.horizontalLayout_2.addWidget(self.cbProtoView)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.groupBoxAdvancedSettings = QtWidgets.QGroupBox(parent=self.splitter)
        self.groupBoxAdvancedSettings.setObjectName("groupBoxAdvancedSettings")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBoxAdvancedSettings)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tabWidgetAdvancedSettings = QtWidgets.QTabWidget(parent=self.groupBoxAdvancedSettings)
        self.tabWidgetAdvancedSettings.setObjectName("tabWidgetAdvancedSettings")
        self.verticalLayout_2.addWidget(self.tabWidgetAdvancedSettings)
        self.verticalLayout_3.addWidget(self.splitter)
        self.btnConfirm = QtWidgets.QPushButton(parent=DialogLabels)
        self.btnConfirm.setObjectName("btnConfirm")
        self.verticalLayout_3.addWidget(self.btnConfirm)

        self.retranslateUi(DialogLabels)

    def retranslateUi(self, DialogLabels):
        _translate = QtCore.QCoreApplication.translate
        DialogLabels.setWindowTitle(_translate("DialogLabels", "Manage Protocol Labels"))
        self.groupBoxSettings.setTitle(_translate("DialogLabels", "Protocol Label Settings"))
        self.label.setText(_translate("DialogLabels", "Start/End values refer to view type:"))
        self.cbProtoView.setItemText(0, _translate("DialogLabels", "Bits"))
        self.cbProtoView.setItemText(1, _translate("DialogLabels", "Hex"))
        self.cbProtoView.setItemText(2, _translate("DialogLabels", "ASCII"))
        self.groupBoxAdvancedSettings.setTitle(_translate("DialogLabels", "Advanced Settings"))
        self.btnConfirm.setText(_translate("DialogLabels", "Confirm"))
from urh.ui.views.ProtocolLabelTableView import ProtocolLabelTableView
