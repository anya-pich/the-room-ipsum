import requests
from bs4 import BeautifulSoup
import re

url = "https://medium.com/@DavidKlion/full-transcript-of-the-room-341e4286db8e"
results = requests.get(url)
soup = BeautifulSoup(results.text, "html.parser")

with open("transcript.txt", "w") as file:
	content = soup.article.find_all('p')
	for each in content:
		if each.find('em'):
			line = each.text
		else:
			line = re.search(r':\s(.+)$', each.text).group(1)
		file.write(line + "\n")
