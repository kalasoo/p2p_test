class TestObj(Object):
	def __init__(self, config):
		self.config = config
	def setup(self):
		pass
	def start(self):
		pass
	def check(self):
		pass
	def end(self):
		pass
	def clean(self):
		pass
	def getlog(self):

class NeP2P_TestObj(TestObj):
	def __init__(self,config):
		TestObj.__init__(self,config)