import requests
import json
from datetime import datetime, timedelta
from google.cloud import bigquery

def ingest_weather(request):
    """Ingest Chicago City yesterday's weather to Google Bigquery
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        Void function
    """
    yesterday_date = datetime.now() - timedelta(days=1)
    start_date = yesterday_date.strftime("%Y-%m-%dT00:00:01Z") #start date to fetch weather data since
    end_date = yesterday_date.strftime("%Y-%m-%dT23:59:59Z") #end date to fetch weather data to
    station_id = "KORD"

    url = 'https://api.weather.gov/stations/{}/observations?start={}&end={}'.format(station_id,start_date,end_date)
    
    try:
        r = requests.get(url)
    except requests.exceptions.RequestException as e:  # API error
        return str(e)

    data = json.loads(r.content) #jsonify API output
    temps = [feature["properties"]["temperature"]["value"] 
            for feature in data["features"] if feature["properties"]["temperature"]["value"] is not None] #filter out None

    def to_farenheit(celsius):
        return (celsius * 9/5) + 32

    date_dt = yesterday_date.strftime("%Y-%m-%d")
    tmax = round(to_farenheit(max(temps)))
    tmin = round(to_farenheit(min(temps)))
    tavg = round((tmax+tmin)/2)

    client = bigquery.Client()
    table_id = "astrafy-bq.chicago_bq.chicago_weather"
    row_to_insert = [{u'date':date_dt, u'tmax':tmax, u'tmin':tmin, u'tavg':tavg}]
    errors = client.insert_rows_json(table_id, row_to_insert)

    if errors == []:
        print("New rows have been added.")
    else:
        return "Encountered errors while inserting rows: {}".format(errors)

    request_json = request.get_json()
    if request.args and 'message' in request.args:
        return request.args.get('message')
    elif request_json and 'message' in request_json:
        return request_json['message']
    else:
        return f'Success!'