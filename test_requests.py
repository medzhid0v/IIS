import requests


def create_book(host, data):
    """Добавить книгу в базу."""
    response = requests.post(url=f'{host}/book', json=data)
    if response.status_code == 200:
        return response.json()
    else:
        return {'status': 'error', 'status_code': response.status_code, 'text': response.text}


def get_all_books(host):
    """Получить список всех книг."""
    response = requests.get(url=f'{host}/book/all')
    if response.status_code == 200:
        return response.json()
    return {'status': 'error', 'status_code': response.status_code, 'text': response.text}


def get_book_by_id(host, book_id):
    """Получить книгу по ID."""
    response = requests.get(url=f'{host}/book/{book_id}')
    if response.status_code == 200:
        return response.json()
    return {'status': 'error', 'status_code': response.status_code, 'text': response.text}


def update_book_info(host, book_id, data):
    """Обновить информацию о книге по ID."""
    response = requests.put(url=f'{host}/book/{book_id}', json=data)
    if response.status_code == 200:
        return response.json()
    return {'status': 'error', 'status_code': response.status_code, 'text': response.text}


def delete_book_by_id(host, book_id):
    """Удалить книгу по ID."""
    response = requests.delete(url=f'{host}/book/{book_id}')
    if response.status_code == 200:
        return response.json()
    return {'status': 'error', 'status_code': response.status_code, 'text': response.text}


# Пример использования:
host = 'http://127.0.0.1:8080'

print(get_all_books(host))

# new_book_data = {"id": 1, "title": "Какой-то заголовок", "author": "Мага2", "year": 2119}
# print(create_book(host, new_book_data))

book_id = 3
# print(get_book_by_id(host, book_id))

update_data = {"id": 3, "title": "Новый", "author": "Мага3", "year": 2120}
print(update_book_info(host, book_id, update_data))

# print(delete_book_by_id(host, book_id))
