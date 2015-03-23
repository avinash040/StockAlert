__author__ = 'avi'

#Input the stock name from the user
#Input the target value from the user
#Sanity Check the values entered
#Put the values entered into a dictionary database


#Create a polling function for alerts
#Create an alert mechanism using email/sms/whatever

import sys
import ystockquote
import pprint
import time
import threading

## TODO - DATABASE stuff
import sqlite3
conn = sqlite3.connect('stocks.db')
c = conn.cursor()
c.execute('')
conn.commit()
conn.close()


class StockPollingThread(threading.Thread):
    def __init__(self, threadID, name, target_value, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.target_value = target_value

    def run(self):
        print "Starting Polling"
        stock_polling(self.name, self.target_value)
        print "exiting polling"


def stock_polling(stock_name,target_value):
    while float(ystockquote.get_price(stock_name)) <= float(target_value):
        print "stock value not reached" + ystockquote.get_price(stock_name)
        time.sleep(60)
    print "yay - stock value at " + ystockquote.get_price(stock_name)



stock_name = raw_input('Enter the stock name: ')
stock_target = raw_input ('Enter the stock target price: ')
#email = raw_input('Enter your email address')

#stock_name = "AAPL"
#stock_target = "25"
print stock_name, stock_target

pprint.pprint(ystockquote.get_all(stock_name))
thread1 = StockPollingThread(1,stock_name,stock_target,1)
thread1.start()

sys.exit()
