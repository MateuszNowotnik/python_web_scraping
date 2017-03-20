import requests
from bs4 import BeautifulSoup
import pyperclip


url = "http://www.torrenttrackerlist.com/torrent-tracker-list/"
r = requests.get(url)

soup = BeautifulSoup(r.content, "html.parser")

g_data = soup.find_all("pre", {"class": "prettyprint"})

for item in g_data:
	pyperclip.copy(item.text)
