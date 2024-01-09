from bot.loader import dp
from aiogram import types
import instaloader
import urllib.parse


context = instaloader.InstaloaderContext()
context.login("call.new.jasjan", "why?so4why?")


def get_scheme(post):
    text = "\n".join(i['node']['text'] for i in post['edge_media_to_caption']['edges'])
    return text


def get_shortcode(url: str):
    parsed = urllib.parse.urlparse(url)
    return parsed.path.replace('\\', '/').strip('/').split('/')[-1]


@dp.message_handler(lambda a: 'instagram.com' in a.text)
async def download_youtube_video(msg: types.Message):
    wait_msg = await msg.answer("⏳")
    post = instaloader.Post(context, node={"shortcode": get_shortcode(msg.text)})._full_metadata
    media_collection = []
    if 'video_url' in post:
        media_collection.append(types.InputMediaVideo(post['video_url']))
    if 'display_url' in post:
        media_collection.append(types.InputMediaPhoto(post['display_url']))
    if 'edge_sidecar_to_children' in post:
        for node in post['edge_sidecar_to_children']['edges']:
            if node['node']['is_video']:
                media_collection.append(types.InputMediaVideo(node['node']['video_url']))
            else:
                media_collection.append(types.InputMediaPhoto(node['node']['display_url']))
    await msg.answer_media_group(types.MediaGroup(media_collection))
    await msg.answer(get_scheme(post))
    await wait_msg.delete()
