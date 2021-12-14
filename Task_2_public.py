from pprint import pprint

import json

import requests

print()

class YaUploader:
    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def find_file_path(filename):
        import os
        filename = input("Введите имя файла с его расширением: ")
        file_path = os.path.join(os.getcwd())
        file_path = file_path + '\\' + filename
        ft = file_path.split('\\')
        path_to_file = ft[-2:]
        f_p = path_to_file[0] + '\\' + path_to_file[1]
        # print(f_p)
        return f_p

    def disk_file_path(folder, find_file_path):
        folder = input("Введите имя папки на Яндекс-диске: ")
        ffp = find_file_path.split('\\')
        f_name = ffp[-1]
        path_to_disk = folder + '/' + f_name
        # print(path_to_disk)
        return path_to_disk
       
    def _get_upload_link(self, disk_file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        return response.json()

    def upload(self, disk_file_path, find_file_path):
        """Метод принимает на вход путь до файла на компьютере и сохраняет файл на Яндекс.Диск 

        с таким же именем"""
        href = self._get_upload_link(disk_file_path=disk_file_path).get("href", " ")
        response = requests.put(href, data=open(find_file_path.split('\\')[1], 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print("Success")

    
TOKEN = " "        

print()



if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    
    token = TOKEN
    uploader = YaUploader(token)
    path_to_file = uploader.find_file_path()
    result = uploader.upload(uploader.disk_file_path(path_to_file), path_to_file)
