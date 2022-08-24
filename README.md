# Astrafy THC - Data Engineer

## Part 2: Coding Challenge

As part of the coding-challenge requirements, the data mart architecture was developed in Google Cloud using Google BigQuery, Scheduled Cloud Functions and Google Data Studio for visualizations.

The data is comprised of taxi trips records from the city of Chicago from 2022-01-01 to 2022-06-30, and weather data of the weather station "KORD" in Chicago from 2022-01-01 onwards.

Both datasets are open source and can be accessed from https://console.cloud.google.com/marketplace/details/city-of-chicago-public-data/chicago-taxi-trips and https://www.ncei.noaa.gov/cdo-web/search?datasetid=GHCND respectively.

### Scripts

> weather_bigquery.py

Python script used to feed the Google BigQuery data table of chicago_weather with past weather data.

> ingest_weather_cloud_function.py

Python script used to ingest new weather data from the weather station "KORD" in Chicago on a periodic basis with a scheduled cloud function.

> chicago_taxi_trips_filter.sql

SQL script used to filter Google BigQuery dataset of Chicago taxi trips.

> join_tables.sql

SQL script used to join Chicago weather data and taxi trips data to produce a data studio.

### Data Studio

The data studio dashboard of the Chicago trips and weather data can be found at:

https://datastudio.google.com/s/v9lO5Klr-pU
