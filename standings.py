import random

from player import Player
from utils import is_in_list_of_pairs

class Standings:
    def __init__(self, table):
        self.table = table
    
    def shuffle(self):
        random.shuffle(self.table)
    
    def find_next_matches(self):
        matches_list = []
        p1 = Player("")
        removed_match = (0,0)
        while len(matches_list) != len(self.table)/2:
            for p in self.table:
                if not is_in_list_of_pairs(matches_list, p):
                    p1 = p
#                    print(p1)
                    break

            remaining = [p for p in self.table if not is_in_list_of_pairs(matches_list, p)]            
            possible_opponents1 = [p for p in remaining if (p not in [ph.opponent for ph in p1.hasPlayedWith] and p1 != p)]
            possible_opponents = [p for p in possible_opponents1 if (p1, p) != removed_match]
#            for p_debug in possible_opponents:
#                print(p_debug)


            if not possible_opponents:
                removed_match = matches_list.pop()
                continue
            p2 = possible_opponents[0]
            matches_list.append((p1, p2))
#            for (i,j) in matches_list:
#                print(i, "vs", j)
#            print()
        return matches_list


    def __str__(self):
        s = ""
        for p in self.table:
            s += p.long_print()
            s += "\n"
        return s