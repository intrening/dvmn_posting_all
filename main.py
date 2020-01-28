import os
from dotenv import load_dotenv
import vk_api
import telegram
import requests


def public_vk(file_name, message):
    vk_access_token = os.getenv('VK_ACCESS_TOKEN')
    group_id = os.getenv('VK_GROUP_ID')
    album_id = os.getenv('VK_ALBUM_ID')
    vk_session = vk_api.VkApi(token=vk_access_token)
    upload = vk_api.VkUpload(vk_session)
    photo = upload.photo(
        file_name,
        album_id=album_id,
        group_id=group_id,
    )

    vk = vk_session.get_api()
    vk.wall.post(
        owner_id=f'-{group_id}',
        message=message,
        attachments=f'photo-{group_id}_{photo[0]["id"]},',
    )


def public_telegram(file_name, message):
    telegram_chat_id = os.getenv('TELEGRAM_CHAT_ID')
    telegram_bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
    bot = telegram.Bot(token=telegram_bot_token)
    bot.send_message(
        chat_id=telegram_chat_id,
        text=message,
    )
    bot.send_photo(chat_id=telegram_chat_id, photo=open(file_name, 'rb'))


def post_facebook(file_name, message):
    fb_access_token = os.getenv('FB_ACCESS_TOKEN')
    fb_group_id = os.getenv('FB_GROUP_ID')
    url = f'https://graph.facebook.com/{fb_group_id}/photos'
    params = {
        'caption': message,
        'access_token': fb_access_token,
    }
    files = {
        'upload_file': open(file_name, 'rb'),
    }
    response = requests.post(url=url, params=params, files=files)
    response.raise_for_status()


def main():
    load_dotenv()


if __name__ == "__main__":
    main()
