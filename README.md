Краткое описание задания:
В 2018 году Джеймс Клир написал книгу «Атомные привычки», которая посвящена приобретению новых полезных привычек и искоренению старых плохих привычек. 
Заказчик прочитал книгу, впечатлился и обратился к вам с запросом реализовать трекер полезных привычек.

В рамках учебного курсового проекта реализуйте бэкенд-часть SPA веб-приложения.

Модель Привычка:
- Пользователь — создатель привычки.
- Место — место, в котором необходимо выполнять привычку.
- Время — время, когда необходимо выполнять привычку.
- Действие — действие, которое представляет из себя привычка.
- Признак приятной привычки — привычка, которую можно привязать к выполнению полезной привычки.
- Связанная привычка — привычка, которая связана с другой привычкой, важно указывать для полезных привычек, но не для приятных.
- Периодичность (по умолчанию ежедневная) — периодичность выполнения привычки для напоминания в днях.
- Вознаграждение — чем пользователь должен себя вознаградить после выполнения.
- Время на выполнение — время, которое предположительно потратит пользователь на выполнение привычки.
- Признак публичности — привычки можно публиковать в общий доступ, чтобы другие пользователи могли брать в пример чужие привычки.
- Последнее время выполнения - время когда пользователь последний раз выполнил привычку

Валидаторы:
- Исключить одновременный выбор связанной привычки и указания вознаграждения.
- Время выполнения должно быть не больше 120 секунд.
- В связанные привычки могут попадать только привычки с признаком приятной привычки.
- У приятной привычки не может быть вознаграждения или связанной привычки.
- Нельзя выполнять привычку реже, чем 1 раз в 7 дней.

Права доступа:
- Каждый пользователь имеет доступ только к своим привычкам по механизму CRUD.
- Пользователь может видеть список публичных привычек без возможности их как-то редактировать или удалять.

Эндпоинты:

1 Регистрация - post запрос на адрес http://127.0.0.1:8000/users/register/
При регистрации необходимо указать email, password и telegram_id аккаунта (необходим для рассылки напоминаний посредством telegram)

2 Авторизация - post запрос на адрес http://127.0.0.1:8000/users/token/
В ответ придет access_token и refresh_token. Они необходимы для доступа к другим эндпоинтам

3 Создание привычки - post запрос на адрес http://127.0.0.1:8000/habits/create/

4 Изменение привычки - patch или put запрос на адрес http://127.0.0.1:8000/habits/update/<id привычки> (редактировать можно привычки созданные авторизованным пользователем)

5 Удаление привычки - delete запрос на адрес http://127.0.0.1:8000/habits/update/<id привычки> (удалить можно привычки созданные авторизованным пользователем)

6 Просмотр списка привычек (по 5 на странице) созданных авторизованным пользователем - get запрос на адрес http://127.0.0.1:8000/habits/

7 Просмотр списка публичных (у которых флаг is_public=True) - get запрос на адрес http://127.0.0.1:8000/habits/public/

8 Просмотр документации проекта - в адресной строке браузера ввести http://127.0.0.1:8000/swagger/ или http://127.0.0.1:8000/redoc/ 

Интеграция с телеграмом:
Сервис напоминает о привычке посредством телеграм. Для интеграции с телеграмом необходимо выполнить следующее:
- При регистрации пользователя указать telegram_id аккаунта на который будут приходить уведомления.
Узнать его можно, например, следующим образом: найти бота @userinfobot, нажать старт, в ответ он пришлет информацию об аккаунте в которой будет id
- Найти в телеграме бота @AleksandrHabitBot и нажать start, таким образом Вы разрешите ему отсылать сообщения.
- Ждать нужного времени, бот обязательно напомнит о привычке)
