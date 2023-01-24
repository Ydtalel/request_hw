import requests
import yadisk


def find_smartest():
    url = 'https://akabab.github.io/superhero-api/api/all.json'
    response = requests.get(url=url)
    data = response.json()
    count = 0
    name = ''
    for hero in data:
        if 'Hulk' in hero.values() or 'Captain America' in hero.values() or 'Thanos' in hero.values():
            intelligence = hero['powerstats']['intelligence']
            if intelligence > count:
                count = intelligence
                name = hero['name']
    return f"Самый умный - {name}, его интеллект равен {intelligence}"


# вариант решения через библиотеку yadisk
# def upload():
#     yandex_token = input('Введите ваш токен: ')
#     path_ = input('Введите путь к загружаемому файлу: ')
#     dst_path = '/' + path_.split('/')[-1]
#     file = yadisk.YaDisk(token=yandex_token)
#     file.upload(path_, dst_path)


def get_question():
    stack_url = 'https://api.stackexchange.com/'
    question = '/2.3/questions?fromdate=1674345600&todate=1674432000&order=desc&sort=creation&tagged=Python&site=stackoverflow'
    result = requests.get(stack_url + question)
    info1 = result.json()
    dict_of_q = {}
    for q in info1['items']:
        dict_of_q[q['title']] = q['link']
    return dict_of_q


## task-1
# print(find_smartest())

## task-2
## upload()
class YaUploader:
    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def _get_upload_link(self, file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        return response.json()

    def upload(self, file_path, filename):
        """Метод загружает файлы на яндекс диск"""
        href = self._get_upload_link(file_path=file_path).get("href", "")
        response = requests.put(href, data=open(filename, 'rb'))
        response.raise_for_status()


if __name__ == '__main__':
    path_to_file = input('Введите путь к файлу на компьютере: ')
    token = input('Введите ваш токен: ')
    file_name = path_to_file.split('/')[-1]
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file, file_name)

## task-3   https://api.stackexchange.com/docs/questions
# print(get_question())
