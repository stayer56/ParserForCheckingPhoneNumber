def phone_search(num):
    import requests
    from bs4 import BeautifulSoup

    # Заголовки для имитации запроса от браузера
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:134.0) Gecko/20100101 Firefox/134.0",
        "X-Amzn-Trace-Id": "Root=1-67a06409-06ecda52579e7ed250df8b92",
    }

    # Формируем URL для запроса, добавляя номер телефона
    url = "https://www.tbank.ru/oleg/who-called/info/" + num + "/"

    # Отправляем GET-запрос на сайт
    response = requests.get(url, headers=headers)
    response.encoding = "utf-8"  # Устанавливаем кодировку ответа

    # Парсим HTML-страницу с помощью BeautifulSoup
    soup = BeautifulSoup(response.text, "lxml")

    # Список для хранения информации о номере
    info_number = []

    # Находим все теги <span> на странице
    span_all = soup.find_all("span")

    # Проходим по всем найденным тегам <span>
    for span in span_all:
        # Проверяем, содержит ли текст тега нужную информацию
        if (
            "Категория номера" in span.text
            or "Название компании" in span.text
            or "Регион:" in span.text
            or "Оператор" in span.text
            or "Код оператора" in span.text
        ):
            # Если информация найдена, добавляем ее в список
            info_number.append(span.text)

    # Если информация о номере не найдена, добавляем соответствующее сообщение
    if info_number == []:
        info_number.append("Информации о номере нет")

    # Возвращаем список с информацией о номере
    return info_number


# Ввод номера телефона пользователем
num = input("\nВведите номер: \n+7")[:10]  # Убираем +7 и оставляем только 10 цифр
num = "7" + num  # Добавляем 7 в начало номера

# Вызов функции и вывод результата
print(phone_search(num))
