
from googleSpreadSheet import SpreadsheetWriter
import time

from projectLogger import ProjectLogger


logger = ProjectLogger(log_file_path ='project.log')



class Master(object):
	"""This class controls all other plugins:

	Attributes:
		name: A string representing the customer's name.
		balance: A float tracking the current balance of the customer's account.
	"""

	def __init__(self):
		"""Return a Customer object whose name is *name*.""" 
		self.spredsheet_controler = 	SpreadsheetWriter(credentials_file_path='optimal-cabinet-213218-fd755cec2c94.json',sheet_name='test')
	
	def process(self):
		number=0
		while(1):
			logger.info("Processing weather.....")
			self.spredsheet_controler.write_at('A2',str(number))
			number = number +1
			time.sleep(2)#sec
		
		
#test
test = Master()
test.process()
#test.error("HI yff baby")