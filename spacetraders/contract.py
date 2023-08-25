class Contract():
    def __init__(self, data):
        self.account_id = data['accountId']
        self.symbol = data['symbol']
        self.headquarters = data['headquarters']
        self.credits = data['credits']
        self.starting_faction = data['startingFaction']

    def __str__(self):
        string = f" \
        Acct: {self.account_id}\n \
        Symb: {self.symbol}\n \
        Head: {self.headquarters}\n \
        Cred: {self.credits}\n \
        Fact: {self.starting_faction}\n"
        return string
