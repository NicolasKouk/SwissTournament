import random

from player import Player
from utils import is_in_list_of_pairs

class Standings:
    def __init__(self, table):
        self.table = table
    
    def shuffle(self, last_player_gets_the_bye):
        if not last_player_gets_the_bye:
            random.shuffle(self.table)
        else:
            temp = self.table[:-1]
            last_elem = self.table[-1]
            random.shuffle(temp)
            self.table = temp + [last_elem]
    
    def find_next_matches(self):
        nop = len(self.table) # number of players
        matches_list = []
        p1 = Player("")
        removed_match = (0,0)

        # find the bye
        if nop % 2 != 0:
            for i in range(nop-1, 0, -1):
                if self.table[i].byes == 0:
                    matches_list.append((self.table[i], "Bye"))
                    self.table[i].byes = 1
                    break


        while len(matches_list) < len(self.table)/2:
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
        counter = 1
        for p in self.table:
            s += (2-len(str(counter))) * " " + str(counter) + ". " 
            s += p.long_print()
            s += "\n"
            counter += 1
        return s