
import logging


LOG_LEVEL = logging.INFO


class ProjectLogger(object):
	"""A customer of ABC Bank with a checking account. Customers have the
	following properties:

	Attributes:
		name: A string representing the customer's name.
		balance: A float tracking the current balance of the customer's account.
	"""

	def __init__(self, log_file_path):
		"""Return a Customer object whose name is *name*.""" 
		logging.basicConfig(level=LOG_LEVEL)
		self.logger = logging.getLogger(__name__)
		
		# create a file handler
		self.handler = logging.FileHandler(log_file_path)
		self.handler.setLevel(LOG_LEVEL)

		# create a logging format
		self.formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
		self.handler.setFormatter(self.formatter)

		# add the handlers to the logger
		self.logger.addHandler(self.handler)
		

	def info(self,message):
		self.logger.info(message)
		
	def debug(self,message):
		self.logger.debug(message)
		
	def error(self,message):
		self.logger.error(message)
		
		
		
		
#test
#test = ProjectLogger(log_file_path ='project.log')
#test.debug("HI baby")
#test.error("HI yff baby")