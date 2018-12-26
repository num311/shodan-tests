import shodan
import pandas
import time
from optparse import OptionParser
import sys
import logging

logging.basicConfig(level=logging.DEBUG)

parser = OptionParser()
parser.add_option("-f", "--file", action="store", dest="redes", help="csv or txt with network list")
parser.add_option("-p", "--port", action="store", dest="puerto", type="int", help="port to be tested")
parser.add_option("-l", "--loglevel", action="store", dest="debugLevel", help="Set the verbosity of the logs")
parser.add_option("-a", "--apikey", action="store", dest="apikey", help="")

(options, args) = parser.parse_args()

if options.redes is None or options.puerto is None or options.apikey is None:
    parser.error("Usage: shodan_test.py -a apikey -f file -p port -l loglevel (DEBUG, INFO, WARNING, ERROR)")

# We extract the port from the parameters

port = str(options.puerto)

# Then we get the api key

api = shodan.Shodan(options.apikey)

# Then we try to read the file with the different networks

try:
    df1 = pandas.read_csv(options.redes)
except FileNotFoundError:
    logging.debug("The file specified with the argument -f or --file could not be found")
    sys.exit(2)

# If all parameters are correct, we throw the request to Shodan using our api key

for row in df1.values:
    time.sleep(1)
    logging.debug("Network: " + str(row[0]))
    resultado = (api.search('net:' + str(row[0]) + ' port:' + port))
    print("Number of ips with port " + port + " open: " + str(resultado['total']))
    print()
    for res in resultado['matches']:
        print(res['ip_str'] + ' ' + str(res['port']) + ' ' + str(res['hostnames']))
