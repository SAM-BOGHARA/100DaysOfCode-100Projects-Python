# from bs4 import BeautifulSoup as bs

# with open("INTERMEDIATE/day45/website.html",encoding='utf-8') as file:
#     contents = file.read()

# soup = bs(contents,"html.parser")

# print(soup.title.string)
# print(soup.prettify())
# all_anchor_tags =  soup.find_all(name="a")

# for tag in all_anchor_tags:
#     # print(tag.getText())
#     # print(tag)
#     print(tag.get("href"))

# heading = soup.find(name="h1" , id = "name")

# print(heading)

# section_heading = soup.find(name="h3",class_ = "heading")
# print(section_heading)
# print(section_heading.getText())
# print(section_heading.get("class"))

# company_url = soup.select_one(selector= "#name")
# print(company_url)

# headings = soup.select(selector = ".heading")
# print(headings)



from bs4 import BeautifulSoup as bs
import requests

response = requests.get("https://news.ycombinator.com")

# print(response.status_code)
yc_webpage = response.text

soup = bs(yc_webpage,"html.parser")
# print(soup.title)

articles= soup.find_all(name="a",class_ = "titlelink")
article_texts = []
article_links = []
for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)
article_upvotes =  [int(score.getText().split()[0]) for score in soup.find_all(name = "span" ,class_ = "score")]

print(article_texts)
print(article_links)
print(article_upvotes)

max_of_the_list = max(article_upvotes)
index_of_max = article_upvotes.index(max_of_the_list)
print(index_of_max)
print(article_texts[index_of_max],article_links[index_of_max],max_of_the_list)
