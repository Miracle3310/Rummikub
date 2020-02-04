from game import rummikub
from PyQt5 import QtCore, QtGui, QtWidgets
from game_widget import Ui_Form
from custom_widget import *

def prepare():
    # instruction = '-' * 21 + '游戏说明' + '-' * 21 + '\n' \
    #                                              '每张牌用一个三位数表示，百位表示花色，后两位表示数字。\n' \
    #                                              '根据提示输入即可。\n' \
    #                                              '一起快乐打以色列麻将吧！'
    instruction='-' * 21 + '游戏开始' + '-' * 21
    print(instruction)
    # player_number=int(input('请输入玩家数量（2-4）：'))
    player_number = 4
    while player_number < 2 or player_number > 4:
        player_number = int(input('请输入玩家数量（2-4）：'))
    p_all = [rummikub.player(i) for i in range(player_number)]
    # print(p[0].number)
    deck_p = rummikub.card_decks()
    deck_p.shuffle()  # 洗牌
    desk_p = rummikub.desk()  # p表示playing

    for p in p_all:
        p.card = deck_p.draw(13)  # 起始手牌数量

    return p_all,deck_p,desk_p


def play_without_GUI():

    p_all, deck_p, desk_p=prepare()

    over=False
    while not over:
        for p in p_all :
            if over:
                break
            print('-'*50)
            print(str(p.number+1)+'号玩家出牌')
            p.cards_sort()  # 理牌
            print('手牌：', p.card)
            print('桌面：', desk_p.card)
            if 'p'!=input('是否出牌（p）：'): # 选择摸牌
                p.card+=deck_p.draw(1)
                if deck_p.quantity==0:
                    over=True
            else: # 选择打牌
                desk_backup=desk_p.card.copy()
                p_backup=p.card.copy()

                input_off = False  # 本轮是否打完
                while not input_off:
                    play_off=False # 控制打出的牌是否合规
                    while (not play_off) : # 直到打出的牌合规
                        try:
                            p.cards_sort() # 理牌
                            print('手牌：',p.card)
                            print('桌面：',desk_p.card)
                            cards = input('输入要打的牌（空格隔开，n表示不出牌）：\n')  # todo:未检查是否符合语法
                            if cards!='n':
                                input_cards = [int(i) for i in cards.split(' ')]
                                desk_p.card+=p.play(input_cards)
                            play_off=True
                        except Exception as e:
                            print(e)
                    if cards!='n':
                        if not desk_p.desk_check() : # 桌上牌不合规
                            #桌上的牌不合规
                            #本轮结束
                            input_off=True
                            #复原
                            desk_p.card=desk_backup
                            p.card=p_backup
                            #罚摸
                            p.card+=deck_p.draw(3)
                            #检测是否摸完
                            if deck_p.quantity == 0:
                                over = True
                    else:
                        input_off=True
                        if desk_backup==desk_p.card: # 选择打牌但没有打出牌
                            # 罚摸
                            p.card += deck_p.draw(3)
                            # 检测是否摸完
                            if deck_p.quantity == 0:
                                over = True
                        else:
                            if p.quantity == 0:
                                over = True

    winner=[i.cards_sum for i in p_all].index(min([i.cards_sum for i in p_all]))
    print('-'*50)
    print('Game Over!')
    print('Winner:',str(winner+1)+'号玩家')


def play_with_GUI():
    import sys
    app = QtWidgets.QApplication(sys.argv)

    # 准备阶段
    p_all, deck_p, desk_p = prepare()
    ui_p_all=[]

    # 显示桌面
    for p in p_all:
        ui_p_all.append(window(player=p,deck=deck_p,desk=desk_p))

    # 正式开始


    sys.exit(app.exec_())




if __name__ == '__main__':
    # test()
    play_with_GUI()