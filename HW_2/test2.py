"""Урок 1. Реализация тестирования API с использованием DDT
Условие: Добавить в задание с REST API ещё один тест, в котором создаётся новый пост,
а потом проверяется его наличие на сервере по полю «описание».
Подсказка: создание поста выполняется запросом к https://test-stand.gb.ru/api/posts
с передачей параметров title, description, content.
"""

from main import login, get, data
import requests

token = login()
title = "HW_1"
description = "web_autotest"
content = "Ivanov Dmitriy"

def create_post(token, title, description, content):
    requests.post(data["url_posts"],
                   headers={"X-Auth-Token": token},
                   params={"title": title, "description": description, "content": content})

create_post(token, title, description, content)


def test_check_post(login):
    posts = get(login)
    lst = posts["data"]
    posts_descriptions = [el["description"] for el in lst]
    assert description in posts_descriptions, "Такого поста нет"