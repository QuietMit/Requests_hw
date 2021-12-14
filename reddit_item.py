from pprint import pprint

import requests

class Reddit:
    def get_popular_videos(self):
        url = "https://reddit.com/r/gifs/top.json?t=day"
        response = requests.get(url, headers = {"User-agent" : "netology"})
        return response.json()

if __name__ == '__main__':
    raddit = Reddit()
    pprint(raddit.get_popular_videos())

# def test_request():
#     url = "https://bootssizes/get"
#     params = {"model": "nike123"}
#     headers = {"Authorization": "secret - token - 123"}
#     response = requests.get(url, params=params, headers=headers, timeout=5)
#     pprint(response)


# if __name__ == '__main__':
#     raddit = Reddit()
#     pprint(raddit.get_popular_videos())
#     ya = YandexDisk(token="TOKEN")
#     ya.upload_file_to_disk("test/netology", "test.txt")