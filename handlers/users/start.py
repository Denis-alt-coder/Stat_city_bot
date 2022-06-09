from aiogram import types
from aiogram.types import InputFile
from aiogram.dispatcher.filters.state import State, StatesGroup
from loader import dp, bot
from . import start_keyboard as kb


class FSMProf(StatesGroup):
    prof_pay_and_get = State()
    prof_pay = State()
    prof_any_card = State()
    prof_tinkoff_sbor = State()
    pay_2800_any = State()
    pay_2800_sbor = State()

class FSMPrem(StatesGroup):
    prem_pay_and_get = State()
    prem_pay = State()
    prem_any_card = State()
    prem_tinkoff_sbor = State()
    pay_2800_any = State()
    pay_2800_sbor = State()

class FSMComposite(StatesGroup):
    composite_pay_and_get = State()
    composite_pay = State()
    composite_any_card = State()
    composite_tinkoff_sbor = State()
    pay_2500_any = State()
    pay_2500_sbor = State()

class FSMTop(StatesGroup):
    top_pay_and_get = State()
    top_pay = State()
    top_any_card = State()
    top_tinkoff_sbor = State()
    pay_3500_any = State()
    pay_3500_sbor = State()

class FSMTotalDom(StatesGroup):
    total_dom_pay_and_get = State()
    total_dom_pay = State()
    total_dom_any_card = State()
    total_dom_tinkoff_sbor = State()
    pay_4000_any = State()
    pay_4000_sbor = State()

@dp.message_handler(commands=['start'])
async def bot_start(message: types.Message):
    photo = InputFile('D:/Downloads/PYTHON/telebot/handlers/users/bot_photo.jpg')
    await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    await message.answer(
        f"Привет, {message.from_user.full_name} Рады вас видеть😊 \n \n С помощью этого бота вы сможете получить доступ к сервису аналитики для маркетплейсов, который подходит именно вам.",
        reply_markup=kb.start_kb)


@dp.message_handler(lambda message: message.text == "Выбрать сервис аналитики📊")
async def tarifs(message: types.Message):
    photo = InputFile('D:/Downloads/PYTHON/telebot/handlers/users/bot_photo.jpg')
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    await message.answer('Выберите интересующий вас сервис из доступных на данный момент:', reply_markup=kb.analitic_kb)


@dp.message_handler(lambda message: message.text == "О складчине💭")
async def about(message: types.Message):
    photo = InputFile('D:/Downloads/PYTHON/telebot/handlers/users/bot_photo.jpg')
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    await message.answer('Что такое «складчина»?\n\n'
                         "Складчина - совместная покупка доступа к тому или иному онлайн продукты (в нашем случае). Таким образом каждый человек может пользоваться полноценным функционалом сервисов за доступные средства.\n\n"
                         "Например, 10 человек хотят купить MPstats за 28.000 рублей, то каждому из них нужно скинуться примерно по 2800 рублей.\n\n"
                         "🔘 Есть ли график пользования или очередь ? - графика и очередей НЕТ, заходите и пользуетесь полным функционалом, когда вам удобно.\n\n"
                         "🔘 Могу ли я подвязать свой личный кабинет WB через API в аккаунт мпстат ? - Да, вы можете это сделать.\n\n"
                         "🔘 Через какой браузер предоставляется доступ в аккаунт - Любой, который удобен вам.\n\n"
                         "🔘 Могу ли я купить доступ и использовать его с друзьями ? - Нет, один доступ в одни руки.\n\n"
                         "🔘 Могу ли я зайти с MacBook? - Да, вы сможете пользоваться сервисом, под любыми операционными системами.\n\n"
                         "🔘 Как мне понять, что вы меня не обманите? - По вашему запросу мы предоставим вам видео ОПЛАЧЕННОГО ТАРИФА ПРОФЕССИОНАЛЬНЫЙ с датой и временем \n\n"
                         "🔘 Какая механика захода в сервис? - Вход по ссылке через любой браузер",
                         reply_markup=kb.about_sklad_kb)


@dp.message_handler(lambda message: message.text == "Чат и отзывы👥")
async def about(message: types.Message):
    photo = InputFile('D:/Downloads/PYTHON/telebot/handlers/users/bot_photo.jpg')
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    await message.answer('Для перехода в нужный раздел нажмите соответствующую кнопку:',
                         reply_markup=kb.chat_and_reviews_kb)


@dp.message_handler(lambda message: message.text == "В Топе на маркетплейс 8.0🔥", state=FSMTop.top_pay_and_get)
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
                         "Стоимость курса - 3500₽", reply_markup=kb.top_pay_and_get_kb)
    await FSMTop.next()


