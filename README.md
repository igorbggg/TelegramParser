# Парсер сообщений телеграм каналов
Скрипт позволяет спарсить сообщения из определенного набора каналов. 
Результатом работы скрипта являются файлы с JSON-представлением сообщений.  

Описание полей:  
`message.id` - id канала, которому принадлежит сообщение (не совсем логично, но пока так);  
`message.date` - дата создания;  
`message.edit_date` - дата редактирования;  
`message.views` - кол-во просмотров;  
`message.forwards` - кол-во пересылок (не уверен, но судя по докстрингам - это так);  
`message.text` - форматированный текст;  
`message.raw_text` - "сырой" текст.  

# Инструкция по использованию скрипта

## Алгоритм получения ключа
1. Перейти на my.telegram.org и авторизоваться по номеру телефона
2. Создать приложение (поля заполнить на своё усмотрение, 
   вроде как это особо ни на что не влияет)
3. Будут созданы два ключа: api_id и api_hash. Их и нужно использовать в main.py

## Первый запуск
При первом запуске скрипт единожды запросит авторизацию для создания файлов сессии.
Это необходимо для работы объекта TelegramClient.

## Прочее
Для корректной работы скрипта необходимо наличие подписки на все каналы, 
из словаря ACCOUNTANT_CHANNELS_IDS

Список каналов:  
https://t.me/eglavbukru  
https://t.me/netipichniy_buh  
https://t.me/obuchenie14  
https://t.me/knopkanews  
https://t.me/accwhisper  
https://t.me/ob_nal  
https://t.me/profaudit  
https://t.me/v_ritme_cifr  