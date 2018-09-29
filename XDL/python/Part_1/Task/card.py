class Card:

    def __init__(self, cardid, password, money):
        self.cardid = cardid
        self.password = password
        self.money = money
        self.islock = False
