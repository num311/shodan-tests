import shodan
import pandas
import time
from optparse import OptionParser
import sys
import logging

logging.basicConfig(level=logging.DEBUG)

api = shodan.Shodan('xxxxxxxxxxxxxxxxxxxxxxx')


parser = OptionParser()
parser.add_option ("-f","--file",action="store", dest="redes", help="csv or txt with network list")
parser.add_option("-p","--port",action="store",dest="puerto",type="int", help="port to be tested")

(options,args) = parser.parse_args()

if options.redes is None or options.puerto is None:
	parser.error("Usage: shodan_test.py -f file -p port")

port=str(options.puerto)


try:
	df1=pandas.read_csv(options.redes)
except FileNotFoundError:
	logging.debug("The file specified with the argument -f or --file could not be found")
	sys.exit(2)
   


for row in df1.values:
        time.sleep(1)
        logging.debug ("network: "+str(row[0]))
        resultado=(api.search('net:'+str(row[0])+' port:'+ port ))
        print ("Number of ips with port "+ port +" open: "+str(resultado['total']))
        print()
        for res in resultado['matches']:
                print (res['ip_str']+' '+str(res['port'])+' '+str(res['hostnames']))

