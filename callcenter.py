import enum
class Status(enum):
	ongoing = "ongoing"
	finished = "finished" 
	incoming = "incoming" 

class Levels(enum):
	firstLevel = "firstLevelEmps"
	secondLevel = "secondLevelEmps" 
	thirdLevel = "thirdLevelEmps" 

class Call:
	def __init__(self):
		self.status = Status.incoming
		self.assignee = None

class Employee():
    def __init__(self, isAvailable, ranking, name, location):
        self.isAvailable = isAvailable
        self.ranking = ranking
        self.name = name
        self.location = location

class CallCenter(): 
	def __init__(self, isAvailable):
		self.isAvailable = isAvailable
		self.emps = {}
	# assumes this creates this structure
	# emps = {
		#firstLevelEmps: [{Employee: T or F}, {Employee: T or F}, {Employee: T or F]}
		#secondLevelEmps: [{Employee: T or F}, {Employee: T or F}, {Employee: T or F]}
		#thirdLevelEmps: [{Employee: T or F}, {Employee: T or F}, {Employee: T or F]}
#}
	def buildLevels(self):
		pass
	
	def dispatchCalls(self, Call):
		# first loop for firstLevel
		if CallCenter.isAvailable == False:
			return "Exception"
		for emp, isAvail in self.emps[Levels.firstLevel].items():
			if isAvail:
				Call.status = Status.ongoing
				Call.assignee = emp
				isAvail = False
				return 
		for emp, isAvail in self.emps[Levels.secondLevel].items():
			if isAvail:
				Call.status = Status.ongoing
				Call.assignee = emp
				isAvail = False
				return 
		
		for emp, isAvail in self.emps[Levels.thirdLevel].items():
			if isAvail:
				Call.status = Status.ongoing
				Call.assignee = emp
				isAvail = False
				return 

		CallCenter.isAvailable = False
		return "Exceptions"
