import requests
import time
from datetime import datetime, timedelta


class StackOverFlow:
    def __init__(self):
        self.tags = ['python']
        now = datetime.now()
        data = now - timedelta(days=2)
        self.from_date = int(data.timestamp())
        self.questions = []

    def load_info(self, number_of_pages: int = 30):
        # Загружает топ самых активно обсуждаемых вопросов на Stack Overflow за последние 2 дня.
        # В качестве параметра принимает колличество вопросов, возвращаемое методом (по умолчинию 30)
        url = 'https://api.stackexchange.com/2.2/questions'
        params = {
            'pagesize': str(number_of_pages),
            'fromdate': str(self.from_date),
            'order': 'desc',
            'sort': 'activity',
            'tagged': ';'.join(self.tags),
            'site': 'stackoverflow'
        }
        reply = requests.get(url, params=params).json()
        self.questions = [
            {
                'title': item['title'],
                'link': item['link'],
                'tags': item['tags'],
                'creation_date': time.ctime(item['creation_date'])
            }
            for item in reply['items']
        ]
        self.questions.sort(key=lambda x: x['creation_date'])
        return reply

    def print_questions(self):
        # Выводит на экран соновную информацию прочитанных ранее вопросов
        dividing_line = f'__________________________________________\n'
        print(dividing_line)
        for item in self.questions:
            print(f'Зааголовок: {item["title"]}\n'
                  f'Ссылка: {item["link"]}\n'
                  f'Тэги: {", ".join(item["tags"])}\n'
                  f'Время публикации: {item["creation_date"]}\n'
                  f'{dividing_line}')
        print(f'Топ {len(self.questions)} самых обсуждаемых вопросов за последние 2 дня на Stack Overflow\n'
              f'(Отсортерованно по дате)')


def main():
    stack_overflow = StackOverFlow()
    stack_overflow.load_info(100)
    stack_overflow.print_questions()


main()