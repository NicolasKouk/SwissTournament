import random

class Standings:
    def __init__(self, table):
        self.table = table
    
    def shuffle(self):
        random.shuffle(self.table)

    def __str__(self):
        s = ""
        for p in self.table:
            s += str(p)
            s += "\n"
        return s