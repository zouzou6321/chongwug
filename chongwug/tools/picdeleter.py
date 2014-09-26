import MySQLdb,os,datetime
if 'SERVER_SOFTWARE' in os.environ:
   MYSQL_HOST = 'chongwug.mysql.rds.aliyuncs.com'
   MYSQL_PORT = 3306
   MYSQL_USER = 'chongwug'
   MYSQL_PASS = 'weet6321'
   MYSQL_DB   = 'chongwug'
else:
   # Make `python manage.py syncdb` works happy!
   MYSQL_HOST = 'localhost'
   MYSQL_PORT = 3306
   MYSQL_USER = 'root'
   MYSQL_PASS = ''
   MYSQL_DB   = 'app_haidaoteam'
conn = MySQLdb.connect(host=MYSQL_HOST,user=MYSQL_USER,passwd=MYSQL_PASS,db=MYSQL_DB,port=MYSQL_PORT)
cur = conn.cursor()
cur.execute('select fname, monitor_time from manager_tmppic_monitor where dele=0')
for name, monitor_time in cur.fetchall():
    time = datetime.datetime.now() - monitor_time
    if time.total_seconds() > 300:
        try:
            #os.remove(name)
            sql = "update manager_tmppic_monitor set dele = 1 where fname ='" + name + "'"
            cur.execute(sql)
            conn.commit()
        except:
            None
conn.close()