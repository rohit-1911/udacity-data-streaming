Question 1 - How did changing values on the SparkSession property parameters affect the throughput and latency of the data?
Answer - Changing different config values impacted processedRowsPerSecond and inputRowsPerSecond. Changes to the values resulted in increased throughput.

Question 2 - What were the 2-3 most efficient SparkSession property key/value pairs? Through testing multiple variations on values, how can you tell these were the most optimal?
Answer - With maxOffsetsPerTrigger as 1000 and maxRatePerPartition as 500, I got a throughput of around 20 processedRowsPerSecond, however, after trying around different values for maxOffsetPerTrigger, I got a good throughput of 81 records processed per seconds with maxOffsetPerTrigger as 2000.

There were a couple more configurations which I tried to include and modify to increase the throughput and performance but only maxRatePerPartition affected it positively

1. maxRatePerPartition
2. spark.sql.shuffle.partitions
