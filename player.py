class Player:
	def __init__(self, name):
		self.name = name
		self.wins = 0
		self.losses = 0 
		self.points = 0 
		self.hasPlayedWith = []

    
	def __str__(self):
		return self.name + " " + str(self.wins) + "-" + str(self.losses) + " " + str(self.points) + "pts"
	
	def points_calibration(self):
		self.points = 2*self.wins + self.losses
