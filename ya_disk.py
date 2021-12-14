from pprint import pprint

import requests
# для подготовки ДЗ
TOKEN = 'AQAAAAAK4pXFAADLWz4B-ZsTOEpauF6kH5Jq2n0'
class YandexDisk:

    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def get_files_list(self):
        files_url = 'https://cloud-api.yandex.net/v1/disk/resources/files'
        headers = self.get_headers()
        response = requests.get(files_url, headers=headers)
        return response.json()

    def _get_upload_link(self, disk_file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        pprint(response.json())
        return response.json()

    def upload_file_to_disk(self, disk_file_path, filename):
        href = self._get_upload_link(disk_file_path=disk_file_path).get("href", " ")
        response = requests.put(href, data=open(filename, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print("Success")

if __name__ == '__main__':
    ya = YandexDisk(token=TOKEN)
    # pprint(ya.get_files_list())
    print()
    ya._get_upload_link('Screenshots/gloxinia.jpg')
    # pprint(resp_dict)
    print()
    # print(resp_dict.get('href'))
    print()
    # print(f"Количество файлов на Яндекс-диске равно {len(ya.get_files_list()['items'])}", "\n")
    ya.upload_file_to_disk('Screenshots/gloxinia.jpg', 'gloxinia.jpg')    
