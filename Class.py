class Computer:
	def __init__(self, id, model, price, os_id):
		self.id = id
		self.model = model
		self.price = price
		self.os_id = os_id
		
class OperatingSystem:
	def __init__(self, id, model, creation_year):
		self.id = id
		self.model = model
		self.creation_year = creation_year
	
class OSC:
	
	def __init__(self, os_id, computer_id):
		self.os_id = os_id
		self.computer_id = computer_id
