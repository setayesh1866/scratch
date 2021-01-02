import requests 

url = "https://www.filimo.com/m/9905"

data = requests.get(url+str(i))
soup = BeautifulSoup(data.text, "html.parser")
p_tags = soup.find_all('p', class_ = "serial-desc")
for p_tag in p_tag:
    print (p_tag.text)