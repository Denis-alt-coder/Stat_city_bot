from aiogram import types
from aiogram.types import InputFile
from loader import dp, bot
from . import start_keyboard as kb


@dp.message_handler(commands=['start'])
async def bot_start(message: types.Message):
    photo = InputFile('D:/Downloads/PYTHON/telebot/handlers/users/bot_photo.jpg')
    await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    await message.answer(f"Привет, Denis! Рады вас видеть😊 \n \n С помощью этого бота вы сможете получить доступ к сервису аналитики для маркетплейсов, который подходит именно вам.",reply_markup=kb.start_kb)


@dp.message_handler(lambda message: message.text == "Выбрать сервис аналитики📊")
async def tarifs(message: types.Message):
    photo = InputFile('D:/Downloads/PYTHON/telebot/handlers/users/bot_photo.jpg')
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    await message.answer('Выберите интересующий вас сервис из доступных на данный момент:',reply_markup=kb.analitic_kb)


@dp.message_handler(lambda message: message.text == "О складчине💭")
async def about(message: types.Message):
    photo = InputFile('D:/Downloads/PYTHON/telebot/handlers/users/bot_photo.jpg')
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    await message.answer('Что такое «складчина»?\n\n'
    "Складчина? - совместная покупка доступа к тому или иному онлайн продукты (в нашем случае). Таким образом каждый человек может пользоваться полноценным функционалом сервисов за доступные средства.\n\n"
    "Например, 10 человек хотят купить MPstats за 28.000 рублей, то каждому из них нужно скинуться примерно по 2800 рублей.\n\n"
    "🔘 Есть ли график пользования или очередь ? - графика и очередей НЕТ, заходите и пользуетесь полным функционалом, когда вам удобно.\n\n"
    "🔘 Могу ли я подвязать свой личный кабинет WB через API в аккаунт мпстат ? - Да, вы можете это сделать.\n\n" 
    "🔘 Через какой браузер предоставляется доступ в аккаунт - Любой, который удобен вам.\n\n" 
    "🔘 Могу ли я купить доступ и использовать его с друзьями ? - Нет, один доступ в одни руки.\n\n" 
    "🔘 Могу ли я зайти с MacBook? - Да, вы сможете пользоваться сервисом, под любыми операционными системами.\n\n" 
    "🔘 Как мне понять, что вы меня не обманите? - По вашему запросу мы предоставим вам видео ОПЛАЧЕННОГО ТАРИФА ПРОФЕССИОНАЛЬНЫЙ с датой и временем \n\n" 
    "🔘 Какая механика захода в сервис? - Вход по ссылке через любой браузер",reply_markup=kb.about_sklad_kb)


@dp.message_handler(lambda message: message.text == "Чат и отзывы👥")
async def about(message: types.Message):
    photo = InputFile('D:/Downloads/PYTHON/telebot/handlers/users/bot_photo.jpg')
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    await message.answer('Для перехода в нужный раздел нажмите соответствующую кнопку:', reply_markup=kb.chat_and_reviews_kb)


@dp.message_handler(lambda message: message.text == "В Топе на маркетплейс 8.0🔥")
async def top(message: types.Message):
    photo = InputFile('D:/Downloads/PYTHON/telebot/handlers/users/top.jpg')
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    await message.answer("Дорогие участники!\n\n"
"Курс Лео Шевченко 8.0 куплен.✅\n\n"
"Старт: 25.02.2022\n\n"
"Длительность: 30 дней\n\n"
"Тариф: ULTIMATE 🔥\n\n\n"
"9 основных модулей:\n\n"
"МОДУЛЬ 0✅ - ПРИНИМАЕМ ПРАВИЛА ИГРЫ И СМОТРИМ В БУДУЩЕЕ\n\n"
"МОДУЛЬ 1✅ - КАК ПОПАСТЬ В ТОП\n\n"
"МОДУЛЬ 2✅ - СОЗДАЕМ ТОПОВЫЙ КОНТЕНТ"
"МОДУЛЬ 3✅ - ВЫВОДИМ ТОВАРЫ В ТОП\n\n"
"МОДУЛЬ 4✅ - ПРОДВИЖЕНИЕ ТОВАРА\n\n"
"МОДУЛЬ 5✅ - РЕПУТАЦИЯ БРЕНДА КАК СПОСОБ ПРОДВИЖЕНИЯ\n\n"
"МОДУЛЬ 6✅ - ДОПОЛНИТЕЛЬНЫЕ ИНСТРУМЕНТЫ ДЛЯ ПОВЫШЕНИЯ ПРИБЫЛИ\n\n"
"МОДУЛЬ 7✅ - ЗАКУПАЙ КАК ПРОФИ\n\n"
"МОДУЛЬ 8✅ - OZON ТОЖЕ КАЧНЕМ\n\n"
"МОДУЛЬ 9✅ - СИСТЕМАТИЗАЦИЯ БИЗНЕСА И УПРАВЛЕНИЕ КОМАНДОЙ\n\n"
"+ Созвоны по ZOOM\n\n"
"Стоимость курса - 3500₽", reply_markup=kb.top_at_kb)


@dp.message_handler(lambda message: message.text == "Тотальное доминирование на МП🦾🔝")
async def top(message: types.Message):
    photo = InputFile('D:/Downloads/PYTHON/telebot/handlers/users/total_dom.jpg')
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    await message.answer("Дорогие участники!\n\n"
"Вы можете приобрести:\n"
"Курс 'Тотальное доминирование на маркетплейсах'\n\n" 
"Содержание:\n\n"
"МОДУЛЬ 0✅ - Подготовка к курсу\n\n"
"МОДУЛЬ 1✅ - Как выбрать товар который будет продаваться\n\n"
"МОДУЛЬ 2✅ - Инвестиции и старт бизнеса\n\n"
"МОДУЛЬ 3✅ - Оформление и подготовка к первой поставке на маркетплейсе\n\n"
"МОДУЛЬ 4✅ - Дизайн и оформление карточки\n\n"
"МОДУЛЬ 5✅ - Продвижение товара\n\n"
"МОДУЛЬ 6✅ - Аналитика\n\n"
"МОДУЛЬ 7✅ - Команда\n\n"
"МОДУЛЬ 8✅ - Автоматизация бизнеса\n\n"
"МОДУЛЬ 9✅ - Построение бренда\n\n"
"МОДУЛЬ 10✅ - Продажа бизнеса\n\n\n"
"🔸общие групповые созвоны\n"
"🔸сео оптимизация от Павла Шевченко\n"
"🔸итоговое мероприятие, контакты", reply_markup=kb.total_dom_kb)


@dp.message_handler(lambda message: message.text == "Мне нужна помощь🙋‍♂")
async def top(message: types.Message):
    photo = InputFile('D:/Downloads/PYTHON/telebot/handlers/users/total_dom.jpg')
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    await message.answer('Вы можете написать администратору либо обратиться с вопросом в чат складчины:', reply_markup=kb.tp_kb)


@dp.message_handler(lambda message: message.text == "Главное меню🗂")
async def main_menu(message: types.Message):
    photo = InputFile('D:/Downloads/PYTHON/telebot/handlers/users/total_dom.jpg')
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    await message.answer(f"Привет, Denis! Рады вас видеть😊 \n \n С помощью этого бота вы сможете получить доступ к сервису аналитики для маркетплейсов, который подходит именно вам.",reply_markup=kb.start_kb)
