import shodan
import pandas
import time
from optparse import OptionParser
import sys

api= shodan.Shodan('xxxxxxxxxxxxxxxxxxxxxxxxxxxxx')


parser = OptionParser()
parser.add_option ("-f","--file",action="store", dest="redes", help="csv or txt with network list")
parser.add_option("-p","--port",action="store",dest="puerto",type="int", help="port to be tested")

(options,args) = parser.parse_args()

if options.redes == None or options.puerto == None:
	parser.error("Usage: shodan_test.py -f file -p port")

port=str(options.puerto)


try:
	df1=pandas.read_csv(options.redes)
except FileNotFoundError:
	print ("The file specified with the argument -f or --file could not be found")
	sys.exit(2)
   


for row in df1.values:
        time.sleep(1)
        print ("Red: "+str(row[0]))
        resultado=(api.search('net:'+str(row[0])+' port:'+ port ))
        print ("Numero de ips con puerto "+ port +" abierto: "+str(resultado['total']))
        print()
        for res in resultado['matches']:
                print (res['ip_str']+' '+str(res['port'])+' '+str(res['hostnames']))