@dp.message_handler(lambda message: message.text == "Оплатить и получить доступ✅", state=FSMTop.top_pay)
async def top_any_card(message: types.Message):
    photo = InputFile('D:/Downloads/PYTHON/telebot/handlers/users/payments.jpg')
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    await message.reply('Выберите способ оплаты:', reply_markup=kb.top_pay_kb)


@dp.message_handler(lambda message: message.text == "Любой картой✅", state=FSMTop.top_any_card)
async def top_any_card(message: types.Message):
    await message.reply('Вы производите оплату курса Лео Шевченко 8.0', reply_markup=kb.pay_3500_kb)
    await FSMTop.next()


@dp.message_handler(lambda message: message.text == "Тинькофф Сбор☑", state=FSMTop.top_any_card)
async def top_any_card(message: types.Message):
    photo = InputFile('D:/Downloads/PYTHON/telebot/handlers/users/payments.jpg')
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    await message.reply('Вы производите оплату курса Лео Шевченко 8.0\n\n'
'🚫Обязательно указать комментарий: на путешествие, на отдых\n\n' 
'❗️После оплаты отправьте скрин чека нам в личные сообщения 👇️\n\n'
'По всем вопросам: @AndreasBel_admin)\n\n', reply_markup=kb.pay_3500_kb)
    await FSMTop.next()
    await FSMTop.next()


@dp.message_handler(lambda message: message.text == "Оплатить 3500₽", state=FSMTop.pay_3500_any)
async def top_any_card(message: types.Message):
    photo = InputFile('D:/Downloads/PYTHON/telebot/handlers/users/payments.jpg')
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    await message.reply('<a href= https://clicks.su/mVejzQ>Any card</a>', parse_mode='HTML')


@dp.message_handler(lambda message: message.text == "Оплатить 3500₽", state=FSMTop.pay_3500_sbor)
async def top_any_card(message: types.Message):
    photo = InputFile('D:/Downloads/PYTHON/telebot/handlers/users/payments.jpg')
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    await message.reply('<a href= https://clicks.su/yRjNAy>Tinkoff Sbor</a>', parse_mode='HTML')


@dp.message_handler(lambda message: message.text == "Тотальное доминирование на МП🦾🔝", state=FSMTotalDom.total_dom_pay_and_get)
async def total_dom(message: types.Message):
    photo = InputFile('D:/Downloads/PYTHON/telebot/handlers/users/total_dom.jpg')
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    await message.answer("Дорогие участники!\n\n"
                         "Вы можете приобрести:\n"
                         'Курс "Тотальное доминирование на маркетплейсах"\n\n'
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
                         "🔸итоговое мероприятие, контакты", reply_markup=kb.total_dom_pay_and_get_kb)
    await FSMTotalDom.next()


@dp.message_handler(lambda message: message.text == "Оплатить и получить доступ✅", state=FSMTotalDom.total_dom_pay)
async def top_any_card(message: types.Message):
    photo = InputFile('D:/Downloads/PYTHON/telebot/handlers/users/payments.jpg')
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    await message.reply('Выберите способ оплаты:', reply_markup=kb.total_dom_pay_kb)


@dp.message_handler(lambda message: message.text == "Любой картой✅", state=FSMTotalDom.total_dom_any_card)
async def top_any_card(message: types.Message):
    photo = InputFile('D:/Downloads/PYTHON/telebot/handlers/users/payments.jpg')
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    await message.reply('Вы производите оплату курса "Тотальное доминирование на маркетплейсах".', reply_markup=kb.pay_4000_kb)
    await FSMTotalDom.next()


@dp.message_handler(lambda message: message.text == "Тинькофф Сбор☑", state=FSMTotalDom.total_dom_tinkoff_sbor)
async def top_any_card(message: types.Message):
    photo = InputFile('D:/Downloads/PYTHON/telebot/handlers/users/payments.jpg')
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    await message.reply('Вы производите оплату курса "Тотальное доминирование на маркетплейсах".\n\n'
'🚫Обязательно указать комментарий: на путешествие, на отдых\n\n' 
'❗️После оплаты отправьте скрин чека нам в личные сообщения 👇️\n\n'
'По всем вопросам: @AndreasBel_admin)\n\n', reply_markup=kb.pay_4000_kb)
    await FSMTotalDom.next()
    await FSMTotalDom.next()


