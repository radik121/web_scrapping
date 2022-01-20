import requests as req
from bs4 import BeautifulSoup

KEYWORDS = ['дизайн', 'фото', 'web', 'python']

HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,'
              'application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'ru,en;q=0.9,zh;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': '_ga=GA1.2.1700603580.1631601403; _ym_d=1631601403; _ym_uid=1631601403386598800; fl=ru; hl=ru; '
              'habr_web_home=ARTICLES_LIST_ALL; visited_articles=349860:247987:462607; _ym_isad=1; '
              '_gid=GA1.2.1514494432.1642498695',
    'Host': 'habr.com',
    'Referer': 'https://github.com/netology-code/py-homeworks-advanced/tree/master/6.Web-scrapping',
    'sec-ch-ua': '"Chromium";v="94", "Yandex";v="21", ";Not A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/94.0.4606.85 YaBrowser/21.11.4.727 Yowser/2.5 Safari/537.36 '
}


def read_post(link):
    res = req.get(link, headers=HEADERS)
    soup_res = BeautifulSoup(res.text, 'html.parser')
    return soup_res.find('article')


def search_posts(keys):
    url = f'https://habr.com/ru/all/'
    response = req.get(url, headers=HEADERS)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    articles = soup.find_all('div', class_="tm-article-snippet")
    # print(len(articles))
    for art in articles:
        link = 'https://habr.com' + art.find('a', class_="tm-article-snippet__readmore").get('href')
        post = read_post(link)
        time_post = post.find('time')
        title_post = post.find('h1')
        for key in KEYWORDS:
            if key in post.text or key.title() in post.text:
                print(f'{key.title()}\n{time_post.text} - {title_post.text} - {link}')
# def search_posts(keywords):
#     url = f'https://habr.com/ru/all/'
#     response = req.get(url, headers=HEADERS)
#     response.raise_for_status()
#     soup = BeautifulSoup(response.text, 'html.parser')
#     read_more_link = soup.find_all('a', class_="tm-article-snippet__readmore")
#     print(len(read_more_link))
#     for link in read_more_link:
#         post_link = 'https://habr.com' + link.get('href')
#         post = read_post(post_link)
#         time_post = post.find('time')
#         title_post = post.find('h1')
#         for key in KEYWORDS:
#             if key in post.text:
#                 print(f'{key.title()}\n{time_post.text} - {title_post.text} - {post_link}')


if __name__ == '__main__':
    search_posts(KEYWORDS)