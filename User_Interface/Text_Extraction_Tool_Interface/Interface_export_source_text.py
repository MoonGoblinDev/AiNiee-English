import yaml
import os
from PyQt5.QtGui import QBrush, QColor, QDesktopServices, QFont, QImage, QPainter, QPixmap#需要安装库 pip3 install PyQt5
from PyQt5.QtCore import  QObject,  QRect,  QUrl,  Qt, pyqtSignal 
from PyQt5.QtWidgets import QAbstractItemView,QHeaderView,QApplication, QTableWidgetItem, QFrame, QGridLayout, QGroupBox, QLabel,QFileDialog, QStackedWidget, QHBoxLayout, QVBoxLayout

from qfluentwidgets.components import Dialog  # 需要安装库 pip install "PyQt-Fluent-Widgets[full]" -i https://pypi.org/simple/
from qfluentwidgets import ProgressRing, SegmentedWidget, TableWidget,CheckBox, DoubleSpinBox, HyperlinkButton,InfoBar, InfoBarPosition, NavigationWidget, Slider, SpinBox, ComboBox, LineEdit, PrimaryPushButton, PushButton ,StateToolTip, SwitchButton, TextEdit, Theme,  setTheme ,isDarkTheme,qrouter,NavigationInterface,NavigationItemPosition, EditableComboBox
from qfluentwidgets import FluentIcon as FIF
from qframelesswindow import FramelessWindow, StandardTitleBar



