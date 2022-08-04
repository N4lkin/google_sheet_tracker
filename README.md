# Как запустить проект:
## Скопировать репозиторий

	123

или

    123

## Настройте переменные окружения
### Вы можете сделать это любым удобным для вас способом. Например:
##### Из корня проекта введите
    ln -s .env venv/.env
##### добавьте в конец файлы venv/bin/activate
    export `grep -Ev '^#|^$|=$' .env`
## Установите все зависимости
    pip3 install -r base_requirements.txt

    pip3 install -r tests_requirements.txt


## Поднимите Docker-Compose
##### из корня проекта введите (флаг -d нужен для скрытия логирования)
    docker-compose -f dev-compose up -d 