@dp.message_handler(lambda message: message.text == "Оплатить 4000₽", state=FSMTotalDom.pay_4000_any)
async def top_any_card(message: types.Message):
    photo = InputFile('D:/Downloads/PYTHON/telebot/handlers/users/payments.jpg')
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    await message.reply('<a href= https://clicks.su/yoJ7R0>Any card</a>', parse_mode='HTML')


@dp.message_handler(lambda message: message.text == "Оплатить 4000₽", state=FSMTotalDom.pay_4000_sbor)
async def top_any_card(message: types.Message):
    photo = InputFile('D:/Downloads/PYTHON/telebot/handlers/users/payments.jpg')
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    await message.reply('<a href= https://clicks.su/yM5vEy>Tinkoff Sbor</a>', parse_mode='HTML')


@dp.message_handler(lambda message: message.text == "Обратится в поддержку✍")
async def top(message: types.Message):
    photo = InputFile('D:/Downloads/PYTHON/telebot/handlers/users/bot_photo.jpg')
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    await message.answer('Вы можете написать администратору либо обратиться с вопросом в чат складчины:',
                         reply_markup=kb.tp_kb)


@dp.message_handler(lambda message: message.text == "MPstats(Профессиональный)💹", state=FSMProf.prof_pay_and_get)
async def prof_tarif(message: types.Message):
    photo = InputFile('D:/Downloads/PYTHON/telebot/handlers/users/bot_photo.jpg')
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    await message.answer('Mpstats (Тариф "Профессиональный")🚀️\n\n\n'
                         '✔️ Тариф "Профессиональный"\n'
                         '✔️ Цена - 2800₽ в месяц / вместо 28.000₽\n'
                         '✔️ Никакого графика и очередей\n\n'
                         '(Окно выборки данных: 91 день)\n\n\n'
                         '✅Пользоваться можно без ограничений\n\n'
                         '✅Работает 24 часа в сутки\n\n'
                         '✅Отдельный закрытый чат для общения и поддержки по MPstats\n\n\n'
                         '❗️Вам будет выдан личный логин и пароль, благодаря такой системе входа вы не будете вылетать и полноценно сможете пользоваться сервисом.\n\n'
                         'После оплаты с вами свяжется менеджер и проведет проверку на подставного покупателя, это происходит быстро. 😊\n\n\n'
                         "💥Новый метод входа в WEB MPSTATS !\n\n"
                         "🔸НЕ ВЫЛЕТАЕТ ИЗ МПСТАТ\n\n "
                         '🔸Работает плагин мпстат c кнопой "Открыть в MPstats"\n\n'
                         "🔸Можете добавить свой Api ключ из Wildberries\n\n "
                         "🔸Без очередей и с удобного вам браузера и устройства Macbook, IPhone, Windows, Android\n\n "
                         "🔸Не нужно скачивать никаких программ и прочих некомфортных действий",
                         reply_markup=kb.prof_pay_and_get_kb)
    await FSMProf.next()


@dp.message_handler(lambda message: message.text == "Оплатить и получить доступ✅", state=FSMProf.prof_pay)
async def top_any_card(message: types.Message):
    photo = InputFile('D:/Downloads/PYTHON/telebot/handlers/users/payments.jpg')
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    await message.reply('Выберите способ оплаты:', reply_markup=kb.prof_pay_kb)
    await FSMProf.next()


@dp.message_handler(lambda message: message.text == "Любой картой✅", state=FSMProf.prof_any_card)
async def top_any_card(message: types.Message):
    photo = InputFile('D:/Downloads/PYTHON/telebot/handlers/users/payments.jpg')
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    await message.reply('Вы производите оплату доступа к сервису Mpstats (Тариф "Профессиональный") на 30 дней.', reply_markup=kb.prof_pay_2800_kb)
    await FSMProf.next()


@dp.message_handler(lambda message: message.text == "Тинькофф Сбор☑", state=FSMProf.prof_tinkoff_sbor)
async def top_any_card(message: types.Message):
    photo = InputFile('D:/Downloads/PYTHON/telebot/handlers/users/payments.jpg')
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    await message.reply('Вы производите оплату доступа к сервису Mpstats (Тариф "Профессиональный") на 30 дней."\n\n'
'🚫Обязательно указать комментарий: на путешествие, на отдых\n\n' 
'❗️После оплаты отправьте скрин чека нам в личные сообщения 👇️\n\n'
'По всем вопросам: @AndreasBel_admin)\n\n', reply_markup=kb.prof_pay_2800_kb)
    await FSMProf.next()
    await FSMProf.next()


