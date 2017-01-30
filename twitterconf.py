import subprocess

keywords = raw_input()
nameoffolder = keywords.replace(',','')
file_content = open('/usr/local/flume/conf/flume-twitter.conf').readlines()

file_content[13] = 'TwitterAgent.sources.Twitter.keywords = '+keywords+'\n'
file_content[17] = 'TwitterAgent.sinks.HDFS.hdfs.path = hdfs://localhost:9000/flume/'+nameoffolder+'\n'
open('/usr/local/flume/conf/flume-twitter.conf','w').writelines(file_content)

command = 'flume-ng agent -n TwitterAgent --conf ./conf/ -f /usr/local/flume/conf/flume-twitter.conf -Dflume.root.logger=DEBUG,console'
command = command.split(' ')
subprocess.call(command)
subprocess.call(['ls','-la'])
