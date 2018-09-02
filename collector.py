import requests
import json
from projectLogger import ProjectLogger


logger = ProjectLogger(log_file_path ='project.log')




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
			return data
			#return (data['EUR_BDT']['val'])
			# for item in response.json():
			# 	for val in item:
			# 		print val
    			


class Weather(object):
	def __init__(self):
		logger.info("Intialized  Weather")

	def collectCurrentWather(self):

		response = requests.get("http://api.openweathermap.org/data/2.5/weather?q=Sonnenberg,DE&APPID=885b527482b54b097a23c78a43660402")
			
		if response.status_code != 200:
    		# This means something went wrong.
			logger.error("collectCurrentWather failed")
			return
		return json.loads (response.text)	
		#data = json.loads(response.text)
		#return (data['EUR_BDT']['val'])	



#test
#test = ExchangeRate()
#print test.collectEUROtoBDTRate()


#t = Weather()
#print (t.collectCurrentTemparature())

