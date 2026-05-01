class Player:
	def __init__(self, name):
		self.name = name
		self.wins = 0
		self.losses = 0 
		self.points = 0 
		self.hasPlayedWith = []
		self.ptsFor = 0
		self.ptsAgainst = 0

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
		s = self.name + " " + str(self.wins) + "-" + str(self.losses) + " " + str(self.points) + "pts"
		s += " (" + str(self.ptsFor) + "-" + str(self.ptsAgainst) + ")"
		return s
	
	def points_calibration(self):
		self.points = 2*self.wins + self.losses
