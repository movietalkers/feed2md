import xmltodict
import time
import os

FILE_PATH = "sample_data/rssdemo.xml"
OUT_DIR= "out\\"

def dir_from_date(path):
	try:
		os.makedirs(path)
	except OSError:
		print ("Creation of the directory %s failed" % path)
	else:
		print ("Successfully created the directory %s" % path)

def make_front_metter(item2, formated):
	# ---
	# title: "Bold Mage"
	# cover: "https://unsplash.it/1280/500/?random?BoldMage"
	# author: "guinevere"
	# date: "2017-01-01"
	# category: "tech"
	# tags:
	#     - programming
	#     - stuff
	#     - other
	# ---
	return "---\ntitle: \"{0}\"\ncover: \"{1}\"\nauthor: \"guinevere\"\ndate: \"{2}\"\n---".format(
		item['title'],
		item['itunes:image']['@href'],
		formated)



with open(FILE_PATH,'r',50,"utf8") as fd13:
	doc = xmltodict.parse(fd13.read())
	items = doc['rss']['channel']['item']
	for item in items:
		creationDate = time.strptime(item['pubDate'],'%a, %d %b %Y %H:%M:%S +0300')

		# Post folder
		formated = "{0}-{1:02d}-{2:02d}".format(creationDate.tm_year, creationDate.tm_mon, creationDate.tm_mday)
		dir_from_date("{1}{0}".format(formated, OUT_DIR))

		# front metter
		front_metter = make_front_metter(item, formated)

		file = open(“index.md”,”w”) 
		
		file.write(front_metter) 
		file.write(“\n”) 
		file.write(item["description"]) 
		file.close() 