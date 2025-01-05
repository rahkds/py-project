import requests
import bs4

# result = requests.get("https://en.wikipedia.org/wiki/Grace_Hopper")
# soup = bs4.BeautifulSoup(result.text,"lxml")
# print(soup.select('.vector-toc-list-item'))




##### this code for image download web scraping #####

result = requests.get("https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)")
soup = bs4.BeautifulSoup(result.text,"lxml")
list = soup.select('img.mw-file-element')

for elem in list:
    # print(elem.get_attribute_list('src'))
    if "Deep_Blue.jpg" in elem.get_attribute_list('src')[0]:
        image_url = "https:"+elem.get_attribute_list('src')[0]
        print(image_url)
        image_link = requests.get(image_url)
        print(image_link.content)
        f = open("my_computer_image.jpg", 'wb')
        f.write(image_link.content)
        f.close()
