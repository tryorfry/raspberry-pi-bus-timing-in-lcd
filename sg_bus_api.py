import os
import requests
import pytz
import dateutil.parser

BASE_EP = 'http://datamall2.mytransport.sg'

class DatamallApiClient(object):
    """ DataMall API Wrapper """
    def __init__(self):
        if 'DATAMALL_API_KEY' not in os.environ:
            raise Exception("DATAMALL_API_KEY key Environment variable is not set. DATAMALL_API_KEY is must for calling api.")
        
        self.api_key = os.environ['DATAMALL_API_KEY']
        self.base_ep = BASE_EP
        self.default_headers = {
            'AccountKey': self.api_key,
            'accept': 'application/json'
        }

    
    def iso_time_to_hhmm(self, iso):
        utctime = dateutil.parser.parse(iso)
        localtime = utctime.astimezone(pytz.timezone("Asia/Singapore"))

        return localtime.strftime('%H:%M')

    def bus_at_busstop_code(self, busstop_code):
        """ for a given busstop_code returns dict of bus_number and mapped to next 3 bus arrival timing list """
        
        res = requests.get(self.base_ep + '/ltaodataservice/BusArrivalv2', headers=self.default_headers, params={'BusStopCode': busstop_code})

        """
        API returns following DS
        {
            'odata.metadata': 'http://datamall2.mytransport.sg/ltaodataservice/$metadata#BusArrivalv2/@Element',
            'BusStopCode': '21459',
            'Services': [{
                'ServiceNo': '240',
                'Operator': 'SBST',
                'NextBus': {
                    'OriginCode': '22009',
                    'DestinationCode': '22009',
                    'EstimatedArrival': '2020-02-29T22:37:16+08:00',
                    'Latitude': '1.347945',
                    'Longitude': '103.71216466666667',
                    'VisitNumber': '1',
                    'Load': 'SEA',
                    'Feature': 'WAB',
                    'Type': 'SD'
                },
                'NextBus2': {
                    ...
                }
                'NextBus3': {
                    ...
                }
            }, ...]
        }
        """

        buses_info = {}
        if res.status_code == 200:
            for bus in res.json()['Services']:
                buses_info[bus['ServiceNo']] = []
                if bus['NextBus']['EstimatedArrival']:
                    buses_info[bus['ServiceNo']].append(self.iso_time_to_hhmm(bus['NextBus']['EstimatedArrival']))
                if bus['NextBus2']['EstimatedArrival']:                    
                    buses_info[bus['ServiceNo']].append(self.iso_time_to_hhmm(bus['NextBus2']['EstimatedArrival']))                    
                if bus['NextBus3']['EstimatedArrival']:                                        
                    buses_info[bus['ServiceNo']].append(self.iso_time_to_hhmm(bus['NextBus3']['EstimatedArrival']))

        # print(buses_info)
        return buses_info


if __name__ == '__main__':
    api = DatamallApiClient()
    print(api.bus_at_busstop_code(28019))
