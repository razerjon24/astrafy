SELECT * FROM `astrafy-bq.chicago_bq.chicago_weather` AS dbw RIGHT JOIN  
(SELECT EXTRACT(DATE FROM trip_start_timestamp) AS date_format,
        COUNT(*) as trips_nums,
        SUM(trip_seconds) AS trips_duration,
        SUM(fare) AS trips_fare,
        SUM(extras) AS trips_extras
FROM  `astrafy-bq.chicago_bq.chicago_taxi_trips`
GROUP BY date_format) dbt ON dbw.date = dbt.date_format ORDER BY dbw.date;