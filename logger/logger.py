import datetime
import time
from pymongo import MongoClient
#from cassandra.cluster import Cluster



#curren time
ts=time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')





def txt_logger(d_type,txt_log,mongo_log=False,file_log=True):
# CASSANDRA DB LOGGIN PROCEDURE

        #try:
            #if cassandra_log:
            #    print('hi')
            #    # * cassandra Configuration
            #    cluster = Cluster()
            #    session = cluster.connect('TEST')
                # * cassandra Configuration
            #    if d_type == -1:
            #        rows = session.execute("""INSERT INTO log_table(id,type, description,log_time) VALUES (now(),%s,%s,%s)""",('Error',txt_log,st))
            #    elif d_type==1:
            #        rows = session.execute("""INSERT INTO log_table(id,type, description,log_time) VALUES (now(),%s,%s,%s)""",('Info', txt_log, st))
        #except  :
         #   print('except')
        #    print ('Error : Cant Connect To Cassandra File For Logging')


#MONGO DB LOGGIN PROCEDURE
        try:

            if mongo_log:
                # mongodb connection
                mongo = MongoClient()
                client = MongoClient('localhost', 27017)
                db = client['sys_logg_col']
                collection = db['sys_logg_col']
                # mongo db connection
                if d_type==-1:
                    post = {"Type": "Error ","Description":txt_log,"log_time":st}
                    posts = db.sys_logg_col
                    post_id = posts.insert_one(post).inserted_id
                elif d_type==1:
                    post = {"Type": "Info ", "Description": txt_log, "log_time": st}
                    posts = db.sys_logg_col
                    post_id = posts.insert_one(post).inserted_id
        except  :
            print ('Error : Cant Connect To Mongodb File For Logging')


# FILIE LOGGIN PROCEDURE
        try:

            if file_log:
                log_file = open('output.txt', 'a+')
                if d_type == -1:
                    s='Error - ' + str(datetime.datetime.now()) + ' (Description: ' + txt_log +')'
                    print(s ,file=log_file)
                elif d_type==1:
                    s = 'Info - ' + str(datetime.datetime.now()) + ' (Description: ' + txt_log + ')'
                    print(s, file=log_file)
        except  :
            print ('Error : Cant Connect To text File For Logging')




