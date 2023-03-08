import os
import requests
import json
from datetime import date, timedelta

def getYesterdaysDate():
    today = date.today()
    yesterday = today - timedelta(days = 1)
    return str(yesterday)+"T00:00:00Z", str(yesterday)+"T23:59:59Z"

def getUrl(variableId):
    return f"https://api.fingrid.fi/v1/variable/{variableId}/events/json?"

def saveJSON(req,savename):
    data = req.json()
    with open(f'{savename}.json', 'w') as f:
        json.dump(data, f) 

def runner():
    electrictyConsumption = getUrl(str(124))
    electrictyByWind = getUrl(str(75))
    
    start, end = getYesterdaysDate()

    electrictyConsumption = getUrl(str(124))
    electrictyByWind = getUrl(str(75))
    
    start, end = getYesterdaysDate()

    headers = {'x-api-key':apiKey}
    params = {'start_time':start,"end_time":end}

    r = requests.get(electrictyConsumption,headers=headers,params=params,)
    saveJSON(r,"consumption")
    r = requests.get(electrictyByWind,headers=headers,params=params,)
    saveJSON(r,"wind")

if __name__ == '__main__':

    apiKey = os.environ['FINGRID_API_KEY']

    runner()


