def take_number(cards):
    if isinstance(cards, list):
        return [(card % 100) for card in cards]
    elif isinstance(cards,int):
        return (cards % 100)
    raise Exception("cards' types are not supported!")


def take_color(cards):
    if isinstance(cards, list):
        return [card//100 for card in cards]
    elif isinstance(cards, int):
        return cards//100
    raise Exception("cards' types are not supported!")


def color2str(color):
    if color==1:
        str= 'red'
    elif color==2:
        str='blue'
    elif color == 3:
        str='green'
    elif color==4:
        str='black'
    else:
        str='brown'
    return str

# def take_end(cards):
#     if isinstance(cards, list):
#         return [card%10 for card in cards]
#     elif isinstance(cards, int):
#         return cards%10
#     raise Exception("cards' types are not supported!")
