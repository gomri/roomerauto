import mysql.connector
import re

conn = mysql.connector.connect(user='admin', password='Roomerhasit1',
                               port='14642',
                               host='qa-db.chwkxuugo66h.us-east-1.rds.amazonaws.com',
                               database='roomer')

my_cursor = conn.cursor()
# my_cursor.execute('''
# select email, api_token, rate_plan_id
# from roomer.partners
# where email like '%trivago%'
# or email like '%kayak%'
# or email like '%skyscanner%'
# ''')
# f = my_cursor.fetchall()
# print f[0][0]
# conn.close()