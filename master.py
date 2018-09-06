
from googleSpreadSheet import SpreadsheetWriter
from  collector 	import 		ExchangeRate
from  collector 	import 		Weather
from  connections 	import 	Connections


import datetime
import time
import json

from projectLogger import ProjectLogger


logger = ProjectLogger(log_file_path ='project.log')



SHOW_EXCHANGE_RATE_EVERY 	= 	20	#3600/2 	#sec
SHOW_CURRENT_TEMP_EVERY 	= 	30	#60*5 	#sec
SHOW_CONNECTIONS_EVERY 		= 	40	#60*5 	#sec
SHOW_APPOINTMENTS_EVERY 	= 	50	#3600 	#sec


SHOW_DATA_AT="spread_sheet"


class SreadSheet(object):
	
	def __init__(self):
		self.spredsheet_writer = 	SpreadsheetWriter(credentials_file_path='optimal-cabinet-213218-fd755cec2c94.json',sheet_name='test')

	def show_exchage_rate(self,data):
		data_to_show = str (data['EUR_BDT']['val'])[:5]
		self.spredsheet_writer.write_at('J2',data_to_show)

	def show_current_weather(self,data):
		temparature = data['main']['temp'] - 273.15 #covert kelvin to celc
		temparature = str (temparature)[:2]

		temparature_max = data['main']['temp_max'] - 273.15 #covert kelvin to celc
		temparature_max = str (temparature_max)[:2]

		temparature_min = data['main']['temp_min'] - 273.15 #covert kelvin to celc
		temparature_min = str (temparature_min)[:2]

		humidity = data['main']['humidity'] 
		humidity = "Humidity "+str (humidity)+ "%"


		self.spredsheet_writer.write_at('A2',temparature)
		self.spredsheet_writer.write_at('C2',temparature_max)
		self.spredsheet_writer.write_at('C4',temparature_min)
		self.spredsheet_writer.write_at('B2',humidity)

	def show_connections(self,data):

		transport_cell = "E"
		time_cell = "D"
		direction_cell = "F"

		start_row_number = 2 
		json_data = json.loads(data)
		print (json_data)
		for item in json_data:
			self.spredsheet_writer.write_at(time_cell + str (start_row_number),item['time'])
			self.spredsheet_writer.write_at(transport_cell + str (start_row_number),item['transport'])
			self.spredsheet_writer.write_at(direction_cell + str (start_row_number),item['direction'])
			start_row_number +=1
			

class Master(object):
	"""This class controls all other plugins:

	Attributes:
		name: A string representing the customer's name.
		balance: A float tracking the current balance of the customer's account.
	"""

	def __init__(self):
		"""Return a Customer object whose name is *name*.""" 

		self.exchangeRate = ExchangeRate()
		self.weather      = Weather()
		self.myconnection = Connections()
		 
		
		#place holder for other option
		if (SHOW_DATA_AT=="spread_sheet"):
			self.data_visualizer = SreadSheet()
		

		self.reset()


	def reset(self):
		self.date_timeLast_sccessful_access_exchange_rate 	=	datetime.datetime.now() - datetime.timedelta(days=7)
		self.date_timeLast_sccessful_access_current_temp 	=	datetime.datetime.now() - datetime.timedelta(days=7)
		self.date_timeLast_sccessful_access_connections  	=	datetime.datetime.now() - datetime.timedelta(days=7)
		self.date_timeLast_sccessful_access_appoitments  	=	datetime.datetime.now() - datetime.timedelta(days=7)





	def show_exchage_rate(self):

		data = self.exchangeRate.collectEUROtoBDTRate()
		self.data_visualizer.show_exchage_rate(data)

	def show_current_weather(self):
		data = self.weather.collectCurrentWather()
		self.data_visualizer.show_current_weather(data)

	def show_connections(self):
		data = self.myconnection.scrape('5006157',["Backnang","Bietigheim-Bissingen"])
		self.data_visualizer.show_connections(data)
	

	
	
	
	def update(self):

		if ( (datetime.datetime.now() - self.date_timeLast_sccessful_access_exchange_rate).total_seconds()
			> SHOW_EXCHANGE_RATE_EVERY ):
			print ("process exchange rate")
			#todo heathcheck
			self.show_exchage_rate()
			self.date_timeLast_sccessful_access_exchange_rate 	=	datetime.datetime.now()
		
		if ( (datetime.datetime.now() - self.date_timeLast_sccessful_access_current_temp).total_seconds()
			> SHOW_CURRENT_TEMP_EVERY ):
			print ("process tempa")
			#todo heathcheck
			self.show_current_weather()
			self.date_timeLast_sccessful_access_current_temp 	=	datetime.datetime.now()

		
		if ( (datetime.datetime.now() - self.date_timeLast_sccessful_access_connections).total_seconds()
			> SHOW_CONNECTIONS_EVERY ):
		
			print ("process connection")
			#todo heathcheck
			self.show_connections()
			self.date_timeLast_sccessful_access_connections 	=	datetime.datetime.now()
			

		if ( (datetime.datetime.now() - self.date_timeLast_sccessful_access_appoitments).total_seconds()
			> SHOW_APPOINTMENTS_EVERY ):
			print ("process appointments")
			#todo heathcheck
			self.date_timeLast_sccessful_access_appoitments 	=	datetime.datetime.now()

	


	def process(self):
		number=0
		while(1):
			#logger.info("Processing weather.....")
			#self.spredsheet_controler.write_at('A2',str(number))
			#number = number +1
			self.update()
			time.sleep(1)#sec
		
		
#test
test = Master()
test.process()
#test.error("HI yff baby")