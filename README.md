# TwitterExtractData
Twitterconf.py will start flume and store data into HDFS,
Twitter.py will monitor hdfs folder and trigger the PIG file whenever twitter's data file cretaed in HDFS,
Tweet.pig will load the DATA from HDFS file,Extract the necessary parameter and store back into HDFS
