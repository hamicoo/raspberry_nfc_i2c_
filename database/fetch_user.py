import psycopg2.extras
import time
import datetime
#import logger
#import send_message_module
#import bcrypt
import sys
sys.path.insert(0,'./logger')
#import logger





ts = time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')


def fetch_balance(tag_id):
    print("tag_id= " + tag_id)
    try:
        conn = psycopg2.connect("dbname='postgres' user='pi' password='123'")
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        #logger.txt_logger(1, 'Database >fetch_user > successfully connected to postgres')
    except:
        print("Err")
        #logger.txt_logger(-1, 'Database >fetch_user > Probelm With Connection To postgres')

    cur.execute("""SELECT owner_name,balance FROM subway_ticket.users_card where tag_id='%s' """ % (tag_id))
    records = cur.fetchall()


    if len(records)!=0:
        return True,records[0]
    elif len(records)==0:
        records=['','']
        return False,records




