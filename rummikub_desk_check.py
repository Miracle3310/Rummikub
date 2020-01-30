# 2020.1.28
# group()决定了只能四种花色，run()则可以突破13的限制

from process import take_number

def check(cards_origin):
    '''
    :param cards: [111,211,311,...]
    :return: T/F
    '''
    def check_one(cards_origin,card):
        cards=cards_origin.copy()
        R = run(cards, card)
        if R!=False:
            for possible_r in R:
                cards_copy=cards.copy()
                for i in possible_r:
                    cards_copy.remove(i)
                cards_r=cards_copy
                if check(cards_r):
                    return True
        G=group(cards,card)
        if G!=False:
            # print(G)
            for possible_g in G:
                cards_copy = cards.copy()
                for i in possible_g:
                    # print('cards_copy:',cards_copy,'i:',i)
                    cards_copy.remove(i)
                cards_g = cards_copy
                if check(cards_g):
                    return True
        return False

    if cards_origin==[]:
        return True

    if 500 not in cards_origin:
        # for card in cards_origin:
        card=cards_origin[-1]
        if not check_one(cards_origin,card):
            return False
        return True
    else:
        cards_origin.remove(500)
        for joker in [i * 100 + j for i in range(1, 5) for j in range(1, 14)]:
            cards_origin.append(joker)
            # cards_origin=[joker]+cards_origin
            if check(cards_origin):
                return True
            cards_origin.remove(joker)
        return False


def run(cards,target):
    # 找最邻近的上下的0
    up=down=target
    while up in cards:
        # print('up:',up)
        up+=1
    while down in cards:
        # print('down:',down)
        down-=1
    up-=1
    down+=1
    # print(up,down)
    # 假如长度小于3，直接结束
    if up-down+1<3:
        return False

    # 生成输出数组（假如上面不为False，则一定有输出）
    output_1=[[i,j] for i in range(down, target+1) for j in range(target,up+1)]
    output=[]
    for item in output_1:
        if max(item)-min(item)+1<3:
            continue
        item=[i for i in range(item[0],item[1]+1)]
        output.append(item)

    return output


def group(cards,target):
    output=[]
    for i in range(1,5):
        j=i*100+take_number(target)
        if j !=target and j in cards:
            output.append(j)

    if len(output)<2:
        return False
    if len(output)==2:
        return [[target]+output]
    if len(output)==3:
        return [[target]+output,[target]+[output[0],output[1]],
                [target]+[output[0],output[2]],[target]+[output[1],output[2]]] # STUPID


def main():
    cards=[110,210,310,110,
           111,211,311,411,
           112,
           113,
           101,201,301
           ]
    card=111
    # print(run(cards,card))
    # print(group(cards,card))

    print(check(cards))


if __name__ == '__main__':
    main()
