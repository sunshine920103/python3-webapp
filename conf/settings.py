# -*- coding: utf-8 -*-
__author__ = 'cc'


# is use checkpoint
USE_CHECKPOINT = False

# app name
SPARK_STREAMING_NAME = 'dp-handler-tag-20170627'

# kafka consumer topic
SPARK_STREAMING_TOPIC = 'bbd_queue_norm_for_tag_20170627'
# group id
SPARK_STREAMING_GROUP = 'dp-group-tag-20170630aaa'
# spark streaming receiver maxRate
SPARK_STREAMING_RECEIVER_MAXRATE = 500
# time interval
SPARK_STREAMING_INTERVAL = 10
# the number of partitions on a topic
SPARK_STREAMING_PARTITIONS = 1
# numPartitions
SPARK_STREAMING_NUM_PARTITIONS = 50
# zookeeper address
SPARK_STREAMING_HOSTS = 'kafka1.prod.bbdops.com:2181,kafka2.prod.bbdops.com:2181,kafka3.prod.bbdops.com:2181,kafka4.prod.bbdops.com:2181,kafka5.prod.bbdops.com:2181/kafka'
# checkpoint base directory
SPARK_STREAMING_BASE_CHECKPOINT_DIRECTORY = '/user/bbddataom/checkpoint/tag'
SPARK_STREAMING_MINSIZE = 30
SPARK_STREAMING_MAXSIZE = 60
# project base directory
SPARK_STREAMING_BASE_PROJECT_DIRECTORY = '/'

SPARK_STREAMING_TOPIC_INDEX = ""

# mysql pool minsize
MYSQL_POOL_MINSIZE = 1
# mysql pool maxsize
MYSQL_POOL_MAXSIZE = 50
# mysql host
MYSQL_HOST = '192.168.81.233'
# mysql port
MYSQL_PORT = 53306
# mysql user
MYSQL_USER = 'root'
# mysql passed
MYSQL_PASSWD = 'Bbders@bbdops#@!123'
# mysql dbname
MYSQL_DB = 'ra_two'

# biz mysql host
MYSQL_HOST_BIZ = 'dataapi.mysql.bbdops.com'
# biz mysql port
MYSQL_PORT_BIZ = 53606
# biz mysql user
MYSQL_USER_BIZ = 'dp_biz'
# biz mysql passed
MYSQL_PASSWD_BIZ = 'MM4bN6JJwcz7zXCvq2NQ'
# biz mysql dbname
MYSQL_DB_BIZ = 'bbd_dp_biz'

# elasticsearch
ES_HOST = "10.28.100.30"
ES_PORT = 39202
INDEX = 'search_20170622'
TABLE = 'qyxx'
