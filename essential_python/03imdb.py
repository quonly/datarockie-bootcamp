import gazpacho
import pandas as pd
from pprint import pprint

url = "https://www.imdb.com/search/title/?groups=top_100&sort=user_rating,desc"
html = gazpacho.get(url)
imdb = gazpacho.Soup(html)

# extract titles, ratings, years from imdb data into lists.
titles = [title.find('a').text for title in imdb.find(
    'h3', {'class': 'lister-item-header'})]
ratings = [rating.strip() for rating in imdb.find(
    'div', {'class': 'ratings-imdb-rating'})]
years = [year.strip().replace('(', '').replace(')', '') for year in imdb.find(
    'span', {'class': 'lister-item-year'})]  # exclude parentheses

# create dictionary data to store all list above
data = {
  'title': titles,
  'rating': ratings,
  'year': years
}

df = pd.DataFrame(data)

pprint(df.head())

# df.to_csv("imdb_top_100.csv")
