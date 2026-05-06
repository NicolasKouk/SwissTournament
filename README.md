# SwissTournament

A program to help organize a tournament with Swiss team-pairing format. Each player plays a few games; first with random players and gradually with players close to his/her level. Players cannot be paired with each other more than once. 

For more information, visit [Swiss system tournament](https://en.wikipedia.org/wiki/Swiss-system_tournament)

## Get Started

- Clone the repository
- Edit `playerslist.txt`, by simply writing the players' names separated by line breaks. 
- Open a terminal. Reach the correct path by typing: 
```cd <your-path>\SwissTournament```
- Run the project with this command: 
```python swiss_tournament.py```

## Play 

In each round, the current standings are displayed, with useful information about each player, along with the next fixtures. All you need to do is enter the result of the match in the format `11-9`. 

After 5 rounds, the final standings are displayed and the winner is revealed. 

### Tie Breakers:
Tie breakers are used to deterministically rank all players. In order, they are:
1. Total Points. 2 points are awarded for each win, and 1 point for each loss. 
2. MBS. It stands for Modified Buchholz Score. It calculates the average rank of the opponents that each player faced. It gives an idea of how difficult schedule each player has. It is only active and displayed at the final standings.
3. Set Point difference. The player that cumulatively scores the most points and conceids the least is being prefered.
4. Set Points for. The cumulative points each player scores in each game. 

## Notes

- This has been made for table tennis, so no draws are supported. 
- In case the number of players is even, there is a player in every round that doesn't play a match (Bye). This player is selected as the weakest player that has not yet received a Bye before. Such a player is awarded a win in that round. 
