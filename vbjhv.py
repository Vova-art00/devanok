импортные запросы
импортировать ос
время импорта
из bs4 импортировать BeautifulSoup как BS

КРАСНЫЙ, БЕЛЫЙ, ГОЛУБОЙ, ЗЕЛЕНЫЙ, ПО УМОЛЧАНИЮ, ГОЛУБОЙ, ЖИРНЫЙ = '\033[91m', '\033[46m', '\033[36m', '\033[1;32m', '\033[0m', '\033[1;36m', '\033[1m'

определение get_html(url):
	вернуть запросы.получить(url).текст

def parse_ua(тутилка):
	суп = BS(tutilka, 'html.parser')
	для даты в soup.findAll('td'):
		содержимое = дата.getText().split(' ')
		для g в содержании:
			если г == '':
				проходить
			elif '\n' в g:
				г = г.заменить("\n", "")
			еще:
				print(f'{CYAN}[{RED}*{CYAN}] {GREEN}'+g)

печать(f'''{BOLD}\033[35м ░░░░░░░░▄███▄▄▄░░▄▄███▄ ░░░░░░░░░
    ░░░░░░░██████████████████░░░░░░░
    ░░░░░░░██████████████████░░░░░░░
    ░░░░░░░██████████████████░░░░░░░
    ░░░░░░░██████████████████░░░░░░░
    ██▄▄▄██▀▀▀▀██████████▀▀▀▀██▄▄▄██
    ░▀██████▄▄▄░░░░░░░░░░▄▄▄██████▀░
    ░░░▀████████████████████████▀░░░
    ░░▄█▀█▀▀▀▀████████████▀▀▀▀█▀█▄░░
    ░░█▀░▀░░░░░▄▄░░░░░░▄▄░░░░░▀░▀█░░                
    ░░█▄░░░░░░█░░█░░░░█░░█░░░░░░▄█░░
    ░░░▀██▄░░░░▀▀░░█░░░▀▀░░░░▄██▀░░░
    ░░░░░▀█▄░░░░░░░▀▀░░░░░░░▄█▀░░░░░
    ░░░░░░░██▄▄░░░████░░░▄▄██░░░░░░░
    ░░░░░▄███████▄▄▄▄▄▄███████▄░░░░░
    ░░░░▄██████████████████████▄░░░░
    ░░░▄████████████████████████▄░░░
    ░░▄██████████████████████████▄░░
    
1 - Поиск по Государственному Номеру Украины
2 - Поиск по номеру телефона
3 - Поиск информации по IP-адресу
4 - Поиск Торрентов по IP-Адресу
5 - Парсинг Прокси
6 - Поиск номеров по Авито
7 - BSSID
[{RED}*{CYAN}] Создано {RED}@tenych69{CYAN} Telegram: {RED}@termuxmam (Подписаться) {CYAN}
''')

