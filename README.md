# coen-assign2

MapReduce


'''
bin/hadoop jar /usr/local/Cellar/hadoop/2.8.2/libexec/share/hadoop/tools/lib/hadoop-streaming-2.8.2.jar -D mapred.map.tasks=10 -D mapred.reduce.tasks=10 \
-file /Users/chongli/Github/coen-assign2/test_mapper.py  -mapper /Users/chongli/Github/coen-assign2/test_mapper.py \
-file /Users/chongli/Github/coen-assign2/test_reducer.py -reducer /Users/chongli/Github/coen-assign2/test_reducer.py \
-input /input/nms_airborne_radioactivity_ssn_radioactivite_dans_air.csv  -output /output/
'''

'''
hdfs dfs -ls /
'''

'''
hdfs dfs -ls /output
'''

'''
hdfs dfs -cat /output/part-00000
'''

delete output folder
'''
hdfs dfs -rm -r -f /output
'''

logs are recorded in mapper.log and reducer.log , which under this path:
/usr/local/Cellar/hadoop/2.8.2

