import requests 

url = "https://bama.ir/car/peykan/all-models/all-trims?page=1"

data = requests.get(url+str(i))
soup = BeautifulSoup(data.text, "html.parser")
p_tags = soup.find_all('p', class_ = "shortdesc removeEmoji")
for p_tag in p_tag:
    print (p_tag.text)