# О Приложении:
## Приложение представляет из себя скрипт для обновления данных берущихся из Google Sheets (смотрите внизу README).
## Так же используется API aiogram для уведомления администратора о событиях в работе скрипта (Неверный формат данных при заполнении таблицы / истечение сроков поставки)

# Как запустить проект:
## Скопировать репозиторий

	git clone https://github.com/N4lkin/google_sheet_tracker.git

или

	git clone git@github.com:N4lkin/google_sheet_tracker.git

## Установите все зависимости
    pip3 install -r requirements.txt

## Поднимите Docker-Compose
##### из корня проекта введите (флаг -d нужен для скрытия логирования)
    cp .env.example .env

    docker-compose -f dev-compose up -d

## Настройте переменные окружения

### Вы можете сделать это любым удобным для вас способом. Например:
##### Из корня проекта введите
    ln -s .env venv/.env
##### добавьте в конец файлы venv/bin/activate
    export `grep -Ev '^#|^$|=$' .env`

## Примите имеющиеся миграции
    alembic upgrade head

## Запустите скрипт
##### запустите main/run_script.py любым удобным для вас образом

## Чтобы запустить уведомления из tg бота - следуйте следующей инструкции (необязательно)

### 1) Начните чат с https://t.me/username_to_id_bot
### 2) Запомните полученный ID
### 3) Запустите файл services/create_notification_recipient.py и следуйте инструкциям
### 4) Отправьте любое сообщение https://t.me/canalservice_test_bot

[Google Sheets](https://docs.google.com/spreadsheets/d/1t8NjnDmAAVTqDGaNWxI8V5FNy8ecryFZ73un1nEfhmc/edit#gid=0)
