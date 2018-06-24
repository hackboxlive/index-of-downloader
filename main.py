# do imports
import os
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.parse import urljoin

download_queue = []


def get_links(url, parent_url, file_location):
	try:
		html = urlopen(url).read()
		soup = BeautifulSoup(html, 'html.parser')
		for link in soup.find_all('a'):
			#print(link.text)
			#print(parent_url + link.get('href'))
			if(link.text == '../'):
				continue
		
			link_name = urljoin(parent_url, link.get('href'))
			location_name = file_location + link.text

			if(link_name.endswith('/')):
				get_links(link_name, url, location_name)	#call again over the gathered links
			else:
				download_queue.append(tuple((link_name, file_location)))
	except:
		print('Error raised. Could not open the url. You are on your own buddy!!')


def download(url, location):
	command = 'wget ' + url + ' -P ' + location
	os.system(command)


print('Enter the base url that you want to scrape')
url = input()

print('Enter the base location to save')
location = input()

get_links(url, url, location)	#get all the links from the base url

print('All links crawled, starting download now')
#print(download_queue)
#for i in range(len(download_queue)):
	#print(download_queue[i][0] + '\t' + download_queue[i][1])

for i in range(len(download_queue)):
	download(download_queue[i][0], download_queue[i][1])

