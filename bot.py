import telebot
from telebot import types
from math import sqrt
bot = telebot.TeleBot("945523593:AAHo-tnht2m8i_-lR7qMQtxe_Dl6MOhwmG8")
words = {
"why": ["почему", "почему?"],
"hello": ["привет", "хай", "хей", "здравствуй", "здравствуйте", "здарова"],
"creators": ["создатели", "разработчики", "создатель", "разработчик"]
}
@bot.message_handler(content_types = ["text"])
def hello(message):
	i = 0
	if message.text.lower() == "/start":
		i = 1
		bot.send_message(message.from_user.id, "Привет)")
		keyboard1 = types.InlineKeyboardMarkup()
		yes_key = types.InlineKeyboardButton(text = "Ага", callback_data = "yes")
		no_key = types.InlineKeyboardButton(text = "Не-а", callback_data = "no")
		keyboard1.add(yes_key, no_key)
		bot.send_message(message.from_user.id, "Хочешь пройти квест?", reply_markup = keyboard1)
	elif i == 0:
		bot.send_message(message.from_user.id, "Я не понимать ;(")
	for word in words["hello"]:
		if message.text.lower() == word:
			i = 1
			bot.send_message(message.from_user.id, "Привет)")
			keyboard1 = types.InlineKeyboardMarkup()
			yes_key = types.InlineKeyboardButton(text = "Ага", callback_data = "yes")
			no_key = types.InlineKeyboardButton(text = "Не-а", callback_data = "no")
			keyboard1.add(yes_key, no_key)
			bot.send_message(message.from_user.id, "Хочешь пройти квест?", reply_markup = keyboard1)
	for word in words["creators"]:
		if message.text.lower() == word:
			i = 1
			bot.send_message(message.from_user.id, "https://t.me/alextyn\nhttps://t.me/SlavaRusWarrior")
	for word in words["why"]:
		if message.text.lower() == word:
			i = 1
			bot.send_message(message.from_user.id, "Ну а хле")
	if message.text.lower() == "жизнь":
			i = 1
			bot.send_message(message.from_user.id, "- боль")
@bot.callback_query_handler(func= lambda call: True)
def callback_worker(call):
	if call.data == "yes":
		keyboard2 = types.InlineKeyboardMarkup()
		city1_key = types.InlineKeyboardButton(text = "Осинники", callback_data = "Osinniki")
		city2_key = types.InlineKeyboardButton(text = "Новокузнецк", callback_data = "Novokuznetsk")
		city3_key = types.InlineKeyboardButton(text = "Кемерово", callback_data = "Kemerovo")
		city4_key = types.InlineKeyboardButton(text = "???", callback_data = "a")
		keyboard2.add(city1_key, city2_key, city3_key, city4_key)
		bot.send_message(call.message.chat.id, "Тогда выбери свой город из списка", reply_markup = keyboard2)
	elif call.data == "no":
		bot.send_message(call.message.chat.id, 'Возвращайся, когда будешь готов :D')
	elif call.data == "Osinniki":
		bot.answer_callback_query(call.id, text = "Город выбран")
		keyboard = types.ReplyKeyboardMarkup(True)
		button_geo = types.KeyboardButton(text="Отправить местоположение", request_location=True)
		keyboard.add(button_geo)
		bot.send_message(call.message.chat.id, "Нажми на кнопку, чтоб я нашел ближайшую контрольную точку :D", reply_markup=keyboard)
	elif call.data == "Novokuznetsk":
		bot.answer_callback_query(call.id, text = "Город выбран")
		bot.send_message(call.message.chat.id, "Coming soon..")
	elif call.data == "Kemerovo":
		bot.answer_callback_query(call.id, text = "Город выбран")
		bot.send_message(call.message.chat.id, "Coming soon..")
	elif call.data == "a":
		bot.answer_callback_query(call.id, text = "Город выбран")
		bot.send_message(call.message.chat.id, "Coming soon..")
