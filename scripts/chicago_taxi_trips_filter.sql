CREATE TABLE `chicago_bq.chicago_taxi_trips`
PARTITION BY TIMESTAMP_TRUNC(trip_start_timestamp, DAY)
OPTIONS (require_partition_filter = TRUE)
AS (SELECT * FROM `bigquery-public-data.chicago_taxi_trips.taxi_trips` 
WHERE trip_start_timestamp BETWEEN TIMESTAMP('2022-01-01') AND TIMESTAMP('2022-06-30'));
