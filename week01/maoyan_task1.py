# 使用 requests、bs4 库，爬取猫眼电影（）的前 10 个电影名称、电影类型和上映时间，并以 UTF-8 字符集保存到 csv 格式的文件中。
import requests
from bs4 import BeautifulSoup as bs
from fake_useragent import UserAgent
import pandas as pd
from fake_useragent import UserAgent

# user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1 Safari/605.1.15'
ua = UserAgent()
user_agent = ua.random

header = {'user-agent':user_agent}
myurl = 'http://maoyan.com/films?showType=3'

response = requests.get(myurl,headers=header)
bs_info = bs(response.text, 'html.parser')
# print(bs_info)

movies = []
num = 0
for tags in bs_info.find_all('div', attrs={'class': 'movie-item-hover'}):
    movie = []
    if num < 10:
        movie_title = tags.find('span', attrs={'class': 'name'}).text
        if movie_title != '':
            movie.append(movie_title)

        for dtags in tags.find_all('div', attrs={'class': 'movie-hover-title movie-hover-brief'}):
            movie_time = dtags.text.replace("\n", "").replace(" ", "").split(':')[1]
            movie.append(movie_time)
        for dtags in tags.find_all('div', attrs={'class': 'movie-hover-title'}):
            hover_tag = dtags.find('span').text
            if hover_tag == '类型:':
                movie_type = dtags.text.replace("\n", "").replace(" ", "").split(':')[1]
                movie.append(movie_type)

        movies.append(movie)
        num = num + 1

movies1 = pd.DataFrame(data = movies)
movies1.to_csv('./maoyan_movie_top10.csv', encoding='utf8', index=False, header=False)