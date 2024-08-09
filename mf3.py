import requests
from bs4 import BeautifulSoup
url = "https://cricblog.net/#google_vignette"
response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")
    text = soup.get_text()
    print("Text from the webpage:")
    print(text)
    links = soup.find_all('a')
    print("\nLinks from the webpage:")
    for link in links:
        href = link.get('href')
        text = link.text
        print(f"Link: {href}, Text: {text}")
    images = soup.find_all('img')
    print("\nImages from the webpage:")
    for img in images:
        src = img.get('src')
        alt = img.get('alt', 'No alt text provided')
        print(f"Image Source: {src}, Alt Text: {alt}")
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
