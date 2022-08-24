import csv
import datetime
from google.cloud import bigquery

#Past weather of Chicago was obtained in CSV format from https://www.ncei.noaa.gov/ and https://www.weather.gov/

client = bigquery.Client.from_service_account_json('astrafy-bq-e833593c704a.json593c704a.json') #Google Bigquery oauth
table_id = "astrafy-bq.chicago_bq.chicago_weather"
rows_to_insert = []

with open('../data/chicago_weather.csv', newline='') as csvfile:
    weather = csv.reader(csvfile, delimiter=',', quotechar='"')
    header = next(weather)
    for row in weather:
        w_date, tmax, tmin  = row[5:]
        date_dt = datetime.datetime.strptime(w_date, "%d/%m/%Y").strftime("%Y-%m-%d")
        rows_to_insert.append({u'date':date_dt, u'tmax':tmax, u'tmin':tmin, u'tavg':round((float(tmax)+float(tmin))/2)})
rows_to_insert

errors = client.insert_rows_json(table_id, rows_to_insert)
if errors == []:
    print("New rows have been added.")
else:
    print("Encountered errors while inserting rows: {}".format(errors))
