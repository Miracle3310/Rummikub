from PyQt5.QtWidgets import QMainWindow, QFrame, QDesktopWidget, QApplication
from PyQt5.QtCore import Qt, QBasicTimer, pyqtSignal
from PyQt5.QtGui import QPainter, QColor
import sys, random
from PyQt5.Qt import *

class area(QWidget):
    pass


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.setGeometry(0,0,500,500)
        self.setWindowTitle('Rummikub')
        self.move(0,0)
        self.resize(1000,1000)

class area_player(QWidget):
    def __init__(self,cards=[],start_time=60,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.button_draw=QPushButton(self)
        self.button_play=QPushButton(self)
        self.button_confirm=QPushButton(self)
        self.label_time=label_time(start_time,self)
        self.cards=cards

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
    def __init__(self,cards,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.cards=cards


class area_others(QWidget):
    def __init__(self,quantity,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.cards_quantity=quantity


class area_deck(QWidget):
    def __init__(self,quantity,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.cards_quantity = quantity


class area_options(QWidget):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.wash=QCheckBox(self)
        self.auto=QCheckBox(self)



class label_time(QLabel):
    def __init__(self,start_time,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.setText(str(start_time))
        self.timer_id=self.startTimer(1000)

    def timerEvent(self, *args,**kwargs):
        current_sec=int(self.text())
        current_sec-=1
        if current_sec==0:
            self.setText('')
            self.killTimer(self.timer_id)
        else:
            self.setText(str(current_sec))



def run():
    app=QApplication(sys.argv)
    window=Window()

    # label=label_time(5,window)
    area1=area_player([],5,window)
    window.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    run()