from datetime import datetime
import json

from bs4 import BeautifulSoup
#import click
import requests
import pytz


URL = ('http://www2.vvs.de/vvs/widget/XML_DM_REQUEST?zocationServerActive=1'
       '&lsShowTrainsExplicit1&stateless=1&language=de&SpEncId=0&anySigWhenPerfectNoOtherMatches=1'
       '&depArr=departure&type_dm=any&anyObjFilter_dm=2&deleteAssignedStops=1&useRealtime=1'
       '&mode=direct&dmLineSelectionAll=1&name_dm={station_id}&itdDateYear={year}&itdDateMonth={month}'
       '&itdDateDay={day}&itdTimeHour={hour}&itdTimeMinute={minute}&limit={limit}')

TIME_FORMAT = '%Y-%m-%d %H:%M'

TIMEZONE = pytz.timezone('Europe/Berlin')





class Connections(object):
    def __init__(self):
        return

    def _now(self):
        return datetime.now().replace(tzinfo=TIMEZONE)


    def search(self,station_id, limit=50):
        now = self._now()
        ctx = {
            'station_id': station_id,
            'year': now.year,
            'month': now.month,
            'day': now.day,
            'hour': now.hour,
            'minute': now.minute,
            'limit': limit
        }
        url = URL.format(**ctx)
        return BeautifulSoup(requests.get(url).content, 'html.parser')


    # #@click.group()
    # def main():
    #     pass


    #@main.command()
    #@click.argument('station_id')
    #@click.option('--direction', '-d', multiple=True,
    #              help="Filter departures by those in a certain direction")
    def scrape(self,station_id, direction):
        direction = [d.lower() for d in direction]
        soup = self.search(station_id)
        result = []
        out_put =""
        for departure in soup.find_all('itddeparture'):
            if direction and departure.itdservingline['direction'].lower() not in direction:
                continue
                
            if departure.itdrtdatetime:
                # Real-time data
                dt = datetime(int(departure.itdrtdatetime.itddate['year']),
                            int(departure.itdrtdatetime.itddate['month']),
                            int(departure.itdrtdatetime.itddate['day']),
                            int(departure.itdrtdatetime.itdtime['hour']),
                            int(departure.itdrtdatetime.itdtime['minute']))

                connection_name = departure.itdservingline['number']
            elif departure.itddatetime:
                # Scheduled data
                dt = datetime(int(departure.itddatetime.itddate['year']),
                            int(departure.itddatetime.itddate['month']),
                            int(departure.itddatetime.itddate['day']),
                            int(departure.itddatetime.itdtime['hour']),
                            int(departure.itddatetime.itdtime['minute']))
                connection_name = departure.itdservingline['number']
            else:
                # Scheduled connection was cancelled
                continue
            out_put +="{\"time\":\""+str (dt.strftime(TIME_FORMAT)[11:16])+"\"," +"\"transport\":\""+str (connection_name)+"\"," +"\"direction\":\""+str (departure.itdservingline['direction'].lower())+"\"},"     
        #print(json.dumps(result))
        return ("["+out_put[:-1]+"]")


    #@main.command()
    #@click.argument('station_id')
    def list_directions(self,station_id):
        soup = search(station_id, limit=1000)
        directions = set()
        for departure in soup.find_all('itddeparture'):
            directions.add(departure.itdservingline['direction'])
        for direction in sorted(list(directions)):
            #click.echo(direction)
            print (direction)


    # @main.command()
    # @click.argument('file', type=click.File('r'))
    # @click.option('--format', '-f', help="Format string for datetimes")
    # @click.option('--limit', '-l', type=int, default=3,
    #               help="Limit the number of departure times displayed")
    def display(self,file, format, limit):
        now = _now()
        departures = [datetime.strptime(d, TIME_FORMAT).replace(tzinfo=TIMEZONE) for d in json.load(file)]
        departures = [d for d in departures if d > now][:limit]
        if not departures:
            print("Scrape required!")

        if format:
            print(', '.join([d.strftime(format) for d in departures]))
        else:
            deltas = [str(int((d - now).seconds / 60)) for d in departures]
            print("In {} min".format(', '.join(deltas)))


#list_directions('5006157')
#t = Connections()
#print (t.scrape('5006157',["Backnang","Bietigheim-Bissingen"]))

