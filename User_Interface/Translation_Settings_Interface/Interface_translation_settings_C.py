
from PyQt5.QtGui import QBrush, QColor, QDesktopServices, QFont, QImage, QPainter, QPixmap#需要安装库 pip3 install PyQt5
from PyQt5.QtCore import  QObject,  QRect,  QUrl,  Qt, pyqtSignal 
from PyQt5.QtWidgets import QAbstractItemView,QHeaderView,QApplication, QTableWidgetItem, QFrame, QGridLayout, QGroupBox, QLabel,QFileDialog, QStackedWidget, QHBoxLayout, QVBoxLayout, QWidget

from qfluentwidgets.components import Dialog  # 需要安装库 pip install "PyQt-Fluent-Widgets[full]" -i https://pypi.org/simple/
from qfluentwidgets import BodyLabel, ExpandGroupSettingCard, FluentIcon, IndicatorPosition, ProgressRing, SegmentedWidget, TableWidget,CheckBox, DoubleSpinBox, HyperlinkButton,InfoBar, InfoBarPosition, NavigationWidget, Slider, SpinBox, ComboBox, LineEdit, PrimaryPushButton, PushButton ,StateToolTip, SwitchButton, TextEdit, Theme,  setTheme ,isDarkTheme,qrouter,NavigationInterface,NavigationItemPosition, EditableComboBox
from qfluentwidgets import FluentIcon as FIF
from qframelesswindow import FramelessWindow, StandardTitleBar



class Widget_translation_settings_C(QFrame):#  混合翻译设置子界面
    def __init__(self, text: str, parent=None,user_interface_prompter=None):#解释器会自动调用这个函数
        super().__init__(parent=parent)          #调用父类的构造函数
        self.setObjectName(text.replace(' ', '-'))#设置对象名，作用是在NavigationInterface中的addItem中的routeKey参数中使用
        self.user_interface_prompter = user_interface_prompter
        #设置各个控件-----------------------------------------------------------------------------------------



        # -----创建第1个组，添加多个组件-----
        box_switch = QGroupBox()
        box_switch.setStyleSheet(""" QGroupBox {border: 1px solid lightgray; border-radius: 8px;}""")#分别设置了边框大小，边框颜色，边框圆角
        layout_switch = QHBoxLayout()

        #设置标签
        self.labe1_4 = QLabel(flags=Qt.WindowFlags())  
        self.labe1_4.setStyleSheet("font-family: 'Microsoft YaHei'; font-size: 17px")
        self.labe1_4.setText("Enabling Mixed Platform Translation")



        # 设置选择开关
        self.SwitchButton_mixed_translation = SwitchButton(parent=self)    
        self.SwitchButton_mixed_translation.checkedChanged.connect(self.test)



        layout_switch.addWidget(self.labe1_4)
        layout_switch.addStretch(1)  # 添加伸缩项
        layout_switch.addWidget(self.SwitchButton_mixed_translation)
        box_switch.setLayout(layout_switch)



        # 首轮翻译平台设置卡
        self.SettingCard_A = SettingCard_A()

        # 次轮翻译平台设置卡
        self.SettingCard_B = SettingCard_B(parent=None,user_interface_prompter=self.user_interface_prompter)

        # 末轮翻译平台设置卡
        self.SettingCard_C = SettingCard_C()

        # 最外层的垂直布局
        container = QVBoxLayout()

        # 把内容添加到容器中
        #container.addStretch(1)  # 添加伸缩项
        container.addWidget(box_switch)
        container.addStretch(1)  # 添加伸缩项
        container.addWidget( self.SettingCard_A)
        container.addWidget( self.SettingCard_B)
        container.addWidget( self.SettingCard_C)
        container.addStretch(1)  # 添加伸缩项
        container.addStretch(1)  # 添加伸缩项

        # 设置窗口显示的内容是最外层容器
        self.setLayout(container)
        container.setSpacing(28) # 设置布局内控件的间距为28
        container.setContentsMargins(50, 70, 50, 30) # 设置布局的边距, 也就是外边框距离，分别为左、上、右、下


    #设置开关绑定函数
    def test(self, isChecked: bool):
        if isChecked:
            self.user_interface_prompter.createWarningInfoBar("Please note that the following settings will only take effect if this switch is turned on, and will override some of the basic settings")

class SettingCard_A(ExpandGroupSettingCard):

    def __init__(self, parent=None):
        super().__init__(FluentIcon.SPEED_OFF, "First round of platforms", "AI platform used for the first round of translations", parent)

        # 第一组
        self.translationPlatform_label = BodyLabel("Translation Platform")
        self.translationPlatform_comboBox = ComboBox()
        self.translationPlatform_comboBox.addItems(['OpenAI',  'Google', 'Anthropic',  'Cohere',  'Moonshot',  'Deepseek',  'Dashscope', 'Volcengine', '零一万物',  '智谱',  'SakuraLLM',  '代理平台A'])
        self.translationPlatform_comboBox.setFixedWidth(160)


        # 调整内部布局
        self.viewLayout.setContentsMargins(0, 0, 0, 0)
        self.viewLayout.setSpacing(0)

        # 添加各组到设置卡中
        self.add(self.translationPlatform_label, self.translationPlatform_comboBox)

    def add(self, label, widget):
        w = QWidget()
        w.setFixedHeight(60)

        layout = QHBoxLayout(w)
        layout.setContentsMargins(48, 12, 48, 12)

        layout.addWidget(label)
        layout.addStretch(1)
        layout.addWidget(widget)

        # 添加组件到设置卡
        self.addGroupWidget(w)


