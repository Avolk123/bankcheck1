import requests
import telebot
import psycopg2
import mysql.connector
import asyncio
import time
from datetime import datetime

config = {
  'user': 'root',
  'password': 'root',
  'host': 'localhost',
  'database': 'babki',
  'raise_on_warnings': True,
}

link = mysql.connector.connect(**config)
cursor = link.cursor()

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
banks = ["http://www.sberbank.ru", "https://alfabank.ru", "https://www.rgs.ru","https://www.pochtabank.ru", "https://www.tinkoff.ru", "https://tochka.com", "https://www.vtb.ru", "https://prostobank.online", "https://www.mtsbank.ru", "https://www.uralsib.ru"]
channel = '@bank1check'
token = '5844091544:AAGzkHvEIkM9aVopIKNcbKuzLt51Q_KH-d0'

headers_mobile = { 'User-Agent' : 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B137 Safari/601.1'}


async def stat_collect():
    while True:
        uptime_list=[]
        
        for bank in banks:
            response = requests.get(bank)
            response_mobile = requests.get(bank, headers=headers_mobile)
            bot = telebot.TeleBot(token)
            if response.status_code == 200:
                #print(bank + ' is up!')
                uptime_list.append(1)
                bot.send_message(channel, bank + ' is up! ' + current_time)
            elif response.status_code != 200 or response_mobile.status_code != 200:
                uptime_list.append(0)
                #print(bank + ' is down!')
                bot.send_message(channel, bank + ' is down! ' + current_time)
        cursor.execute('INSERT INTO babki.uptime_stat (sberbank, alfabank, rgs, pochtabank, tinkoff, tochka, vtb, prostobank, mtsbank, uralsib) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);', (str(uptime_list[0]), str(uptime_list[1]), str(uptime_list[2]), str(uptime_list[3]), str(uptime_list[4]), str(uptime_list[5]), str(uptime_list[6]), str(uptime_list[7]), str(uptime_list[8]), str(uptime_list[9])))
        link.commit()
        await asyncio.sleep(180)


async def stat_send():
    bot = telebot.TeleBot(token)
    while True:
        cursor.execute("SELECT * FROM babki.uptime_stat")
        records = list(cursor.fetchall())
        for i in range(len(records[0])):
            uptime_sum = 0
            for j in range(len(records)):
                uptime_sum = uptime_sum + int(records[j][i])
            uptime_percent = round(uptime_sum / len(records) * 100, 2)
            bot.send_message(channel, banks[i] + 'uptime percent = ' + str(uptime_percent))

        await asyncio.sleep(86400)


async def main():
    asyncio.create_task(stat_collect())
    asyncio.create_task(stat_send())
    loop = asyncio.get_running_loop()
    while True:
        await loop.run_in_executor(None, time.sleep, 0.1)

asyncio.run(main())
