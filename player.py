class Player:
	def __init__(self, name):
		self.name = name
		self.wins = 0
		self.losses = 0 
		self.points = 0 
		self.hasPlayedWith = []
		self.ptsFor = 0
		self.ptsAgainst = 0
		self.byes = 0
		self.buchholz = 0.0

	def getName(self):
		return self.name
	def getWins(self):
		return self.wins
	def getLosses(self):
		return self.losses
	def getPoints(self):
		return self.points
	def getHasPlayedWith(self):
		return self.hasPlayedWith
	def getPtsFor(self):
		return self.ptsFor
	def getPtsAgainst(self):
		return self.ptsAgainst
    
	def __str__(self):
		s = self.name + " (" + str(self.points) + "pts)"
		return s
	
	def long_print(self):
		s = self.name + (15-len(self.name))*" "
		s += str(self.wins) + "-" + str(self.losses) + " " + str(self.points) + "pts "
		if self.buchholz != 0:
			s += str(self.buchholz) + (4-len(str(self.buchholz))) * " "
		s += "(" + str(self.ptsFor) + "-" + str(self.ptsAgainst) + ")        "
		for m in self.hasPlayedWith:
			s += str(m)
		return s

	def points_calibration(self):
		self.points = 2*self.wins + self.losses

	def buchholz_calibration(self, standings):
		if not self.hasPlayedWith:
			return 0
		mysum = 0.0
		for m in self.hasPlayedWith:
			if m.opponent == "Bye":
				mysum += len(standings.table)
				continue
			opponent_name = m.opponent.name
			for i in range(len(standings.table)):
				if standings.table[i].name == opponent_name:
					mysum += i+1
					break
		self.buchholz = round(mysum / len(self.hasPlayedWith), 1)


