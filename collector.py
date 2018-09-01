import requests
import json
from projectLogger import ProjectLogger


logger = ProjectLogger(log_file_path ='project.log')



class Manager(object):
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




class ExchangeRate(object):
	
	def __init__(self):
		logger.info("Intialized  ExchangeRate")

	def collectEUROtoBDTRate(self):
			response = requests.get("http://free.currencyconverterapi.com/api/v5/convert?q=EUR_BDT&compact=y")
			
			if response.status_code != 200:
    			# This means something went wrong.
				logger.error("collectEUROtoBDTRate failed")
				return
			data = json.loads(response.text)
			return (data['EUR_BDT']['val'])
			# for item in response.json():
			# 	for val in item:
			# 		print val
    			


class Weather(object):
	def __init__(self):
		logger.info("Intialized  Weather")

	def collectCurrentTemparature(self):

		response = requests.get("http://api.openweathermap.org/data/2.5/weather?q=Sonnenberg,DE&APPID=885b527482b54b097a23c78a43660402")
			
		if response.status_code != 200:
    		# This means something went wrong.
			logger.error("collectCurrentTemparature failed")
			return
		return json.loads (response.text)	
		#data = json.loads(response.text)
		#return (data['EUR_BDT']['val'])	



#test
#test = ExchangeRate()
#print test.collectEUROtoBDTRate()


t = Weather()
print (t.collectCurrentTemparature())

