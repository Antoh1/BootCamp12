class Calendar(object):
	def __init__(self, event, event_time):
		self.event = event
		self.event_time = event_time
		

	def create(self, event, event_time):
		self.schedule = {1:{self.event:self.event_time}}
		event_time = raw_input("Enter your event time: ")
		event = raw_input("Enter event at this time: ")
		count = 1
		if self.schedule[count[event]] == self.schedule[self.count[self.event]]:
			return "The day-time is already occupied with another event"
		elif self.schedule == {1:{self.event:self.event_time}}:
			self.schedule[count] = self.schedule[count[self.event]]


anto = Calendar("My event", "16/11/2016")
print(anto.create("My event", "16/11/2016"))	    	
	    


