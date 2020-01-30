import os
from dotenv import load_dotenv
import vk_api
import telegram
import requests
import argparse


def public_vk(token, group_id, album_id, file_name, message):
    vk_session = vk_api.VkApi(token=token)
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


def public_telegram(token, chat_id, file_name, message):
    bot = telegram.Bot(token=token)
    bot.send_message(
        chat_id=chat_id,
        text=message,
    )
    bot.send_photo(chat_id=chat_id, photo=open(file_name, 'rb'))


def post_facebook(token, group_id, file_name, message):
    url = f'https://graph.facebook.com/{group_id}/photos'
    params = {
        'caption': message,
        'access_token': token,
    }
    files = {
        'upload_file': open(file_name, 'rb'),
    }
    response = requests.post(url=url, params=params, files=files)
    response.raise_for_status()


def main():
    load_dotenv()
    vk_access_token = os.getenv('VK_ACCESS_TOKEN')
    vk_group_id = os.getenv('VK_GROUP_ID')
    vk_album_id = os.getenv('VK_ALBUM_ID')
    telegram_chat_id = os.getenv('TELEGRAM_CHAT_ID')
    telegram_bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
    fb_access_token = os.getenv('FB_ACCESS_TOKEN')
    fb_group_id = os.getenv('FB_GROUP_ID')

    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    parser.add_argument("message")
    args = parser.parse_args()
    filename, message = args.filename, args.message

    public_vk(
        token=vk_access_token,
        group_id=vk_group_id,
        album_id=vk_album_id,
        file_name=filename,
        message=message,
    )
    public_telegram(
        token=telegram_bot_token,
        chat_id=telegram_chat_id,
        file_name=filename,
        message=message,
    )
    post_facebook(
        token=fb_access_token,
        group_id=fb_group_id,
        file_name=filename,
        message=message,
    )


if __name__ == "__main__":
    main()
