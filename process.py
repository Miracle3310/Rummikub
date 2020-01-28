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


# def take_end(cards):
#     if isinstance(cards, list):
#         return [card%10 for card in cards]
#     elif isinstance(cards, int):
#         return cards%10
#     raise Exception("cards' types are not supported!")
