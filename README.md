# Adding-a-program-to-the-Docker-container, Lab_1

# Программа Telegram_BOT

## Оглавление

0. Автор программы.

1. Краткое описание программы.

## Автор программы:
студент УРФУ ФТИ  Борзых А.П., группа ФТ-310008
[:arrow_up:Оглавление](#Оглавление)

## Краткое описание программы:
Был создан телеграм-бот, в нем можно найти интересующий ресурс по учебным дисциплинам, который необходим пользователю, а также можно предложить, какую-либо информацию по своему желанию.    
[:arrow_up:Оглавление](#Оглавление)

## Руководство пользования программой:
1. Telegram_Bot написан на языке Phyton, в среде разработки PyCharm.
2. Из того, что программа написана на языке Phyton, ее можно запустить с помощью приложений, которые поддерживают расширение Phyton (.py).
3. Telegram_Bot имеет название "Помощник по учебе👨‍💻", ссылка: https://t.me/study_assistant_school_bot
4. Для запуска Docker контейнера нужно:
   1. Убедитесь, что Docker установлен и настроен на вашем компьютере.
   2. Откройте командную строку или терминал и перейдите в каталог, в котором находится ваш Docker-контейнер.
   3. Запустите контейнер с использованием команды docker run, указав имя вашего образа:
                             docker run senzor/my-telegram-bot
   Если вы хотите указать определенный тэг, добавьте его после имени образа:
                             docker run senzor/my-telegram-bot:your_tag
   Ваш контейнер будет запущен, и телеграм-бот будет доступен для использования.

   4. Обратите внимание, что вам может потребоваться настроить контейнер, чтобы он имел доступ к интернету и мог взаимодействовать с серверами Telegram. Подробности зависят от вашей конкретной конфигурации.
   5. Теперь можно проверить работу бота в Telegram.
  ## Ссылки:
  1. Docker_Hub: https://hub.docker.com/repository/docker/senzor/my-telegram-bot/general
  
  2. Git_Hub: https://github.com/arsen11yy/Adding-a-program-to-the-Docker-container

## Скрин Telegram_BOT:
![image](https://github.com/arsen11yy/Adding-a-program-to-the-Docker-container/assets/112753125/2fd301d1-67f1-417f-9060-c0eb2a887609)


