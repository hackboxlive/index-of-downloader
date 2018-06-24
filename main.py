# do imports
import os
from bs4 import BeautifulSoup
from urllib.request import urlopen

download_queue = []


def get_links(url, parent_url, file_location):
	if(url.endswith('/')):	#that means it is a folder
		#print('here')
		try:
			html = urlopen(url).read()
			soup = BeautifulSoup(html, 'html.parser')
			for link in soup.find_all('a'):
				print(parent_url + link.get('href'))
			#call again over the gathered links
		except:
			print('Error raised. Could not open the url. You are on your own buddy!!')
	else:
		#append this link into the download queue
		download_queue.append(tuple((url,file_location)))


def download(url, location):
	command = 'wget ' + url + ' O ' + location
	os.system(command)


print('Enter the base url that you want to scrape')
url = input()

print('Enter the base location to save')
location = input()

get_links(url, url, location)	#get all the links from the base url

print('All links crawled, starting download now')

#download(url, '~/try')


