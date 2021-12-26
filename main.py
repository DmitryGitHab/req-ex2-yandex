from pprint import pprint
import requests


class YaUploader:

    def __init__(self, token):
        self.token = TOKEN

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

    def _get_upload_link(self, file):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": file, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        pprint(response.json())
        return response.json()

    def upload_file_to_disk(self, file_path: str):
        file = file_path.split('\\')[-1]
        href = self._get_upload_link(file=file).get("href", "")

        response = requests.put(href, data=open(file_path, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print("Success")


if __name__ == '__main__':
    TOKEN = ""
    # TOKEN = input('Введите ваш токен: ')
    path_to_file = input('Введите путь к файлу: ')
    ya = YaUploader(TOKEN)
    ya.upload_file_to_disk(path_to_file)
