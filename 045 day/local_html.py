from bs4 import BeautifulSoup


def get_html_content(file_path):
    with open(file_path, 'r') as file:
        return file.read()


contents = get_html_content('website.html')
soup = BeautifulSoup(contents, 'html.parser')
print(soup.title)
print(soup.title.string)
print(soup.a)
# print(soup.prettify())
all_anchor_tags = soup.find_all(name='a')
for tag in all_anchor_tags:
    print(tag.getText())
    print(tag.get('href'))

heading = soup.find(name='h1', id='name')
print(heading)

selection_css = soup.select_one(selector='p a')
print(selection_css)

selection_css_list = soup.select(selector='.heading')
print(selection_css_list)