class Widget_export_source_text(QFrame):#  提取子界面
    def __init__(self, text: str, parent=None,configurator=None,user_interface_prompter=None,jtpp=None):#解释器会自动调用这个函数
        super().__init__(parent=parent)          #调用父类的构造函数
        self.setObjectName(text.replace(' ', '-'))#设置对象名，作用是在NavigationInterface中的addItem中的routeKey参数中使用
        self.configurator = configurator
        self.user_interface_prompter = user_interface_prompter
        self.jtpp = jtpp
        #设置各个控件-----------------------------------------------------------------------------------------



        # -----创建第1个组，添加多个组件-----
        box = QGroupBox()
        box.setStyleSheet(""" QGroupBox {border: 1px solid lightgray; border-radius: 8px;}""")#分别设置了边框大小，边框颜色，边框圆角
        layout = QHBoxLayout()


        self.labe1_3 = QLabel(flags=Qt.WindowFlags())  
        self.labe1_3.setStyleSheet("font-family: 'Microsoft YaHei'; font-size: 17px")
        self.labe1_3.setText("RPG Maker MV/MZ 的文本提取注入工具")


        #设置Official Docs说明链接按钮
        hyperlinkButton = HyperlinkButton(
            url='https://github.com/NEKOparapa/AiNiee/blob/main/StevExtraction/%E4%BD%BF%E7%94%A8%E8%AF%B4%E6%98%8E.md',
            text='(Instructions for use)'
        )


        layout.addStretch(1)  # 添加伸缩项
        layout.addWidget(self.labe1_3)
        layout.addWidget(hyperlinkButton)
        layout.addStretch(1)  # 添加伸缩项
        box.setLayout(layout)




        # -----创建第1个组，添加多个组件-----
        box_switch = QGroupBox()
        box_switch.setStyleSheet(""" QGroupBox {border: 1px solid lightgray; border-radius: 8px;}""")#分别设置了边框大小，边框颜色，边框圆角
        layout_switch = QHBoxLayout()

        #设置“是否日语游戏”标签
        self.labe1_4 = QLabel(flags=Qt.WindowFlags())  
        self.labe1_4.setStyleSheet("font-family: 'Microsoft YaHei'; font-size: 17px")
        self.labe1_4.setText("Whether the game is in Japanese")



        # 设置“是否日语游戏”选择开关
        self.SwitchButton_ja = CheckBox('        ')
        self.SwitchButton_ja.setChecked(True)    
        # 绑定选择开关的点击事件
        self.SwitchButton_ja.clicked.connect(self.test)



        layout_switch.addWidget(self.labe1_4)
        layout_switch.addStretch(1)  # 添加伸缩项
        layout_switch.addWidget(self.SwitchButton_ja)
        box_switch.setLayout(layout_switch)



        # -----创建第2个组，添加多个组件-----
        box_input = QGroupBox()
        box_input.setStyleSheet(""" QGroupBox {border: 1px solid lightgray; border-radius: 8px;}""")#分别设置了边框大小，边框颜色，边框圆角
        layout_input = QHBoxLayout()

        #设置“游戏文件夹”标签
        label4 = QLabel(flags=Qt.WindowFlags())  
        label4.setStyleSheet("font-family: 'Microsoft YaHei'; font-size: 17px")
        label4.setText("Games Folder")

        #设置“游戏文件夹”显示
        self.label_input_path = QLabel(parent=self, flags=Qt.WindowFlags())  
        self.label_input_path.setStyleSheet("font-family: 'Microsoft YaHei'; font-size: 11px")
        self.label_input_path.setText("(Game root folder)")  

        #设置打开文件按钮
        self.pushButton_input = PushButton('Select Folder', self, FIF.FOLDER)
        self.pushButton_input.clicked.connect(self.Select_project_folder) #按钮绑定槽函数



        layout_input.addWidget(label4)
        layout_input.addWidget(self.label_input_path)
        layout_input.addStretch(1)  # 添加伸缩项
        layout_input.addWidget(self.pushButton_input)
        box_input.setLayout(layout_input)



        # -----创建第3个组，添加多个组件-----
        box_output = QGroupBox()
        box_output.setStyleSheet(""" QGroupBox {border: 1px solid lightgray; border-radius: 8px;}""")#分别设置了边框大小，边框颜色，边框圆角
        layout_output = QHBoxLayout()

        #设置“输出文件夹”标签
        label6 = QLabel(parent=self, flags=Qt.WindowFlags())  
        label6.setStyleSheet("font-family: 'Microsoft YaHei'; font-size: 17px;  color: black")
        label6.setText("Original storage folder")

        #设置“输出文件夹”显示
        self.label_output_path = QLabel(parent=self, flags=Qt.WindowFlags())  
        self.label_output_path.setStyleSheet("font-family: 'Microsoft YaHei'; font-size: 11px;  color: black")
        self.label_output_path.setText("(The folder where the original game is stored after extraction)")

        #设置输出文件夹按钮
        self.pushButton_output = PushButton('Select Folder', self, FIF.FOLDER)
        self.pushButton_output.clicked.connect(self.Select_output_folder) #按钮绑定槽函数


        layout_output.addWidget(label6)
        layout_output.addWidget(self.label_output_path)
        layout_output.addStretch(1)  # 添加伸缩项
        layout_output.addWidget(self.pushButton_output)
        box_output.setLayout(layout_output)



        # -----创建第3个组，添加多个组件-----
        box_data = QGroupBox()
        box_data.setStyleSheet(""" QGroupBox {border: 1px solid lightgray; border-radius: 8px;}""")#分别设置了边框大小，边框颜色，边框圆角
        layout_data = QHBoxLayout()

        #设置“输出文件夹”标签
        label6 = QLabel(parent=self, flags=Qt.WindowFlags())  
        label6.setStyleSheet("font-family: 'Microsoft YaHei'; font-size: 17px;  color: black")
        label6.setText("Project Storage Folder")

        #设置“输出文件夹”显示
        self.label_data_path = QLabel(parent=self, flags=Qt.WindowFlags())  
        self.label_data_path.setStyleSheet("font-family: 'Microsoft YaHei'; font-size: 11px;  color: black")
        self.label_data_path.setText("(The folder where the game's project data is stored)")

        #设置输出文件夹按钮
        self.pushButton_data = PushButton('Select Folder', self, FIF.FOLDER)
        self.pushButton_data.clicked.connect(self.Select_data_folder) #按钮绑定槽函数


        layout_data.addWidget(label6)
        layout_data.addWidget(self.label_data_path)
        layout_data.addStretch(1)  # 添加伸缩项
        layout_data.addWidget(self.pushButton_data)
        box_data.setLayout(layout_data)





        # -----创建第x个组，添加多个组件-----
        box_start_export = QGroupBox()
        box_start_export.setStyleSheet(""" QGroupBox {border: 0px solid lightgray; border-radius: 8px;}""")#分别设置了边框大小，边框颜色，边框圆角
        layout_start_export = QHBoxLayout()


        #设置“开始翻译”的按钮
        self.primaryButton_start_export = PrimaryPushButton('Begin extraction of the original text', self, FIF.UPDATE)
        self.primaryButton_start_export.clicked.connect(self.Start_export) #按钮绑定槽函数


        layout_start_export.addStretch(1)  # 添加伸缩项
        layout_start_export.addWidget(self.primaryButton_start_export)
        layout_start_export.addStretch(1)  # 添加伸缩项
        box_start_export.setLayout(layout_start_export)



        # 最外层的垂直布局
        container = QVBoxLayout()

        # 把内容添加到容器中
        container.addStretch(1)  # 添加伸缩项
        container.addWidget(box)
        container.addWidget(box_switch)
        container.addWidget(box_input)
        container.addWidget(box_output)
        container.addWidget(box_data)
        container.addWidget(box_start_export)
        container.addStretch(1)  # 添加伸缩项

        # 设置窗口显示的内容是最外层容器
        self.setLayout(container)
        container.setSpacing(28) # 设置布局内控件的间距为28
        container.setContentsMargins(50, 70, 50, 30) # 设置布局的边距, 也就是外边框距离，分别为左、上、右、下

    #设置开关绑定函数
    def test(self, isChecked: bool):
        if isChecked== False:
            self.user_interface_prompter.createWarningInfoBar("Not recommended for non-Japanese games, prone to problems.")

    # 选择输入文件夹按钮绑定函数
    def Select_project_folder(self):
        Input_Folder = QFileDialog.getExistingDirectory(None, 'Select Directory', '')      #调用QFileDialog类里的函数来选择文件目录
        if Input_Folder:
            self.label_input_path.setText(Input_Folder)
            print('[INFO]  The game root folder has been selected: ',Input_Folder)
        else :
            print('[INFO]  No folder selected')
            return  # 直接返回，不执行后续操作


    # 选择原文文件夹按钮绑定函数
    def Select_output_folder(self):
        Output_Folder = QFileDialog.getExistingDirectory(None, 'Select Directory', '')      #调用QFileDialog类里的函数来选择文件目录
        if Output_Folder:
            self.label_output_path.setText(Output_Folder)
            print('[INFO]  Original text storage folder has been selected:' ,Output_Folder)
        else :
            print('[INFO]  No folder selected')
            return  # 直接返回，不执行后续操作


    # 选择工程文件夹按钮绑定函数
    def Select_data_folder(self):
        data_Folder = QFileDialog.getExistingDirectory(None, 'Select Directory', '')      #调用QFileDialog类里的函数来选择文件目录
        if data_Folder:
            self.label_data_path.setText(data_Folder)
            print('[INFO]  Project storage folder selected:' ,data_Folder)
        else :
            print('[INFO]  No folder selected')
            return  # 直接返回，不执行后续操作


    # 提取函数
    def Start_export(self):
        print('[INFO]  Start to extract the original game, please wait!！！！')

        #读取配置文件
        config_path = os.path.join(self.configurator.script_dir, "StevExtraction", "config.yaml")
        with open(config_path, 'r', encoding='utf-8') as file:
            config = yaml.safe_load(file)

        #修改输入输出路径及开关
        config['game_path'] = self.label_input_path.text()
        config['save_path'] = self.label_data_path.text()
        config['data_path'] = self.label_output_path.text()
        config['ja']=self.SwitchButton_ja.isChecked()
        #提取文本
        pj=self.jtpp.Jr_Tpp(config)
        pj.FromGame(config['game_path'],config['save_path'],config['data_path'])
