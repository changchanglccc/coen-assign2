# coen-assign2

MapReduce


```bash
bin/hadoop jar /usr/local/Cellar/hadoop/2.8.2/libexec/share/hadoop/tools/lib/hadoop-streaming-2.8.2.jar -D mapred.map.tasks=10 -D mapred.reduce.tasks=10 \
-file /Users/chongli/Github/coen-assign2/test_mapper.py  -mapper /Users/chongli/Github/coen-assign2/test_mapper.py \
-file /Users/chongli/Github/coen-assign2/test_reducer.py -reducer /Users/chongli/Github/coen-assign2/test_reducer.py \
-input /input/nms_airborne_radioactivity_ssn_radioactivite_dans_air.csv  -output /output/
```

```bash
hdfs dfs -ls /
```

```bash
hdfs dfs -ls /output
```

```bash
hdfs dfs -cat /output/part-00000
```

delete output folder
```bash
hdfs dfs -rm -r -f /output
```

logs are recorded in mapper.log and reducer.log , which under this path:
/usr/local/Cellar/hadoop/2.8.2

add useful link:
1. http://icejoywoo.github.io/2015/09/28/introduction-to-hadoop-streaming.html
2. https://python.freelycode.com/contribution/detail/307
3. http://blog.csdn.net/chosen0ne/article/details/7319306
