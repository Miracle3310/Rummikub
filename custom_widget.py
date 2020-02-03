from PyQt5.Qt import *
from game import process

'''
1.倒计时
    时间到——>还原，摸牌，进入下一回合
'''

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
        self.setDisabled()

    # def setDisabled(self,event):
    #     super().setDisabled(event)

    def click(self):
        super().click()
        self.play_signal.emit()


class draw(QPushButton):
    draw_signal=pyqtSignal()
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.setDisabled()

    def click(self):
        super().click()
        self.draw_signal.emit()


class confirm(QPushButton):
    confirm_signal=pyqtSignal()
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.setDisabled()

    def click(self):
        super().click()
        self.confirm_signal.emit()


class remain(QLabel):
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


class area_player(QWidget):
    def __init__(self,*args,**kwargs):
        super().__init__(*args)
        self.resize(500,500)
        # self.move(100,100)
        if 'cards' not in kwargs.keys():
            raise Exception('Missing required parameters: cards')
        else:
            self.cards_list=kwargs['cards']
        self.cards=dict()
        self.cards_layout=QGridLayout()
        self.setLayout(self.cards_layout)

        self.get(self.cards_list)


    def get(self,cards):  # 必须是数组类型
        i=0
        for card_each in cards:
            # print(card_each)
            if card_each in self.cards.keys():
                self.cards[card_each+500] = card(card=card_each, move=False)
                self.cards_layout.addWidget(self.cards[card_each+500],0,i)
            else:
                self.cards[card_each]=card(card=card_each,move=False)
                self.cards_layout.addWidget(self.cards[card_each],0,i)
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
