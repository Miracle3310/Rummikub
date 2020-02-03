# from PyQt5.QtWidgets import QMainWindow, QFrame, QDesktopWidget, QApplication
# from PyQt5.QtCore import Qt, QBasicTimer, pyqtSignal
# from PyQt5.QtGui import QPainter, QColor
import sys
from PyQt5.Qt import *
from game import process


class area(QWidget):
    pass


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.setGeometry(0,0,500,500)
        self.setWindowTitle('Rummikub')
        # self.move(500,200)
        # self.resize(1370//2+50,1250//2+50)
        self.resize(1028, 975)

        main_layout=QGridLayout()
        # player_layout=QGridLayout()
        # desk_layout=QGridLayout()
        # deck_layout=QGridLayout()
        # others_layout_1,others_layout_2,others_layout_3=QGridLayout(),QGridLayout(),QGridLayout()

        # self.player_layout = area_player([111], 60)
        self.player_layout = area_player([111, 213, 312, 401, 500], 60)
        self.desk_layout=area_desk([111, 213, 312, 401, 500])
        self.deck_layout=area_deck()
        self.others_layout_1=area_others(1230-150,110)
        self.others_layout_2 = area_others(150,930-110)
        self.others_layout_3= area_others(150,930-110)

        self.setLayout(main_layout)
        main_layout.addWidget(self.deck_layout,0,0)
        main_layout.addWidget(self.others_layout_1,0,1)
        main_layout.addWidget(self.others_layout_2, 1, 0)
        main_layout.addWidget(self.desk_layout, 1, 1)
        main_layout.addWidget(self.others_layout_3, 1, 2)
        main_layout.addWidget(self.player_layout,2,0,1,3)

        # print(main_layout.rowCount())
        # print(main_layout.columnCount())
        # print(main_layout.cellRect(0, 0))

        # 状态栏，工具栏
        # self.menubar = QMenuBar(self)
        # self.menubar.setGeometry(QRect(0, 0, 1028, 26))
        # self.menubar.setObjectName("menubar")
        # self.setMenuBar(self.menubar)
        # self.statusbar = QStatusBar(self)
        # self.statusbar.setObjectName("statusbar")
        # self.setStatusBar(self.statusbar)


