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

In each round, the current standings are displayed, with useful information about each player, along with the next fixtures. All you need to do is enter the result of the match in the format `2-1`. 

In the end, the final standings are displayed and the winner is revealed. 

# Notes

- This has been made for table tennis, so no draws are supported. 
