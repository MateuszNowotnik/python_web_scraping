import requests
from bs4 import BeautifulSoup


url = "http://www.imdb.com/chart/moviemeter?ref_=nv_mv_mpm_8"
r = requests.get(url)

soup = BeautifulSoup(r.content, "html.parser")

tb_data = soup.find("tbody", {"class": "lister-list"})

title_data = tb_data.find_all("td", {"class": "titleColumn"})

rating_data = tb_data.find_all("td", {"class": "ratingColumn imdbRating"})


for i, item in enumerate(title_data, start=1):
	#title
	print(i, end="")
	print(". " + item.contents[1].text)


#	for rItem in rating_data:
#		#rating
#		if(rItem.find("strong") == None):
#			print("  _None")
#		else:
#			print("  _" + rItem.contents[1].text)