@bot.message_handler(content_types=["location"])
def location(message):
	osinniki = [53.577475, 53.658998, 87.277901, 87.451449]
	lenin = [53.598598, 87.338041]
	lion = [53.598330, 87.330634]
	pandf = [53.600084, 87.337079]
	if osinniki[0] < message.location.latitude and message.location.latitude < osinniki[1] and osinniki[2] < message.location.longitude and message.location.longitude < osinniki[3]:
		latitude1 = abs(lenin[0] - message.location.latitude) * 111135
		latitude2 = abs(lion[0] - message.location.latitude) * 111135
		latitude3 = abs(pandf[0] - message.location.latitude) * 111135
		longitude1 = abs(lenin[1] - message.location.longitude) * 111321
		longitude2 = abs(lion[1] - message.location.longitude) * 111321
		longitude3 = abs(pandf[1] - message.location.longitude) * 111321
		distance1 = round(sqrt(latitude1**2 + longitude1**2))
		distance2 = round(sqrt(latitude2**2 + longitude2**2))
		distance3 = round(sqrt(latitude3**2 + longitude3**2))
		if distance1 < 20:
			bot.send_message(message.from_user.id, "Отлично!\nТы дошёл до Памятника В.И.Ленину :D")
			keyboard3 = types.InlineKeyboardMarkup()
			url_button = types.InlineKeyboardButton(text="Получить", url="https://t.me/addstickers/membitch")
			keyboard3.add(url_button)
			bot.send_message(message.from_user.id, "Твой приз - 1 часть нашего набора стикеров🎉", reply_markup=keyboard3)
			bot.send_message(message.from_user.id, "✅Памятник В.И.Ленину - " + str(distance1) + " м" + "\nФонтан \"Лев\" - " + str(distance2) + " м" + "\nПамятник Петру и Февронии - " + str(distance3) + " м")
			bot.send_message(message.from_user.id, "Продолжай путь, чтобы собрать весь стикерпак :3")
		elif distance2 < 20:
			bot.send_message(message.from_user.id, "Отлично!\nТы около Фонтана \"Лев\" :D")
			keyboard3 = types.InlineKeyboardMarkup()
			url_button = types.InlineKeyboardButton(text="Получить", url="https://t.me/addstickers/PresidentPutin")
			keyboard3.add(url_button)
			bot.send_message(message.from_user.id, "Твой приз - 2 часть нашего набора стикеров🎉", reply_markup=keyboard3)
			bot.send_message(message.from_user.id, "Памятник В.И.Ленину - " + str(distance1) + " м" + "\n✅Фонтан \"Лев\" - " + str(distance2) + " м" + "\nПамятник Петру и Февронии - " + str(distance3) + " м")
			bot.send_message(message.from_user.id, "Продолжай путь, чтобы собрать весь стикерпак :3")
		elif distance3 < 20:
			bot.send_message(message.from_user.id, "Отлично!\nТы находишься около Памятника Петру и Февронии 👌")
			keyboard3 = types.InlineKeyboardMarkup()
			url_button = types.InlineKeyboardButton(text="Получить", url="https://t.me/addstickers/HotCherry")
			keyboard3.add(url_button)
			bot.send_message(message.from_user.id, "Твой приз - 3 часть нашего набора стикеров🎉", reply_markup=keyboard3)
			bot.send_message(message.from_user.id, "Буду благодарен, если ты расскажешь о квесте своим друзьям😃")
			bot.send_message(message.from_user.id, "Мои создатели😊\nhttps://t.me/alextyn\nhttps://t.me/SlavaRusWarrior")
			bot.send_message(message.from_user.id, "Памятник В.И.Ленину - " + str(distance1) + " м" + "\nФонтан \"Лев\" - " + str(distance2) + " м" + "\n✅Памятник Петру и Февронии - " + str(distance3) + " м")
			bot.send_message(message.from_user.id, "Продолжай путь, чтобы собрать весь стикерпак :3")
		else:
			bot.send_message(message.from_user.id, "Достопримечательности вашего города и расстояния до них.\n\nПамятник В.И.Ленину - " + str(distance1) + " м" + "\nФонтан \"Лев\" - " + str(distance2) + " м" + "\nПамятник Петру и Февронии - " + str(distance3) + " м")
			keyboard = types.ReplyKeyboardMarkup(True, True)
			button_geo = types.KeyboardButton(text="Отправить местоположение", request_location=True)
			keyboard.add(button_geo)
			bot.send_message(message.from_user.id, "Когда будешь около достопримечательности, просто нажми на кнопку", reply_markup=keyboard)
	else:
		bot.send_message(message.from_user.id, "Прости, но я пока не знаю твоего города :(")
bot.polling()
