# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GitNote.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form_note(object):
    def setupUi(self, Form_note):
        Form_note.setObjectName("Form_note")
        Form_note.resize(1105, 789)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form_note.sizePolicy().hasHeightForWidth())
        Form_note.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form_note)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_update = QtWidgets.QPushButton(Form_note)
        self.pushButton_update.setText("")
        self.pushButton_update.setIconSize(QtCore.QSize(16, 16))
        self.pushButton_update.setObjectName("pushButton_update")
        self.horizontalLayout.addWidget(self.pushButton_update)
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.toolButton_config = QtWidgets.QToolButton(Form_note)
        self.toolButton_config.setText("")
        self.toolButton_config.setObjectName("toolButton_config")
        self.horizontalLayout.addWidget(self.toolButton_config)
        self.horizontalLayout.setStretch(1, 1)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.splitter_2 = QtWidgets.QSplitter(Form_note)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setChildrenCollapsible(False)
        self.splitter_2.setObjectName("splitter_2")
        self.splitter = QtWidgets.QSplitter(self.splitter_2)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setChildrenCollapsible(False)
        self.splitter.setObjectName("splitter")
        self.treeWidget_tree = QtWidgets.QTreeWidget(self.splitter)
        self.treeWidget_tree.setMinimumSize(QtCore.QSize(10, 0))
        self.treeWidget_tree.setMaximumSize(QtCore.QSize(200, 16777215))
        self.treeWidget_tree.setSizeIncrement(QtCore.QSize(0, 0))
        self.treeWidget_tree.setBaseSize(QtCore.QSize(0, 0))
        self.treeWidget_tree.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.treeWidget_tree.setObjectName("treeWidget_tree")
        self.treeWidget_tree.headerItem().setText(0, "1")
        self.treeWidget_tree.header().setVisible(False)
        self.listWidget_list = QtWidgets.QListWidget(self.splitter)
        self.listWidget_list.setMinimumSize(QtCore.QSize(10, 0))
        self.listWidget_list.setMaximumSize(QtCore.QSize(150, 16777215))
        self.listWidget_list.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.listWidget_list.setIconSize(QtCore.QSize(0, 0))
        self.listWidget_list.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.listWidget_list.setFlow(QtWidgets.QListView.LeftToRight)
        self.listWidget_list.setProperty("isWrapping", True)
        self.listWidget_list.setResizeMode(QtWidgets.QListView.Adjust)
        self.listWidget_list.setViewMode(QtWidgets.QListView.ListMode)
        self.listWidget_list.setObjectName("listWidget_list")
        self.layoutWidget = QtWidgets.QWidget(self.splitter_2)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_save = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_save.setText("")
        self.pushButton_save.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_save.setObjectName("pushButton_save")
        self.horizontalLayout_3.addWidget(self.pushButton_save)
        self.lineEdit_title = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_title.setReadOnly(True)
        self.lineEdit_title.setObjectName("lineEdit_title")
        self.horizontalLayout_3.addWidget(self.lineEdit_title)
        self.pushButton_addpicture = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_addpicture.setText("")
        self.pushButton_addpicture.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_addpicture.setObjectName("pushButton_addpicture")
        self.horizontalLayout_3.addWidget(self.pushButton_addpicture)
        self.toolButton_functions = QtWidgets.QToolButton(self.layoutWidget)
        self.toolButton_functions.setText("")
        self.toolButton_functions.setIconSize(QtCore.QSize(20, 20))
        self.toolButton_functions.setPopupMode(QtWidgets.QToolButton.MenuButtonPopup)
        self.toolButton_functions.setObjectName("toolButton_functions")
        self.horizontalLayout_3.addWidget(self.toolButton_functions)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.plainTextEdit_markdown = QtWidgets.QPlainTextEdit(self.layoutWidget)
        self.plainTextEdit_markdown.setEnabled(True)
        self.plainTextEdit_markdown.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.plainTextEdit_markdown.setObjectName("plainTextEdit_markdown")
        self.horizontalLayout_2.addWidget(self.plainTextEdit_markdown)
        self.textEdit_show = QtWidgets.QTextEdit(self.layoutWidget)
        self.textEdit_show.setReadOnly(True)
        self.textEdit_show.setOverwriteMode(True)
        self.textEdit_show.setObjectName("textEdit_show")
        self.horizontalLayout_2.addWidget(self.textEdit_show)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addWidget(self.splitter_2)

        self.retranslateUi(Form_note)
        QtCore.QMetaObject.connectSlotsByName(Form_note)
        Form_note.setTabOrder(self.treeWidget_tree, self.listWidget_list)
        Form_note.setTabOrder(self.listWidget_list, self.lineEdit_title)
        Form_note.setTabOrder(self.lineEdit_title, self.plainTextEdit_markdown)
        Form_note.setTabOrder(self.plainTextEdit_markdown, self.textEdit_show)
        Form_note.setTabOrder(self.textEdit_show, self.pushButton_update)
        Form_note.setTabOrder(self.pushButton_update, self.pushButton_save)

    def retranslateUi(self, Form_note):
        _translate = QtCore.QCoreApplication.translate
        Form_note.setWindowTitle(_translate("Form_note", "笔记"))


