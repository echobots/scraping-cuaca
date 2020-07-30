import requests
from bs4 import BeautifulSoup

page = requests.get('http://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Medan&AreaID=501580&Prov=34')
soup = BeautifulSoup(page.text, 'html.parser')
repo = soup.find(class_="row no-space-carousel-block")
repo_list = repo.find_all(class_='col-md-8')
for repo in repo_list:
    waktu = repo.find(class_='kota').text
    c = repo.find(class_='heading-md').text
    print(f'{ waktu } { c }')