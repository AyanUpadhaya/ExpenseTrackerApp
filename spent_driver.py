from docopt import docopt
from tabulate import tabulate
from spent import *

#docopt for creating api - pip install docopt if you dont have it
#pip install tabulate if you don't have it

#let build api

usage="""
Usage:
	spent_driver.py init
	spent_driver.py view [<view_category>]
	spent_driver.py <amount> <category> [<message>]
"""

args= docopt(usage)

if args['init']:
	init()
if args['view']:
	category=args['<view_category>']
	amount, result=view(category)

	print("Total amount: ",amount)
	print(tabulate(result))

if args['<amount>']:
	try:
		amount=float(args['<amount>'])
		log(amount,args['<category>'],args['<message>'])
	except Exception as e:
		print(e)

