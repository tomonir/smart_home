
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from projectLogger import ProjectLogger


logger = ProjectLogger(log_file_path ='project.log')




class SpreadsheetWriter(object):
	"""A customer of ABC Bank with a checking account. Customers have the
	following properties:

	Attributes:
		name: A string representing the customer's name.
		balance: A float tracking the current balance of the customer's account.
	"""

	def __init__(self, credentials_file_path,sheet_name):
		"""Return a Customer object whose name is *name*.""" 
		self.scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
		 
		try: 
			self.credentials = ServiceAccountCredentials.from_json_keyfile_name(credentials_file_path, self.scope)
			self.gc_gspread = gspread.authorize(self.credentials)
			self.workSheet = self.gc_gspread.open(sheet_name).sheet1#TODO: make sheet1 as a variable
		except:
			logger.error("Connection failed to spreadsheets.google.com")


	def write_at(self,at,what):
		try:
			self.workSheet.update_acell(at, what)
		except:
			logger.error("Wrting failed at" + at)



#test = SpreadsheetWriter(credentials_file_path='optimal-cabinet-213218-fd755cec2c94.json',sheet_name='test')
#test.write_at('A2','90')