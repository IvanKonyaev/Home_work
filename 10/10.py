# + Реализовать две функции: write_to_file(data) и read_file_data().
# Которые соотвественно: пишут данные в файл и читают данные из файла.

# If you change mode = 'w', then text in data.txt file fill be delited and new information adding.

# def write_to_file(data, content, mode='a'):
# 	with open(data, mode=mode) as d:
# 		return d.write(content)

# def read_to_file(data2):
# 	with open(data2) as d:
# 		return d.read()

# write_to_file('data.txt', 'New line\n')
# write_to_file('data.txt', 'New line\n')
# write_to_file('data.txt', 'New line\n')

# print(read_to_file('data2.txt'))

# + Реализовать следующую логику: получать при помощи requests данные сервиса https://jsonplaceholder.typicode.com/
# (сущность можно выбрать любую, например https://jsonplaceholder.typicode.com/comments),
# выводить в консоль все пары заголовки, сохранять полученный json в файл на диск.

import requests
import json


def write_to_file(file, data, mode='w'):
    print('Writing to {}\n'.format(file))
    with open(file, mode) as newfile:
        newfile.write(data)


def get_service_data(url):
    result = requests.get(url)
    return result


response = get_service_data('https://jsonplaceholder.typicode.com/comments')
dict_for_json = {}
for hdr, value in response.headers.items():
    dict_for_json[hdr] = value
    print('{}:{}\n'.format(hdr, value))


write_to_file('site_response.json', json.dumps(dict_for_json, sort_keys=True, indent=4))

# + Обратиться с странице https://habrahabr.ru/. Получить текст страницы.
# При помощи регулярных выражений нужно получить все ссылки со страницы на другие.
# Ответить себе на вопрос удобно ли так делать?