class Waypoint():
    def __init__(self, data):
        self.sector = data['symbol'].split("-")[0]
        self.system = data['systemSymbol']
        self.symbol = data['symbol']
        self.type = data['type']
        self.x = data['x']
        self.y = data['y']
        self.orbitals = data["orbitals"]
        self.faction = data["faction"]
        self.traits = data["traits"]
        self.chart = data["chart"]

    def __str__(self):
        string = f" \
        Sect: {self.sector}\n \
        Sys : {self.system}\n \
        Symb: {self.symbol}\n \
        Type: {self.type}\n \
        X   : {self.x}\n \
        Y   : {self.y}\n \
        Orbi: {self.orbitals}\n \
        Fact: {self.faction}\n \
        Trai: {self.traits}\n \
        Char: {self.chart}\n \
"
        return string
