class Match:
    def __init__(self, opp, n1, n2):
        self.opponent = opp
        self.score1 = n1
        self.score2 = n2

    def __str__(self):
        maxlen = 25
        if self.opponent == "Bye":
            return "Bye" + (maxlen-3) * " "
        s = "W " if self.score1 > self.score2 else "L "
        s += str(self.score1) + "-" + str(self.score2) + " vs " + str(self.opponent.name)
        s += (maxlen-len(s)) * " "
        return s 

    