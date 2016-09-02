import os
from flask import Flask

application = Flask(__name__)

@application.route("/aaaa")
def hello():
    return "<br><br><br><br><br><br><br><br><br><br><h1><marquee><b>Hello world From Mj!</b>"
from flask import Flask,request
#from boto.dynamodb2.table import Table
from flask import Flask,render_template
##from flask import Markup
#import MySQLdb
import jinja2
import os
#import boto

#import csv
from datetime import datetime
import random
#import memcache
import sys
from time import sleep


application = Flask(__name__)


@application.route('/back',methods= ['GET', 'POST'])
# Configure the Jinja2 environment.
def main4():
    return render_template('query.html',
                           title='MAIN',
                           user='mj')


@application.route('/input',methods= ['GET', 'POST'])
# Configure the Jinja2 environment.
def main2():
    user = {'nickname': 'Miguel'}  # fake user
    return render_template('mayank.html',
                           title='MAIN',
                           user=mj1)

@application.route('/sign', methods= ['GET', 'POST'])
# Configure the Jinja2 environment.
def main1():
    my_res=[]
    magn=request.form['mag']
    loc=str(request.form['loc'])


    ## Relational DB Code
    if len(magn)==0:
        magn=None
    if len(loc)==0:
        loc=None
    '''
    print "fetching records from My SQL"
    db = MySQLdb.connect(host='mayank-db-instance.czvgwfu3umqu.us-west-2.rds.amazonaws.com', port=3306, db='mayank_database', user='mayank', passwd='mayank123')
    cursor = db.cursor()
    cursor.execute('select place,mag,id type from all_month_data where mag=%s OR place like"%%" %s "%%" order by mag limit 5',(2,loc))
    ##
    my_res = [];
    for row in cursor.fetchall():
            my_res.append(dict([('loc',row[0]),
                                 ('mag',row[1]),
                                 ('id',row[2])
                                 ]))

    '''
    ##Dynamo Db Conn
    '''
    dyn=boto.dynamodb2.connect_to_region('us-west-2',aws_access_key_id ='AKIAJP5BQGMU42V7FGYQ',aws_secret_access_key='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')
    tab=Table('all_month_data',connection=dyn)
    start_time = datetime.now()

    res= tab.scan(mag__eq=magn)
    sleep(2)
    end_time = datetime.now()
    print "fetching the results from Dynamo Db"
    final_time=format(end_time - start_time)
    '''
    final_time=20
    #my_res="mj"
    my_res.append(dict([('mag','20'),
                            ('loc','Arlington'),
                            ('id','1')
                            ]))
    print final_time
    '''for row in res:
 #       my_res.append(dict['(mag', res['mag'])])
        my_res.append(dict([('mag',row['mag']),
                            ('loc',row['place']),
                            ('id',row['id'])
                            ]))
    '''
    return render_template('results.html',
                           title='results',
                           my_res=my_res, final_time=str(final_time))


    #user = {'nickname': 'Miguel'}  # fake user


@application.route('/')
# Configure the Jinja2 environment.
def main3():
    user = {'nickname': 'Miguel'}  # fake user
    mj1=['MJ','Jain','PJ']
    return render_template('query.html',
                           title='Home',
                           user=mj1)
# add a rule for the index page.
application.add_url_rule('/', 'index', (lambda: 'Hello From Mayank updated2'))

if __name__ == "__main__":
    #port = int(os.environ.get("port", 5001))
    #app.run(host='0.0.0.0', port=port)
    #app.debug = True
    application.run()
    #app.run()