@dp.message_handler(lambda message: message.text == "Оплатить 2800₽", state=FSMProf.pay_2800_any)
async def top_any_card(message: types.Message):
    photo = InputFile('D:/Downloads/PYTHON/telebot/handlers/users/payments.jpg')
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    await message.reply('<a href= https://clicks.su/mjqPMX>Any card</a>', parse_mode='HTML')


@dp.message_handler(lambda message: message.text == "Оплатить 2800₽", state=FSMProf.pay_2800_sbor)
async def top_any_card(message: types.Message):
    photo = InputFile('D:/Downloads/PYTHON/telebot/handlers/users/payments.jpg')
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    await message.reply('<a href= https://clicks.su/9qGqRg>Tinkoff Sbor</a>', parse_mode='HTML')


@dp.message_handler(lambda message: message.text == "Moneyplace(Premium)📈", state=FSMPrem.prem_pay_and_get)
async def prem_tarif(message: types.Message):
    photo = InputFile('D:/Downloads/PYTHON/telebot/handlers/users/bot_photo.jpg')
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    await message.answer('Moneyplace (Тариф "Premium") 🚀\n\n'
                         '✔️ Тариф "Premium"\n'
                         '✔️ Цена - 2800р в месяц\n\n'
                         '✔️ Никакого графика и очередей\n\n\n'
                         '✅Пользоваться можно без ограничений\n\n'
                         '✅Работает 24 часа в сутки\n\n'
                         '✅Отдельный закрытый чат для общения и поддержки по Moneyplace\n\n\n'
                         '❗️Вам будет выдан личный логин и пароль, благодаря такой системе входа вы не будете вылетать и полноценно сможете пользоваться сервисом.\n\n'
                         'После оплаты с вами свяжется менеджер и проведет проверку на подставного покупателя, это происходит быстро. 😊\n\n\n'
                         '💥Новый метод входа в WEB MONEYPLACE !\n\n'
                         '🔸НЕ ВЫЛЕТАЕТ ИЗ MONEYPLACE\n\n'
                         '🔸Можете добавить свой Api ключ из Wildberries\n\n'
                         '🔸Без очередей и с удобного вам браузера и устройства Macbook, IPhone, Windows, Android\n\n'
                         '🔸Не нужно скачивать никаких программ и прочих некомфортных действий\n\n'
                         '🔸Наша команда гарантирует помощь при любых проблемах', reply_markup=kb.prem_pay_and_get_kb)


@dp.message_handler(lambda message: message.text == "Оплатить и получить доступ✅", state=FSMPrem.prem_pay)
async def top_any_card(message: types.Message):
    photo = InputFile('D:/Downloads/PYTHON/telebot/handlers/users/payments.jpg')
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    await message.reply('Выберите способ оплаты:', reply_markup=kb.prem_pay_kb)
    await FSMPrem.next()


@dp.message_handler(lambda message: message.text == "Любой картой✅", state=FSMPrem.prem_any_card)
async def top_any_card(message: types.Message):
    photo = InputFile('D:/Downloads/PYTHON/telebot/handlers/users/payments.jpg')
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    await message.reply('Вы производите оплату доступа к сервису Moneyplace (Тариф "Premium") на 30 дней.', reply_markup=kb.prem_pay_2800_kb)
    await FSMProf.next()


@dp.message_handler(lambda message: message.text == "Тинькофф Сбор☑", state=FSMPrem.prem_tinkoff_sbor)
async def top_any_card(message: types.Message):
    photo = InputFile('D:/Downloads/PYTHON/telebot/handlers/users/payments.jpg')
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    await message.reply('Вы производите оплату доступа к сервису Moneyplace (Тариф "Premium") на 30 дней."\n\n'
'🚫Обязательно указать комментарий: на путешествие, на отдых\n\n' 
'❗️После оплаты отправьте скрин чека нам в личные сообщения 👇️\n\n'
'По всем вопросам: @AndreasBel_admin)\n\n', reply_markup=kb.prem_pay_2800_kb)
    await FSMPrem.next()
    await FSMPrem.next()


@dp.message_handler(lambda message: message.text == "Оплатить 2800₽", state=FSMPrem.pay_2800_any)
async def top_any_card(message: types.Message):
    photo = InputFile('D:/Downloads/PYTHON/telebot/handlers/users/payments.jpg')
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    await message.reply('<a href= https://clicks.su/mjqPMX>Any card</a>', parse_mode='HTML')


