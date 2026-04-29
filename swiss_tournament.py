from player import Player
from standings import Standings

N = 5 # number of rounds

f = open("playerslist.txt")
players = []
for name in f:
    players.append(Player(name.rstrip()))
f.close()

standings = Standings(players)

print(standings)
standings.shuffle()
print()
print(standings)

# begin tournament
n = 1
while(n <= 5):
    print(standings)
    print("Next matches:")
    print()
    n += 1
    a = input()

