# -*- coding: utf-8 -*-
__author__ = 'Lvv'

import os
import sys
import conf.settings as settings
import pymysql
from DBUtils.PooledDB import PooledDB
from ESPool import ESPool


# POOLS_DIRECTORY = os.path.join(settings.SPARK_STREAMING_BASE_PROJECT_DIRECTORY,
#                                'DataPlatform/lib/pools')
# if POOLS_DIRECTORY not in sys.path:
#     sys.path.append(POOLS_DIRECTORY)



MYSQLPOOL = PooledDB(MySQLdb,
                     mincached=settings.MYSQL_POOL_MINSIZE,
                     maxconnections=settings.MYSQL_POOL_MAXSIZE,
                     blocking=True,
                     host=settings.MYSQL_HOST,
                     port=settings.MYSQL_PORT,
                     user=settings.MYSQL_USER,
                     passwd=settings.MYSQL_PASSWD,
                     db=settings.MYSQL_DB,
                     charset='utf8')

MYSQLPOOL_BIZ = PooledDB(MySQLdb,
                     mincached=settings.MYSQL_POOL_MINSIZE,
                     maxconnections=settings.MYSQL_POOL_MAXSIZE,
                     blocking=True,
                     host=settings.MYSQL_HOST_BIZ,
                     port=settings.MYSQL_PORT_BIZ,
                     user=settings.MYSQL_USER_BIZ,
                     passwd=settings.MYSQL_PASSWD_BIZ,
                     db=settings.MYSQL_DB_BIZ,
                     charset='utf8')

ESPOOL = ESPool(settings.ES_HOST, settings.ES_PORT, 0, maxsize=3)

