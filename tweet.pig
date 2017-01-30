REGISTER /usr/local/pig/lib/json-simple-1.1.jar;
REGISTER /usr/local/pig/lib/elephant-bird-core-4.1.jar;
REGISTER /usr/local/pig/lib/elephant-bird-pig-4.1.jar;
REGISTER /usr/local/pig/lib/elephant-bird-hadoop-compat-4.1.jar;
tweets = LOAD '$file' USING com.twitter.elephantbird.pig.load.JsonLoader('-nestedLoad') as (json:map[]);
user_details = FOREACH tweets GENERATE json#'text',json#'timestamp_ms',json#'id',json#'lang';
dump user_details;
STORE user_details INTO 'hdfs://localhost:9000/twitter_pigoutput/$file/' USING PigStorage (',');