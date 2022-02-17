import requests
from bs4 import BeautifulSoup


def getCharts(date):
    response = requests.get('https://www.billboard.com/charts/hot-100/' + date)
    billboard_page = response.text
    soup = BeautifulSoup(billboard_page, 'html.parser')

    song_names = soup.find_all(name='span', class_='chart-element__information__song text--truncate color--primary')
    song_artists = soup.find_all(name='span',
                                 class_='chart-element__information__artist text--truncate color--secondary')
    song_ranks = soup.find_all(name='span', class_='chart-element__rank__number')
    return song_names, song_artists, song_ranks
