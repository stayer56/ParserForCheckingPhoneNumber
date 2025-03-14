Программа предназначена для поиска информации о телефонном номере. Она использует библиотеку requests для отправки HTTP-запросов и библиотеку BeautifulSoup для парсинга HTML-страницы. 
Программа извлекает информацию о номере телефона, такую как категория номера, название компании, регион, оператор и код оператора.
Основные шаги программы:

    Ввод номера телефона: 
    Пользователь вводит номер телефона, который начинается с +7. Программа удаляет +7 и оставляет только последние 10 цифр.

    Формирование URL: 
    Программа формирует URL для запроса, добавляя введенный номер телефона к базовому URL сайта.

    Отправка HTTP-запроса: 
    Программа отправляет GET-запрос на сайт, используя заголовки, которые имитируют запрос от браузера.

    Парсинг HTML-страницы: 
    С помощью библиотеки BeautifulSoup программа анализирует HTML-код страницы и извлекает нужную информацию.

    Сбор информации: 
    Программа ищет определенные теги <span>, которые содержат информацию о номере телефона. Если информация найдена, она добавляется в список info_number.

    Вывод результата: 
    Если информация о номере найдена, она выводится на экран. Если информация отсутствует, программа сообщает об этом.

Программа позволяет пользователю получить информацию о телефонном номере, используя веб-скрейпинг. 
Она проста в использовании и может быть расширена для обработки дополнительных данных или интеграции с другими сервисами.
