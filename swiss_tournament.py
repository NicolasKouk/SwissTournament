from match import Match
from player import Player
from standings import Standings
from utils import is_in_list_of_pairs, is_valid_score, result_to_scores

N = 5 # number of rounds

f = open("playerslist.txt")
players = []
for name in f:
    players.append(Player(name.rstrip()))
f.close()

standings = Standings(players)

print(standings)
# At first a random draw is made to determine the first pairings
standings.shuffle()
print()

# begin tournament
n = 1
while(n <= 5):
    print(20*"\n")
    print(standings)
    print()

    print("Round " + str(n) + ":")
    next_matches = standings.find_next_matches()
    for (i,j) in next_matches:
        if j != "Bye":
            print(i, "vs", j)
        else:
            print(i, j)
    print()

    for (p1,p2) in next_matches:
        if p2 == "Bye":
            p1.wins += 1
            p1.hasPlayedWith.append(Match("Bye", 0, 0))
            p1.points_calibration()

        else:
            result = ""
            while not is_valid_score(result):
                result = input("Type result for " + str(p1.name) + " vs " + str(p2.name) + "  ")
            scores = result_to_scores(result)
            if scores[0] > scores[1]:
                p1.wins += 1
                p2.losses += 1
            else:
                p2.wins += 1
                p1.losses += 1
            p1.ptsFor += scores[0]
            p1.ptsAgainst += scores[1]
            p2.ptsFor += scores[1]
            p2.ptsAgainst += scores[0]

            p1.hasPlayedWith.append(Match(p2, scores[0], scores[1]))
            p2.hasPlayedWith.append(Match(p1, scores[1], scores[0]))

            p1.points_calibration()
            p2.points_calibration()
    n += 1
    standings.table=sorted(standings.table, key = lambda x: (-x.points, x.ptsAgainst-x.ptsFor))
    a = input()



print(20*"\n")
print("Final Standings:")
print(standings)
print()
