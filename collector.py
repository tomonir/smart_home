from __future__ import print_function
import datetime
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools


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
    			



# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/calendar.readonly'
class Appointments(object):

		def __init__(self,service):
			self.service = service
			
		def collectAppointments(self,request_num_of_appoinments=10):
			return
			

class Test(object):
	def __init__(self):
		data = 1
		data2 = data + 1
	def getData(self):
		return 1	


#test
#test = ExchangeRate()
#print test.collectEUROtoBDTRate()


store = file.Storage('token.json')
creds = store.get()

creds = store.get()
if not creds or creds.invalid:
	flow = client.flow_from_clientsecrets('calender_credentials.json', SCOPES)
	creds = tools.run_flow(flow, store)
service = build('calendar', 'v3', http=creds.authorize(Http()))	

test = Appointments(service)
#print test.collectEUROtoBDTRate()

#t = Test()
#print (t.getData())

