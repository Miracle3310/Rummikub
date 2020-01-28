import process

def run(cards):
    # 判断顺子
    color = process.take_color(cards)
    number=process.take_number(cards)
    # print(number,color)
    return (max(number) - min(number) + 1) == len(set(number)) and len(set(number)) >= 3 and len(set(color))==1


def group(cards):
    # 判断对子
    color=process.take_color(cards)
    number=process.take_number(cards)
    return len(set(color))>=3 and len(set(color))==len(color) and len(set(number))==1


def check(cards):
    return run(cards) or group(cards)


def experience():
    cards=[413,412,411]
    print(check(cards))

if __name__ == '__main__':
    experience()