@dp.message_handler(lambda message: message.text == "Оплатить 2800₽", state=FSMPrem.pay_2800_sbor)
async def top_any_card(message: types.Message):
    photo = InputFile('D:/Downloads/PYTHON/telebot/handlers/users/payments.jpg')
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    await message.reply('<a href= https://clicks.su/9qGqRg>Tinkoff Sbor</a>', parse_mode='HTML')


@dp.message_handler(lambda message: message.text == "MarketGuru(Комбинированый)📉", state=FSMPrem.prem_pay_and_get)
async def composite_tarif(message: types.Message):
    photo = InputFile('D:/Downloads/PYTHON/telebot/handlers/users/bot_photo.jpg')
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    await message.answer('Личный аккаунт MarketGuru по стоимости 2500₽ (вместо 12700₽)\n\n'
                         '✔️ Тариф "Комбинированный"\n'
                         '✔️ Цена - 2500₽ в месяц / вместо 12700₽\n'
                         '✔️ Личный аккаунт в 1 руки (полный доступ)\n\n'
                         '✅Пользоваться можно без ограничений\n\n'
                         '✅Переходите на сайт Marketguru.ru и вводите логин и пароль\n\n'
                         '✅Отдельный закрытый чат для общения\n\n'
                         '❗️Вам будет выдан личный логин и пароль, благодаря такой системе входа вы не будете вылетать и полноценно сможете пользоваться сервисом.\n\n'
                         'После оплаты с вами свяжется менеджер и проведет проверку на подставного покупателя, это происходит быстро. 😊',
                         reply_markup=kb.composite_pay_and_get_kb)


@dp.message_handler(lambda message: message.text == "Оплатить и получить доступ✅", state=FSMComposite.composite_pay)
async def top_any_card(message: types.Message):
    photo = InputFile('D:/Downloads/PYTHON/telebot/handlers/users/payments.jpg')
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    await message.reply('Выберите способ оплаты:', reply_markup=kb.composite_pay_kb)
    await FSMComposite.next()


@dp.message_handler(lambda message: message.text == "Любой картой✅", state=FSMComposite.composite_any_card)
async def top_any_card(message: types.Message):
    photo = InputFile('D:/Downloads/PYTHON/telebot/handlers/users/payments.jpg')
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    await message.reply('Вы производите оплату доступа к сервису MarketGuru (Тариф "Комбинированный") на 30 дней.', reply_markup=kb.pay_2500_kb)
    await FSMComposite.next()


@dp.message_handler(lambda message: message.text == "Тинькофф Сбор☑", state=FSMComposite.composite_tinkoff_sbor)
async def top_any_card(message: types.Message):
    photo = InputFile('D:/Downloads/PYTHON/telebot/handlers/users/payments.jpg')
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    await message.reply('Вы производите оплату доступа к сервису MarketGuru (Тариф "Комбинированный") на 30 дней."\n\n'
'🚫Обязательно указать комментарий: на путешествие, на отдых\n\n' 
'❗️После оплаты отправьте скрин чека нам в личные сообщения 👇️\n\n'
'По всем вопросам: @AndreasBel_admin)\n\n', reply_markup=kb.pay_2500_kb)
    await FSMComposite.next()
    await FSMComposite.next()


@dp.message_handler(lambda message: message.text == "Оплатить 2500₽", state=FSMComposite.pay_2500_any)
async def top_any_card(message: types.Message):
    photo = InputFile('D:/Downloads/PYTHON/telebot/handlers/users/payments.jpg')
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    await message.reply('<a href= https://clicks.su/gx7zL1>Any card</a>', parse_mode='HTML')


@dp.message_handler(lambda message: message.text == "Оплатить 2500₽", state=FSMComposite.pay_2500_sbor)
async def top_any_card(message: types.Message):
    photo = InputFile('D:/Downloads/PYTHON/telebot/handlers/users/payments.jpg')
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    await message.reply('<a href= https://clicks.su/9qGqRg>Tinkoff Sbor</a>', parse_mode='HTML')


@dp.message_handler(lambda message: message.text == "Чат👥")
async def about(message: types.Message):
    photo = InputFile('D:/Downloads/PYTHON/telebot/handlers/users/bot_photo.jpg')
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    await message.reply('<a href= https://clicks.su/ydaaKg>Chat</a>', parse_mode='HTML')


@dp.message_handler(lambda message: message.text == "Написать в тех.поддержку✍")
async def about(message: types.Message):
    photo = InputFile('D:/Downloads/PYTHON/telebot/handlers/users/bot_photo.jpg')
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    await message.reply('<a href= https://clicks.su/yYllW9>Help</a>', parse_mode='HTML')