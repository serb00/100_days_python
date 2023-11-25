from bs4 import BeautifulSoup
import requests

# response = requests.get('https://news.ycombinator.com/')
# response.raise_for_status()
# html_text = response.text
# soup = BeautifulSoup(html_text, 'html.parser')
# all_articles = soup.find_all(name='tr', class_='athing')
#
# texts = [str(article.getText()).strip() for article in all_articles] links = [article.select_one(
# selector='.titleline a').get('href') for article in all_articles] scores = [int(soup.select(selector=f"#score_{
# article.get('id')}")[0].getText().split()[0]) for article in all_articles] print(texts) print(links) print(scores)
#
# print("\nThe most upvoted article currently is:")
# max_score_index = scores.index(max(scores))
# print(texts[max_score_index])
# print(links[max_score_index])
# print(scores[max_score_index])


response = requests.get('https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best'
                        '-movies-2/')
response.raise_for_status()
html_text = response.text
soup = BeautifulSoup(html_text, 'html.parser')
all_movies = soup.find_all(name='h3', class_='title')
movies = [movie.getText() for movie in all_movies]

with open('movies.txt', 'w') as file:
    for movie in movies[::-1]:
        file.write(f"{movie}\n")