class area_player(QWidget):
    def __init__(self,cards=[],start_time=60,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.cards=cards
        self.resize(1370//2,(1250-930)//2)
        # self.setStyleSheet('background-color:red;')
        self.setObjectName('area_player')
#         self.setStyleSheet("border-width:6px;\n"
# "border-color: rgb(0, 255, 0);\n"
# "border-style:solid;")

        main_layout = QGridLayout()
        self.information=area_information()
        self.options=area_options()
        self.cards_layout = area_cards(cards)
        # options_layout=QGridLayout()
        # button_layout=QGridLayout()
        # time_layout=QGridLayout()

        self.setLayout(main_layout)
        main_layout.addWidget(self.options,0,0,2,1)
        main_layout.addWidget(self.cards_layout,0,1,2,1)
        main_layout.addWidget(self.information,0,2)


    def start(self):
        # 开始轮到本方打牌
        # 设置各个控件的位置
        pass

    def status(self,draw,play,confirm,time):
        # 控制本方区域内各个控件的显示状态
        self.button_draw.setVisible(draw)
        self.button_play.setVisible(play)
        self.button_confirm.setVisible(confirm)
        self.label_time.setVisible(time)


class area_desk(QWidget):
    def __init__(self,cards=[],*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.resize((1230-150)//2,(930-110)//2)

        self.setObjectName('area_desk')
#         self.setStyleSheet('QWidget#area_desk{\
#     border-width:3px;\
#     border-style:solid;\
# }')

        self.cards_show(cards)

    def cards_show(self,cards):
        cards_layout = QHBoxLayout()
        self.setLayout(cards_layout)
        for card_each in cards:
            self.cards_dict = {card_each:card(card_each,False)}  # dict:{311:card(311),...}
            cards_layout.addWidget(self.cards_dict[card_each])




class area_others(QWidget):
    def __init__(self,w,h,quantity=0,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.setObjectName('area_others')
        self.resize(w//2,h//2)
        self.cards_quantity=quantity


class area_deck(QWidget):
    def __init__(self,quantity=0,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.setObjectName('area_deck')
        self.resize(150//2,110//2)
        self.cards_quantity = quantity
        self.lcd=QLCDNumber(2,self)
        self.lcd.display(str(self.cards_quantity))
        self.lcd.resize(150//2,110//2)


class area_options(QWidget):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.resize(150//2,(1250-930)//2)
        self.setObjectName('area_options')
        self.wash=QCheckBox('自动洗牌')
        self.auto=QCheckBox('自动摸牌')

        main_layout=QGridLayout()
        self.setLayout(main_layout)

        main_layout.addWidget(self.wash,0,0)
        main_layout.addWidget(self.auto,1,0)



class label_time(QLabel):
    def __init__(self,start_time=60,*args,**kwargs):
        super().__init__(*args,**kwargs)
        # self.resize(70,90)
        self.time=start_time
        self.setText('Time:'+str(self.time))
        self.timer_id=self.startTimer(1000)
        self.setObjectName('Timer')
        self.setAlignment(Qt.AlignCenter)

        # self.adjustSize()

    def timerEvent(self, *args,**kwargs):
        self.time-=1
        if self.time==0:
            self.setText('')
            self.killTimer(self.timer_id)
        else:
            self.setText('Time:'+str(self.time))



class area_information(QWidget):
    def __init__(self,start_time=60,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.button_draw = QPushButton('抽牌')
        self.button_play = QPushButton('打牌')
        self.button_confirm = QPushButton('确认')
        self.label_time = label_time(start_time)

        button_layout=QGridLayout()
        self.setLayout(button_layout)

        button_layout.addWidget(self.button_play, 0, 0)
        button_layout.addWidget(self.button_draw, 1, 0)
        button_layout.addWidget(self.button_confirm, 2, 0)
        button_layout.addWidget(self.label_time, 3, 0)


class area_cards(QWidget):
    def __init__(self,cards,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.cards_show(cards)

    def cards_show(self,cards):
        cards_layout = QHBoxLayout()
        self.setLayout(cards_layout)
        for card_each in cards:
            self.cards_dict = {card_each:card(card_each)}  # dict:{311:card(311),...}
            cards_layout.addWidget(self.cards_dict[card_each])

    def mouseMoveEvent(self, event):
        pass



class card(QLabel):
    def __init__(self,card=101,in_player=True,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.in_player=in_player
        # self.resize(100//2,100//2)
        self.setMaximumSize(QSize(100//2,100//2))

        self.number=str(card)[1:3]
        self.color= process.color2str(process.take_color(card))

        self.setObjectName('card')
        self.setAlignment(Qt.AlignCenter)
        # self.setNum(self.number)
        self.setText(self.number)
        self.setStyleSheet("QLabel#card{color:"+self.color+";}")

        # self.setMouseTracking(True)

    def mouseMoveEvent(self, event): # todo：未设置不能超出边界
        # print(event.windowPos().x()-25,event.windowPos().y()-25)
        # self.setMouseTracking(True)
        if not self.in_player:
            self.move(event.windowPos().x()-25,event.windowPos().y()-25)
        pass







def run():
    app=QApplication(sys.argv)

    with open('GUI_qss.qss','r') as f:
        app.setStyleSheet(f.read())

    window=Window()
    # label=label_time(5,window)
    # area1=area_player([],5,window)
    # test=card(113,window)
    window.show()

    # print(window.deck_layout.pos())
    # print(window.desk_layout.pos())
    # print(window.others_layout_1.pos())
    # print(window.others_layout_2.pos())
    # print(window.others_layout_3.pos())

    # main_layout=window.layout()
    # print(main_layout.rowCount())
    # print(main_layout.columnCount())
    # for i in range(main_layout.rowCount()):
    #     for j in range(main_layout.columnCount()):
    #             print(i,j,':',main_layout.cellRect(2, 0))

    sys.exit(app.exec_())


if __name__ == '__main__':
    run()