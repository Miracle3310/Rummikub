from PyQt5.Qt import *
from game import process
from PyQt5 import QtCore, QtGui, QtWidgets
'''
1.倒计时
    时间到——>还原，摸牌，进入下一回合
'''

class window(QWidget):
    def __init__(self,*args,**kwargs):
        super().__init__(*args)
        # if 'card' not in kwargs.keys():
        #     raise Exception('Missing required parameter: card')
        # else:
        #     self.card=kwargs['card']
        self.player=kwargs['player']
        self.deck=kwargs['deck']
        self.desk=kwargs['desk']

        # 要显示一个已经发好牌的桌面
        # 先用qt designer设计一个初始界面
        # 然后补上一个自定义初始化函数，包括第一位玩家按钮可用+倒计时等等
        # 考虑通过信号与槽实现玩家回合结束的这个操作
        self.setupUi(self)
        self.show_hand()
        self.show()

    # 展示手牌
    def show_hand(self):
        self.findChild(QFrame,'area_player').get(self.player.card)

    def setupUi(self, Form):
            Form.setObjectName("Form")
            Form.resize(1535, 937)
            self.gridLayout = QtWidgets.QGridLayout(Form)
            self.gridLayout.setObjectName("gridLayout")
            self.lcdNumber = LCD_time(Form)
            self.lcdNumber.setMinimumSize(QtCore.QSize(100, 100))
            self.lcdNumber.setMaximumSize(QtCore.QSize(100, 100))
            self.lcdNumber.setStyleSheet("")
            self.lcdNumber.setFrameShape(QtWidgets.QFrame.Box)
            self.lcdNumber.setFrameShadow(QtWidgets.QFrame.Plain)
            self.lcdNumber.setLineWidth(5)
            self.lcdNumber.setSmallDecimalPoint(False)
            self.lcdNumber.setDigitCount(2)
            self.lcdNumber.setProperty("value", 60.0)
            self.lcdNumber.setObjectName("lcdNumber")
            self.gridLayout.addWidget(self.lcdNumber, 0, 0, 1, 1)
            self.widget_2 = QtWidgets.QWidget(Form)
            self.widget_2.setMinimumSize(QtCore.QSize(800, 100))
            self.widget_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
            self.widget_2.setStyleSheet("border-width:6px;\n"
                                        "border-color: rgb(0, 255, 0);\n"
                                        "border-style:solid;")
            self.widget_2.setObjectName("widget_2")
            self.label_3 = remain(self.widget_2)
            self.label_3.setGeometry(QtCore.QRect(370, 20, 70, 70))
            self.label_3.setStyleSheet("\n"
                                       "background-color: rgb(255, 255, 255);\n"
                                       "    border-width:6px;\n"
                                       "    border-style:solid;\n"
                                       "    font-family:Consolas;\n"
                                       "    font-size:30px;\n"
                                       "    font-weight:700;\n"
                                       "color: rgb(0, 255, 0);")
            self.label_3.setAlignment(QtCore.Qt.AlignCenter)
            self.label_3.setObjectName("label_3")
            self.gridLayout.addWidget(self.widget_2, 0, 1, 1, 1)
            self.remain_all = remain(Form)
            self.remain_all.setMinimumSize(QtCore.QSize(60, 50))
            self.remain_all.setMaximumSize(QtCore.QSize(100, 500))
            self.remain_all.setStyleSheet("background-color:white;\n"
                                          "    border-width:6px;\n"
                                          "    border-style:solid;\n"
                                          "    font-family:Consolas;\n"
                                          "    font-size:80px;\n"
                                          "    font-weight:900;")
            self.remain_all.setAlignment(QtCore.Qt.AlignCenter)
            self.remain_all.setObjectName("remain_all")
            self.gridLayout.addWidget(self.remain_all, 0, 2, 1, 1)
            self.widget_3 = QtWidgets.QWidget(Form)
            self.widget_3.setMinimumSize(QtCore.QSize(100, 600))
            self.widget_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
            self.widget_3.setStyleSheet("border-width:6px;\n"
                                        "border-color: rgb(255, 0, 0);\n"
                                        "border-style:solid;")
            self.widget_3.setObjectName("widget_3")
            self.label_2 = remain(self.widget_3)
            self.label_2.setGeometry(QtCore.QRect(10, 270, 70, 70))
            self.label_2.setMinimumSize(QtCore.QSize(50, 50))
            self.label_2.setStyleSheet("background-color:white;\n"
                                       "color: rgb(255, 0, 0);\n"
                                       "    border-width:6px;\n"
                                       "    border-style:solid;\n"
                                       "    font-family:Consolas;\n"
                                       "    font-size:30px;\n"
                                       "    font-weight:700;")
            self.label_2.setAlignment(QtCore.Qt.AlignCenter)
            self.label_2.setWordWrap(True)
            self.label_2.setObjectName("label_2")
            self.gridLayout.addWidget(self.widget_3, 1, 0, 1, 1)
            self.desk = QtWidgets.QWidget(Form)
            self.desk.setMaximumSize(QtCore.QSize(16777215, 16777215))
            self.desk.setStyleSheet("border-width:6px;\n"
                                    "border-color: rgb(255, 255, 0);\n"
                                    "border-style:solid;")
            self.desk.setObjectName("desk")
            self.gridLayout.addWidget(self.desk, 1, 1, 1, 1)
            self.frame = QtWidgets.QFrame(Form)
            self.frame.setMinimumSize(QtCore.QSize(100, 600))
            self.frame.setMaximumSize(QtCore.QSize(100, 16777215))
            self.frame.setStyleSheet("border-width:6px;\n"
                                     "border-color: rgb(0, 0, 255);\n"
                                     "border-style:solid;")
            self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
            self.frame.setObjectName("frame")
            self.label_4 = QtWidgets.QLabel(self.frame)
            self.label_4.setGeometry(QtCore.QRect(10, 250, 70, 70))
            self.label_4.setStyleSheet("background-color:white;\n"
                                       "color: rgb(0, 0, 255);\n"
                                       "    border-width:6px;\n"
                                       "    border-style:solid;\n"
                                       "    font-family:Consolas;\n"
                                       "    font-size:30px;\n"
                                       "    font-weight:700;")
            self.label_4.setAlignment(QtCore.Qt.AlignCenter)
            self.label_4.setObjectName("label_4")
            self.gridLayout.addWidget(self.frame, 1, 2, 1, 1)
            self.verticalLayout_2 = QtWidgets.QVBoxLayout()
            self.verticalLayout_2.setSpacing(1)
            self.verticalLayout_2.setObjectName("verticalLayout_2")
            self.checkBox_2 = QtWidgets.QCheckBox(Form)
            self.checkBox_2.setObjectName("checkBox_2")
            self.verticalLayout_2.addWidget(self.checkBox_2)
            self.checkBox = QtWidgets.QCheckBox(Form)
            self.checkBox.setObjectName("checkBox")
            self.verticalLayout_2.addWidget(self.checkBox)
            self.checkBox_3 = QtWidgets.QCheckBox(Form)
            self.checkBox_3.setObjectName("checkBox_3")
            self.verticalLayout_2.addWidget(self.checkBox_3)
            self.checkBox_4 = QtWidgets.QCheckBox(Form)
            self.checkBox_4.setObjectName("checkBox_4")
            self.verticalLayout_2.addWidget(self.checkBox_4)
            self.gridLayout.addLayout(self.verticalLayout_2, 2, 0, 1, 1)
            self.area_player = area_player(Form)
            self.area_player.setMinimumSize(QtCore.QSize(800, 200))
            self.area_player.setStyleSheet("border-width:6px;\n"
                                           "border-color: rgb(0, 0, 0);\n"
                                           "border-style:solid;")
            self.area_player.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.area_player.setFrameShadow(QtWidgets.QFrame.Raised)
            self.area_player.setLineWidth(1)
            self.area_player.setObjectName("area_player")
            self.gridLayout.addWidget(self.area_player, 2, 1, 1, 1)
            self.verticalLayout = QtWidgets.QVBoxLayout()
            self.verticalLayout.setSpacing(4)
            self.verticalLayout.setObjectName("verticalLayout")
            self.pushButton_3 = play(Form)
            self.pushButton_3.setMaximumSize(QtCore.QSize(100, 16777215))
            self.pushButton_3.setObjectName("pushButton_3")
            self.verticalLayout.addWidget(self.pushButton_3)
            self.pushButton = draw(Form)
            self.pushButton.setMaximumSize(QtCore.QSize(100, 16777215))
            self.pushButton.setObjectName("pushButton")
            self.verticalLayout.addWidget(self.pushButton)
            self.pushButton_2 = confirm(Form)
            self.pushButton_2.setMaximumSize(QtCore.QSize(100, 16777215))
            self.pushButton_2.setObjectName("pushButton_2")
            self.verticalLayout.addWidget(self.pushButton_2)
            self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
            self.horizontalLayout_2.setObjectName("horizontalLayout_2")
            self.label = remain(Form)
            self.label.setMinimumSize(QtCore.QSize(60, 50))
            self.label.setMaximumSize(QtCore.QSize(60, 50))
            self.label.setStyleSheet("background-color:white;\n"
                                     "    border-width:6px;\n"
                                     "    border-style:solid;\n"
                                     "    font-family:Consolas;\n"
                                     "    font-size:35px;\n"
                                     "    font-weight:900;")
            self.label.setAlignment(QtCore.Qt.AlignCenter)
            self.label.setObjectName("label")
            self.horizontalLayout_2.addWidget(self.label)
            self.verticalLayout.addLayout(self.horizontalLayout_2)
            self.gridLayout.addLayout(self.verticalLayout, 2, 2, 1, 1)

            self.retranslateUi(Form)
            self.pushButton.clicked.connect(self.remain_all.draw_down)
            self.pushButton.clicked.connect(self.label.draw_up)
            self.pushButton.clicked.connect(self.lcdNumber.timeStop)
            QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
            _translate = QtCore.QCoreApplication.translate
            Form.setWindowTitle(_translate("Form", "Form"))
            self.label_3.setText(_translate("Form", "13"))
            self.remain_all.setText(_translate("Form", "54"))
            self.label_2.setText(_translate("Form", "13"))
            self.label_4.setText(_translate("Form", "13"))
            self.checkBox_2.setText(_translate("Form", "自动洗牌"))
            self.checkBox.setText(_translate("Form", "自动摸牌"))
            self.checkBox_3.setText(_translate("Form", "CheckBox"))
            self.checkBox_4.setText(_translate("Form", "CheckBox"))
            self.pushButton_3.setText(_translate("Form", "打牌"))
            self.pushButton.setText(_translate("Form", "摸牌"))
            self.pushButton_2.setText(_translate("Form", "确认"))
            self.label.setText(_translate("Form", "13"))


