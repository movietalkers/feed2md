import xmltodict
import time
import os

FILE_PATH = "sample_data/rssdemo.xml"
OUT_DIR= "out/{0}/"

def dir_from_date(path):
	try:
		print(path)
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

	episode_image = 'https://pbcdn1.podbean.com/imglogo/image-logo/1676116/r_My_Post_3_.jpg'
	if 'itunes:image' in item.keys():
		episode_image = item['itunes:image']['@href']
		

	return "---\ntitle: \"{0}\"\ncover: \"{1}\"\nauthor: \"guinevere\"\ndate: \"{2}\"\n---".format(
		item['title'],
		episode_image,
		formated)



with open(FILE_PATH,'r',50,"utf8") as fd13:
	doc = xmltodict.parse(fd13.read())
	items = doc['rss']['channel']['item']
	for item in items:
		creation_date = time.strptime(item['pubDate'],'%a, %d %b %Y %H:%M:%S +0300')

		# Post folder
		formated = '{0}-{1:02d}-{2:02d}'.format(creation_date.tm_year, creation_date.tm_mon, creation_date.tm_mday)
		full_path = OUT_DIR.format(formated)
		dir_from_date(full_path)

		# front metter
		front_metter = make_front_metter(item, formated)
		
		file = open('{0}/{1}'.format(full_path, 'index.md'),'w+') 
		file.write(front_metter) 
		file.write('\n') 
		if item["description"] is None:
			file.write(item["title"]) 
		else:
			file.write(item["description"]) 
		file.close() 