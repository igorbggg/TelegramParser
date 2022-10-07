import json
from typing import Dict

from telethon import TelegramClient
from telethon.tl.patched import Message

API_ID = 777
API_HASH = 'api_hash'
APP_NAME = 'parser'  # Имя приложения

LIMIT = 100
ACCOUNTANT_CHANNELS_IDS = {-1001359516226: 'Журнал "Главбух"',
                           -1001282727749: 'Нетипичный бухгалтер',
                           -1001502172112: 'Бухгалтерия онлайн',
                           -1001102196030: 'Кнопка – новости бизнеса и бухгалтерия для ИП и ООО',
                           -1001360616183: 'Обнальщик',
                           -1001306567848: 'Переводчик с бухгалтерского',
                           -1001486761039: 'Чёрная бухгалтерия',
                           -1001464659541: 'В РИТМЕ ЦИФР | Бухгалтерия с Евгенией Ковязиной'}


async def get_message_params(message: Message) -> Dict:
    """
    Достает необходимые параметры из сообщения
    :param message:
    :return:
    """
    return dict(
        id=message.chat.id,
        date=message.date.strftime("%Y-%m-%dT%H:%M:%S+00:00") if message.date else None,
        edit_date=message.edit_date.strftime("%Y-%m-%dT%H:%M:%S+00:00") if message.edit_date else None,
        views=message.views,
        forwards=message.forwards,
        text=message.text,
        raw_text=message.raw_text,
    )


async def parse_channels(channel_ids: Dict[int, str]):
    """
    Парсит каналы

    :param channel_ids:
    :return:
    """

    async for dialog in client.iter_dialogs():
        if dialog.id not in channel_ids.keys():
            continue

        messages = []
        async for message in client.iter_messages(dialog, limit=100000):
            messages.append(await get_message_params(message))

        with open(channel_ids[dialog.id] + '.json', 'w') as file:
            file.write(json.dumps(messages, ensure_ascii=False, indent=2))


if __name__ == '__main__':

    client = TelegramClient(APP_NAME, API_ID, API_HASH)

    with client:
        client.loop.run_until_complete(parse_channels(ACCOUNTANT_CHANNELS_IDS))