class LCD_time(QLCDNumber):
    equal_zero=pyqtSignal()

    def __init__(self,*args,**kwargs):
        super().__init__(*args)
        # self.resize(100,100)

        # for v in args:
        #     print('Optional argument (args): ', v)
        # for k, v in kwargs.items():
        #     print('Optional argument %s (kwargs): %s' % (k, v))

        self.setObjectName('Timer')
        if 'start_time' not in kwargs.keys():
            self.start_time=60
        else:
            self.start_time=kwargs['start_time']

        self.time=self.start_time
        self.display(self.time)

        # self.setNum(self.time)
        # self.setText('Time:'+str(self.time))
        # self.setAlignment(Qt.AlignCenter)
        # self.adjustSize()

    def timerEvent(self,*args,**kwargs):
        if self.time==0:
            # self.setText('')
            self.timeStop()
            # self.equal_zero.emit()
        else:
            self.time -= 1
            self.display(self.time)

    def timeStop(self):
        self.killTimer(self.timer_id)

    def timeStart(self):
        self.time=self.start_time
        self.display(self.time)
        self.timer_id = self.startTimer(1000)


class card(QLabel):
    double_clicked=pyqtSignal()
    def __init__(self,*args,**kwargs):
        super().__init__(*args,)
        if 'move' not in kwargs.keys():
            self.can_move = True
        else:
            self.can_move=kwargs['move']

        if 'card' not in kwargs.keys():
            raise Exception('Missing required parameters: card')
        else:
            self.card=kwargs['card']

        self.setMaximumSize(QSize(100//2,100//2))
        self.setMinimumSize(QSize(100 // 2, 100 // 2))

        self.number=str(self.card)[1:3]
        print(self.number)
        self.color= process.color2str(process.take_color(self.card))

        self.setObjectName('card')
        self.setAlignment(Qt.AlignCenter)
        # self.setNum(self.number)
        self.setText(self.number)
        self.setStyleSheet("background-color:rgb(238,222,176);\n"
                                    "border-color: rgb(0, 0, 0);\n"
                                    "    border-width:3px;\n"
                                    "    border-style:solid;\n"
                                    "    font-family:Consolas;\n"
                                    "    font-size:35px;\n"
                                    "    font-weight:900;\n"
                           "color:"+self.color+";")
        # self.setStyleSheet("QLabel#card{color:"+self.color+";}")

        # self.setMouseTracking(True)

    def mouseMoveEvent(self, event): # todo：未设置不能超出边界，移动坐标还有问题
        # print(event.windowPos().x()-25,event.windowPos().y()-25)
        # self.setMouseTracking(True)

        if self.can_move:
            self.move(event.windowPos().x() - 25, event.windowPos().y() - 25)


        # self.move(event.windowPos().x() - 25, event.windowPos().y() - 25)

    def mouseDoubleClickEvent(self, event):
        if self.can_move:
            pass
        else:
            self.double_clicked.emit()
            self.deleteLater()  # 删除控件


class play(QPushButton):
    play_signal=pyqtSignal()
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.setDisabled(True)

    # def setDisabled(self,event):
    #     super().setDisabled(event)

    def click(self):
        super().click()
        self.play_signal.emit()


class draw(QPushButton):
    draw_signal=pyqtSignal()
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.setDisabled(True)

    def click(self):
        super().click()
        self.draw_signal.emit()


class confirm(QPushButton):
    confirm_signal=pyqtSignal()
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.setDisabled(True)

    def click(self):
        super().click()
        self.confirm_signal.emit()


class remain(QLabel):
    # 显示剩余牌的数量
    game_over=pyqtSignal
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        if 'init' not in kwargs.keys():
            self.init=13
        else:
            self.init=kwargs['init']

        self.num=self.init

        self.setText(str(self.num))

    def change(self,num):
        self.num+=num
        self.setNum(self.num)

    def draw_up(self):
        self.change(1)

    def draw_down(self):
        self.change(-1)

    def punish_up(self):
        self.change(3) # 这里没有考虑抽完的情况

    def punish_down(self):
        if self.num > 3:
            self.change(-3)
        else:
            self.change(-self.num)
            self.end_game()

    def end_game(self):
        if self.num==0:
            self.game_over.emit()


class area_player(QFrame):
    def __init__(self,*args,**kwargs):
        super().__init__(*args)
        # self.resize(500,500)
        # self.move(100,100)
        # if 'cards' not in kwargs.keys():
        #     raise Exception('Missing required parameters: cards')
        # else:
        #     self.cards_list=kwargs['cards']

        self.cards=dict()
        self.cards_layout=QGridLayout()
        self.setLayout(self.cards_layout)

        # self.get(self.cards_list)

    # 必须是数组类型
    # 未检验是否自动换行排列
    def get(self,cards):
        i=len(self.cards)
        for card_each in cards:
            j = i // 13
            # print(card_each)
            if card_each in self.cards.keys():
                self.cards[card_each+500] = card(card=card_each, move=False)
                self.cards_layout.addWidget(self.cards[card_each+500],j,i)
            else:
                self.cards[card_each]=card(card=card_each,move=False)
                self.cards_layout.addWidget(self.cards[card_each],j,i)
            i+=1

    def pop(self,card):
        # 未考虑直接删除对layout的影响，
        # 必须要传参，作为槽函数需要使用匿名函数
        if card+500 in self.cards.keys():
            self.cards_list.remove(card)
            del self.cards[card+500]
        elif card in self.cards.keys():
            self.cards_list.remove(card)
            del self.cards[card]
        else:
            raise Exception("Don't have card: "+str(card))



if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window=QWidget()
    # time=LCD_time(window, start_time=5)
    # time.timeStart()
    # time.equal_zero.connect(time.timeStop)

    # c=card(window,card=113)
    # c.move(50,50)

    player=area_player(window,cards=[111,211,311,111,101,102,103,104])
    # player

    window.show()

    # time.timeStop()
    sys.exit(app.exec_())