в то время как Истина:
	shell = input(f'{CYAN}[{RED}*{CYAN}] Выберите число: {GREEN}')
	если оболочка == '1':
		num = input(f'{CYAN}[{RED}*{CYAN}] Номер автомобиля: {GREEN}')
		parse_ua(get_html('https://baza-gai.com.ua/nomer/' + num))
	оболочка elif == '2':
		phone = input(f'{CYAN}[{RED}*{CYAN}] Номер телефона: {GREEN}')
		пытаться:
			ответ = запросы.получить('https://htmlweb.ru/geo/api.php?json&telcod=' + телефон)
			данные = ответ.json()
			user_country = data[ 'страна' ][ 'английский' ]
			user_id = данные[ 'страна' ][ 'id' ]
			user_location = данные[ 'страна' ][ 'местоположение' ]
			user_city = data[ 'столица' ][ 'английский' ]
			user_lat = data[ 'столица' ][ 'широта' ]
			user_log = data[ 'столица' ][ 'долгота' ]
			user_post = data[ 'capital' ][ 'post' ]
			user_oper = данные[ '0' ][ 'oper' ]
			uty = requests.get("https://api.whatsapp.com/send?phone="+phone)
			если uty.status_code==200:
				utl2 = "https://api.whatsapp.com/send?phone="+телефон
			еще:
				utl2 = 'Не найдено!'
			userr_all_info = f'{CYAN}[{RED}*{CYAN}] Страна: {GREEN}{str(user_country)}\n{CYAN}[{RED}*{CYAN}] ID: {GREEN}{str(user_id)}\n{CYAN}[{RED}*{CYAN}] Местоположение: {GREEN}{str(user_location)}\n{CYAN}[{RED}*{CYAN}] Город: {GREEN}{str(user_city)}\n{CYAN}[{RED}*{CYAN}] Широта: {GREEN}{str(user_lat)}\n{CYAN}[{RED}*{CYAN}] Долгота:{GREEN} {str(user_log)}\n{CYAN}[{RED}*{CYAN}] Индекс записи:{GREEN} {str(user_post)}\n{CYAN}[{RED}*{CYAN}] Оператор:{ЗЕЛЕНЫЙ} {str(user_oper)}'
			num_name = []
			phone_ow = requests.get(f'https://phonebook.space/?number=%2B{phone}').text
			содержимое = BS(phone_ow, 'html.parser').find('div', class_='results')
			для i в content.find_all('li'):
				num_name.append(i.text.strip())
			имя = ', '.join(num_name)
			user_all_info = f"""
\033[35m-===[Информация об операторе]===-
{userr_all_info}
\033[35м-===[Социальные сети]===-
{CYAN}[{RED}*{CYAN}] WhatsApp: {GREEN}{utl2}
\033[35m-===[Персональная информация]===-
{CYAN}[{RED}*{CYAN}] Возможные названия: {GREEN}{name}
	"""
			печать(user_all_info)
		кроме:
			print(f'{CYAN}[{RED}-{CYAN}] Хуево написал, пиши правильно. ¯╲_(ツ)_/¯')
	оболочка элиф == '3':
		запрос = ввод(f'{CYAN}[{RED}*{CYAN}] IP для сканирования: {GREEN}')
		пытаться:
			r = запросы.get(f'http://ip-api.com/json/{query}').json()
			print(f'{CYAN}[{RED}*{CYAN}] Страна:{GREEN} {r["country"]}\n{CYAN}[{RED}*{CYAN}] Код страны:{GREEN} {r["countryCode"]}\n{CYAN}[{RED}*{CYAN}] Регион:{GREEN} {r["region"]}\n{CYAN}[{RED}*{CYAN}] Название региона:{GREEN} {r["regionName"]}\n{CYAN}[{RED}*{CYAN}] Город: {GREEN}{r["city"]}\n{CYAN}[{RED}*{CYAN}] Почтовый индекс:{GREEN} {r["zip"]}\n{CYAN}[{RED}*{CYAN}] Латинская: {GREEN}{r["lat"]}\n{CYAN}[{RED}*{CYAN}] Долгота: {GREEN}{r["lon"]}\n{CYAN}[{RED}*{CYAN}] Часовой пояс: {GREEN}{r["timezone"]}\n{CYAN}[{RED}*{CYAN}] Интернет-провайдер:{GREEN} {r["isp"]}\n{CYAN}[{RED}*{CYAN}] Орг:{GREEN} {r["org"]}\n{CYAN}[{RED}*{CYAN}] Как: {GREEN}{r["as"]} ')
		кроме:
			print(f'{CYAN}[{RED}-{CYAN}] Не найдено, либо ты гей :)')
	оболочка элиф == '4':
		запрос = ввод(f'{CYAN}[{RED}*{CYAN}] IP для сканирования: {GREEN}')
		target_ip = запрос
		пытаться:
			headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; ) AppleWebKit/537.36 (KHTML, как Gecko) Chrome/83.0.4086.0 Safari/537.36","Connection": "keep-alive","Host": "iknowwhatyoudownload.com","Referer": "https://iknowwhatyoudownload.com"}
			страница = запросы.get("https://iknowwhatyoudownload.com/ru/peer/?ip=" + target_ip, headers=заголовки)
			суп = BS(страница.контент, "html.парсер")
			таблица = суп.найти(класс_="таблица").найти("tbody")
			торренты = таблица.find_all("tr")
			для торрента в торрентах:
				первый, последний = torrent.find_all(class_="date-column")
				первый, последний = первый.текст, последний.текст
				категория = torrent.find(class_="category-column").text
				имя = torrent.find(class_="имя-столбца").текст.заменить("\n", '').заменить(' ', '')
				размер = torrent.find(class_="size-column").text
				print(f'{CYAN}[{RED}*{CYAN}] Использовано первый раз: {GREEN}{first}{CYAN}, использовано последний раз: {GREEN}{last}{CYAN}, тип торрента: {GREEN} {category}{CYAN}, название торента: {GREEN}{name}{CYAN}, размер торента: {GREEN}{size}{CYAN}\n')
		кроме:
			print(f'{CYAN}[{RED}-{CYAN}] Неизвестная ошибка ¯╲_(ツ)_/¯')
	оболочка elif == '5':
		res1 = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout=1000&country=all&anonymity=elite&ssl=yes')
		print(f'{CYAN}[{RED}*{CYAN}] Ваш прокси, ser:\n' + '\n'.join(res1.text.split('\r\n')))
	оболочка элиф == '6':
		телефон = ввод(f'{CYAN}[{RED}*{CYAN}] Номер телефона: {GREEN} ')
		пытаться:
			страница = запросы.получить('https://mirror.bullshit.agency/search_by_phone/'+phone)
			суп = BS(страница.текст, 'html.парсер')
			classsell=soup.find(class_='media-heading')
			namesell= суп.find_all('h4')
			для classsell в namesell:
				print(f"{CYAN}[{RED}*{CYAN}] Имя: {GREEN}", classsell.text)
			classtext = soup.find(class_='text-muted')
			имятекст = суп.найти_все('span')
			для classtext в nametext:
				print(f"{CYAN}[{RED}*{CYAN}] Адрес и данные:{GREEN} ", classtext.text)
		кроме:
			print(f'{CYAN}[{RED}-{CYAN}] Неизвестная ошибка ¯╲_(ツ)_/¯')
	оболочка элиф == '7':
		запрос = ввод(f'{CYAN}[{RED}*{CYAN}] BSSID: {GREEN} ')
		пытаться:
			ответ = запросы.get("https://api.mylnikov.org/geolocation/wifi?v=1.1&data=open&bssid=" + запрос)
			данные = ответ.json()
			статус = данные["результат"]
			если статус == 200:
				широта = данные["данные"]["широта"]
				lon = данные["данные"]["lon"]
				print(f'{CYAN}[{RED}*{CYAN}] Латинянка: {GREEN}{lat}{CYAN}\n{CYAN}[{RED}*{CYAN}] Долгота: {GREEN}{lon}')
			еще:
				errorCode = данные["сообщение"]
				errorMessage = данные["desc"]
				print(f'{CYAN}[{RED}*{CYAN}] Код ошибки: {GREEN}{errorCode}{CYAN}\n{CYAN}[{RED}*{CYAN}] Сообщение об ошибке: {GREEN}{errorMessage}{CYAN}')
		кроме:
			print(f'{CYAN}[{RED}-{CYAN}] Пиши верно! или ты лох')
			
