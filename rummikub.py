import random
import rule
import process
import numpy as np
from rummikub_desk_check import check
'''
单机对战：
1. 三大类：牌堆，玩家，桌面
    牌堆：
    玩家：
    桌面：
2.规则：
    1.顺子
    2.对子
    3.破冰
    4.罚摸
    5.胜利条件
3.todo：
    1.joker处理
    2.罚摸判断
    3.桌面牌是否合规
    4.判断玩家打算放入的牌是否与它所想的合规
        两种编程思路：
        1.每次只考虑玩家放进去的牌 ———— 简单，
                                    但是很难实现readme中设想的玩家任意移动牌的情景，
                                    那一部分应该交给游戏界面编写来完成
        2.玩家出完牌，考虑桌面的牌是否合规 ————困难
'''

class card_decks():
    def __init__(self):
        # 数牌：4种花色，1-13数字，共104张
        # joker：2张
        #   1   |   10   |   0
        # color | number |  0/1
        # 1-4, 01-13, 0-1
        # joker: 5xxx
        # self.card=[i*1000+j*10+k for i in range(1,5) for j in range(1,14) for k in range(0,2)]+[5000,5001]
        self.card = [i * 100 + j for i in range(1, 5) for j in range(1, 14)] + [500]
        self.card=self.card+self.card
        # self.shuffle()
        # self.quantity=len(self.card)

        # self.print_p()

    @property
    def quantity(self):
        return len(self.card)

    def shuffle(self):
        random.shuffle(self.card)  # shuffle cards

    def draw(self,count):
        return [self.card.pop() for i in range(min(count,self.quantity))]

    def print_p(self):
        print('-'*50)
        print('card decks:')
        print('\n'.join(['%s:%s' % item for item in self.__dict__.items()]))
        print('-' * 50)


class player():
    def __init__(self,number):
        self.number=number  # 玩家序号
        self.card=[]
        # self.quantity=0
        self.breaking_ice=False

    @property
    def quantity(self):
        return len(self.card)

    @property
    def cards_sum(self):
        number_list=process.take_number(self.card)
        return sum(number_list)

    def take_out(self, cards):
        # 未加规则判断
        for card in cards:
            if card not in self.card:
                # print('Player '+str(self.number)+' does not have card '+str(card))
                raise Exception('Player '+str(self.number)+' does not have card '+str(card))
                # return False
            else:
                self.card.remove(card)
        # self.quantity-=len(cards)
        return cards

    def play(self,cards):
        if not self.breaking_ice:
            if rule.check(cards) and sum(process.take_number(cards))>=30: # todo:joker破冰时的判断
                self.breaking_ice=True
                # try:
                #     self.take_out(cards)
                # except KeyError:
                #     print('input another cards')
                self.take_out(cards)
            else:
                raise Exception('You need break ice first')
        else:
            # 检测是否符合规则
            self.take_out(cards)
        return cards

    def cards_sort(self):
        self.card.sort()


class desk():
    def __init__(self):
        self.card=[]
        # self.quantity=0
        # self.desk=np.zeros((5,14))
        # self.desk=[[0 for i in range(14)] for j in range(5)]


    # def desk_card(self,cards=[]):
    #     # 牌进入桌面，记录矩阵变化
    #     self.card=self.card+cards
    #     for card in self.card:
    #         self.desk[process.take_color(card)][process.take_number(card)]+=1

    @property
    def quantity(self):
        return len(self.card)

    def desk_check(self):
        return check(self.card)


    def print_p(self):
        print('-'*50)
        print('card desk:')
        print('\n'.join(['%s:%s' % item for item in self.__dict__.items()]))
        print('-' * 50)


def test():
    # card_deck=card_decks()
    # card_deck.print_p()
    # a=card_deck.draw(1)
    # print(a)
    # card_deck.print_p()
    #
    # p1=player(1)
    # p1.card=card_deck.draw(13)
    # p1.take_out([413])
    # card_deck.print_p()

    d=desk()

    d.card=[401,110,113]
    d.print_p()

    print(d.quantity)
    print(d.desk_check())


def main():
    instruction='-'*21+'游戏说明'+'-'*21+'\n' \
                '每张牌用一个三位数表示，百位表示花色，后两位表示数字。\n' \
                '根据提示输入即可。\n' \
                '一起快乐打以色列麻将吧！'
    print(instruction)
    # player_number=int(input('请输入玩家数量（2-4）：'))
    player_number=2
    while player_number<2 or player_number>4:
        player_number = int(input('请输入玩家数量（2-4）：'))
    p_all=[player(i) for i in range(player_number)]
    # print(p[0].number)
    deck_p=card_decks()
    deck_p.shuffle() #洗牌
    desk_p=desk()  # p表示playing

    for p in p_all:
        p.card=deck_p.draw(13) #起始手牌数量

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



if __name__ == '__main__':
    # test()
    main()