class SettingCard_B(ExpandGroupSettingCard):

    def __init__(self, parent=None,user_interface_prompter=None):
        super().__init__(FluentIcon.SPEED_MEDIUM, "Sub-round platforms", "AI platform used for the second round of translations", parent)
        self.user_interface_prompter = user_interface_prompter


        # 第一组
        self.translationPlatform_label = BodyLabel("Translation Platform")
        self.translationPlatform_comboBox = ComboBox()
        self.translationPlatform_comboBox.addItems(['OpenAI',  'Google', 'Anthropic',  'Cohere',  'Moonshot',  'Deepseek',  'Dashscope', 'Volcengine', '零一万物',  '智谱',  'SakuraLLM',  '代理平台A'])
        self.translationPlatform_comboBox.setFixedWidth(160)



        # 第二组
        self.customModel_label = BodyLabel("Reselection models")
        self.customModel_Button = SwitchButton("Off.", self, IndicatorPosition.RIGHT)
        self.customModel_Button.setOnText("On.")
        self.customModel_Button.checkedChanged.connect(self.test)
        # 第三组
        self.modeLabel = BodyLabel("Model name")
        self.model_type = LineEdit()
        self.model_type.setFixedWidth(160)

        # 第四组
        self.textSplitting_label = BodyLabel("Split text in half")
        self.textSplitting_Button = SwitchButton("Off.", self, IndicatorPosition.RIGHT)
        self.textSplitting_Button.setOnText("On.")


        # 调整内部布局
        self.viewLayout.setContentsMargins(0, 0, 0, 0)
        self.viewLayout.setSpacing(0)

        # 添加各组到设置卡中
        self.add(self.translationPlatform_label, self.translationPlatform_comboBox)
        self.add(self.customModel_label, self.customModel_Button)
        self.add(self.modeLabel, self.model_type)
        self.add(self.textSplitting_label, self.textSplitting_Button)


    def add(self, label, widget):
        w = QWidget()
        w.setFixedHeight(60)

        layout = QHBoxLayout(w)
        layout.setContentsMargins(48, 12, 48, 12)

        layout.addWidget(label)
        layout.addStretch(1)
        layout.addWidget(widget)

        # 添加组件到设置卡
        self.addGroupWidget(w)

    #设置开关绑定函数
    def test(self, isChecked: bool):
        if isChecked:
            self.user_interface_prompter.createWarningInfoBar("Please note that predefined models that are not in the platform configuration will have problems")

class SettingCard_C(ExpandGroupSettingCard):

    def __init__(self, parent=None):
        super().__init__(FluentIcon.SPEED_HIGH, "Last round of platforms", "AI platform used for all subsequent rounds of translation", parent)

        # 第一组
        self.translationPlatform_label = BodyLabel("Translation Platform")
        self.translationPlatform_comboBox = ComboBox()
        self.translationPlatform_comboBox.addItems(['OpenAI',  'Google', 'Anthropic',  'Cohere',  'Moonshot',  'Deepseek',  'Dashscope', 'Volcengine', '零一万物',  '智谱',  'SakuraLLM',  '代理平台A'])
        self.translationPlatform_comboBox.setFixedWidth(160)



        # 第二组
        self.customModel_label = BodyLabel("Reselection models")
        self.customModel_Button = SwitchButton("Off.", self, IndicatorPosition.RIGHT)
        self.customModel_Button.setOnText("On.")

        # 第三组
        self.modeLabel = BodyLabel("Model name")
        self.model_type = LineEdit()
        self.model_type.setFixedWidth(160)

        # 第四组
        self.textSplitting_label = BodyLabel("Split text in half")
        self.textSplitting_Button = SwitchButton("Off.", self, IndicatorPosition.RIGHT)
        self.textSplitting_Button.setOnText("On.")


        # 调整内部布局
        self.viewLayout.setContentsMargins(0, 0, 0, 0)
        self.viewLayout.setSpacing(0)

        # 添加各组到设置卡中
        self.add(self.translationPlatform_label, self.translationPlatform_comboBox)
        self.add(self.customModel_label, self.customModel_Button)
        self.add(self.modeLabel, self.model_type)
        self.add(self.textSplitting_label, self.textSplitting_Button)


    def add(self, label, widget):
        w = QWidget()
        w.setFixedHeight(60)

        layout = QHBoxLayout(w)
        layout.setContentsMargins(48, 12, 48, 12)

        layout.addWidget(label)
        layout.addStretch(1)
        layout.addWidget(widget)

        # 添加组件到设置卡
        self.addGroupWidget(w)