import requests
import random


def GettingAyah():
    """The code used to get an Ayah from the Quran every fixed time"""
    while True:
        ayah = random.randint(1, 6237)
        url = f'http://api.alquran.cloud/v1/ayah/{ayah}'
        res = requests.get(url)
        if len(res.json()['data']['text']) <= 280:
            return res.json()['data']['text']
