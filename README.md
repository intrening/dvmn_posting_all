# Автопостинг в социальных сетях Vkontakte, Telegram, Facebook

Программа публикует текст и картинку в соц.сетях.

### Как установить
Python3 должен быть уже установлен. 
Используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```
В каталоге с программой создайте файл .env, в котором укажите переменные:

`VK_ACCESS_TOKEN` - токен от приложения ВКонтакте

`VK_GROUP_ID`  - id группы ВКонтакте

`VK_ALBUM_ID` - id альбома в группе ВКонтакте

`TELEGRAM_CHAT_ID` - id канала в Telegram

`TELEGRAM_BOT_TOKEN` - токен бота-администратора группы Telegram

`FB_ACCESS_TOKEN` - access token Facebook

`FB_GROUP_ID` - id группы в Facebook


### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
