from bs4 import BeautifulSoup
import requests
import lxml  
import os
import urllib


def mkdir(directory):
	if not os.path.exists(directory):
		os.makedirs(directory)


if __name__ == '__main__':

	mkdir('./output') #make output directory if not already made
	output_dir = os.path.join(os.path.dirname(__file__), 'output')

	first_source = requests.get('https://xkcd.com/archive/').text
	first_soup = BeautifulSoup(first_source, 'lxml')
	divs = first_soup.find_all('div', attrs={'class' : 'box'})
	for div in divs:
		if div.attrs['id']=='middleContainer':
			for link in div.find_all('a'):
				if link.has_attr('href'):
					image_number = link.attrs['href']
					temp_link = 'https://xkcd.com' + image_number
					
					second_source = requests.get(temp_link).text
					second_soup = BeautifulSoup(second_source, 'lxml')
					''' get image_name '''
					for img_div in second_soup.find_all('div'):
						if img_div.has_attr('id'):
							if img_div.attrs['id'] == 'ctitle':
								image_name = img_div.text
								image_name = image_name + '.png'
								break
					'''download and save as image_name '''
					for img_div in second_soup.find_all('div'):
						if img_div.has_attr('id'):
							if img_div.attrs['id'] == 'comic':
								for img_src in img_div.find_all('img'):
									if img_src.has_attr('src'):
										image_link = 'https:'
										image_link =image_link + img_src.attrs['src']
										output_path = output_dir+'/'+image_name
										with open(output_path, 'wb') as output_img:
											output_img.write(urllib.urlopen(image_link).read())
											output_img.close()
