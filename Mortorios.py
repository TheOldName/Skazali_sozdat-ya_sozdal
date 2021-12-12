import telebot
from telebot import types
from random import choice
from random import randint
import sqlite3

bot = telebot.TeleBot('2060146318:AAF06zNS93TsQewvlsJF3lFhazPoqZP0nv4')

com = sqlite3.connect("Player.db", check_same_thread = False)
cur = com.cursor()

# класс игрока и его объявление

class Player:
  def __init__(self):
    self.HP = 50
    self.DMG = 10
    self.LVL = 1

player = Player()
global player

# класс врага и его объявление

class Enemy:
  def __init__(self):
    self.HP = player.DMG + randint(-3, 3)
    self.DMG = player.DMG + randint(-2, 2)
    self.LVL = round(player.DMG/self.HP)

enemy1 = Enemy()
global enemy1
enemy2  = Enemy()
global enemy2
enemy3 = Enemy()
global enemy3
enemy4 = Enemy()
global enemy4

# всякие нуженые штукм

death = 0
global death

fight = 0
global fight

oneen = 0
global oneen

# создание таблицы

t = 'CREATE TABLE IF NOT EXISTS player( ' \
      ' id INT NOT NULL PRIMARY KEY,' \
      ' hp INT,' \
      ' dmg INT,' \
      ' lvl INT)'

cur.execute(t)

cur.execute("INSERT INTO player VALUES(?, ?, ?, ?)", [1, player.HP, player.DMG, player.LVL])

# ответ на команду /start

@bot.message_handler(commands=['start'])
def welcome(message):
  bot.reply_to(message, "Погнали! Просто напиши комманду /nextstep!")

# ответ на команду /restart

@bot.message_handler(commands=['restart'])
def welcome(message):
  global death
  if death == 1:
    bot.reply_to(message, "Погнали! Просто напиши комманду /nextstep!")
    game_bool = True
    death = 0

# ответ на комаиду /nextstep

@bot.message_handler(commands=['nextstep'])
def welcome(message):
  global fight
  global death
  global player
  player = Player()

  
  if fight == 0 and death == 0:
    
    global oneen
    
    markup = types.InlineKeyboardMarkup()
    bot.send_message(message.chat.id, "Ваше здоровье: " + str(player.HP) + ", " + "Ваш урон: " + str(player.DMG) + ", " + "Ваш уровень: " + str(player.LVL))
    item1 = types.InlineKeyboardButton(choice(["Зомби, ", "Вепрь, ", "Демон, ", "Оборотень, "]) + 'Здоровье: ' + str(enemy1.HP) + ' Урон: ' + str(enemy1.DMG), callback_data = 'en1')
    item2 = types.InlineKeyboardButton(choice(["Зомби, ", "Вепрь, ", "Демон, ", "Оборотень, "]) + 'Здоровье: ' + str(enemy2.HP) + ' Урон: ' + str(enemy2.DMG), callback_data = 'en2')
    item3 = types.InlineKeyboardButton(choice(["Зомби, ", "Вепрь, ", "Демон, ", "Оборотень, "]) + 'Здоровье: ' + str(enemy3.HP) + ' Урон: ' + str(enemy3.DMG), callback_data = 'en3')
    item4 = types.InlineKeyboardButton(choice(["Зомби, ", "Вепрь, ", "Демон, ", "Оборотень, "]) + 'Здоровье: ' + str(enemy4.HP) + ' Урон: ' + str(enemy4.DMG), callback_data = 'en4')

    markup.add(item1)
    markup.add(item2)
    markup.add(item3)
    markup.add(item4)
    
    oneen = 0
    fight = 1
    
    bot.send_message(message.chat.id, "На вашем пути встали враги. Кого в будете атаковать?", reply_markup=markup)

# бой

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
  
  global date
  global enemy1
  global enemy2
  global enemy3
  global enemy4
  global fight
  global death
  global oneen
  global player
  
  fight = 0
  date = call.data

  if call.data == 'en1' and oneen == 0:
    
    oneen = 1
    
    if enemy1.HP <= player.DMG and death == 0:
      
      bot.send_message(call.message.chat.id, 'Вы победили! Введите команду /nextstep, чтобы продолжить')
      
      player.HP = player.HP + 5
      player.DMG = player.DMG + 1
      player.LVL = player.LVL + 1
      
      enemy1 = Enemy()
      enemy2 = Enemy()
      enemy3 = Enemy()
      enemy4 = Enemy()
      
      abc = 'Update player SET hp =' + str(player.HP)
      abc1 = 'Update player SET dmg =' + str(player.DMG)
      abc2 = 'Update player SET lvl =' + str(player.LVL)
      
      cur.execute(abc)
      cur.execute(abc1)
      cur.execute(abc2)
        
    elif enemy1.HP > player.DMG and death == 0:
      
      bot.send_message(call.message.chat.id, 'Вы проиграли! Введите команду /nextstep, чтобы продолжить')
      
      player.HP = player.HP - enemy1.DMG
     
      enemy1 = Enemy()
      enemy2 = Enemy()
      enemy3 = Enemy()
      enemy4 = Enemy()
      
      abc = 'Update player SET hp =' + str(player.HP)
      abc1 = 'Update player SET dmg =' + str(player.DMG)
      abc2 = 'Update player SET lvl =' + str(player.LVL)
      
      cur.execute(abc)
      cur.execute(abc1)
      cur.execute(abc2)

  if call.data == 'en2' and oneen == 0:
    
    oneen = 1
    
    if enemy2.HP <= player.DMG and death == 0:
      
      bot.send_message(call.message.chat.id, 'Вы победили! Введите команду /nextstep, чтобы продолжить')
      
      player.HP = player.HP + 5
      player.DMG = player.DMG + 1
      player.LVL = player.LVL + 1
      
      enemy1 = Enemy()
      enemy2 = Enemy()
      enemy3 = Enemy()
      enemy4 = Enemy()
      
      abc = 'Update player SET hp =' + str(player.HP)
      abc1 = 'Update player SET dmg =' + str(player.DMG)
      abc2 = 'Update player SET lvl =' + str(player.LVL)
      
      cur.execute(abc)
      cur.execute(abc1)
      cur.execute(abc2)

    elif enemy2.HP > player.DMG and death == 0:
      
      bot.send_message(call.message.chat.id, 'Вы проиграли! Введите команду /nextstep, чтобы продолжить')
      
      player.HP = player.HP - enemy2.DMG
      
      enemy1 = Enemy()
      enemy2 = Enemy()
      enemy3 = Enemy()
      enemy4 = Enemy()
      
      abc = 'Update player SET hp =' + str(player.HP)
      abc1 = 'Update player SET dmg =' + str(player.DMG)
      abc2 = 'Update player SET lvl =' + str(player.LVL)
      
      cur.execute(abc)
      cur.execute(abc1)
      cur.execute(abc2)

  if call.data == 'en3' and oneen == 0:
    
    oneen = 1
    
    if enemy3.HP <= player.DMG and death == 0:
    
      bot.send_message(call.message.chat.id, 'Вы победили! Введите команду /nextstep, чтобы продолжить')
    
      player.HP = player.HP + 5
      player.DMG = player.DMG + 1
      player.LVL = player.LVL + 1
    
      enemy1 = Enemy()
      enemy2 = Enemy()
      enemy3 = Enemy()
      enemy4 = Enemy()
    
      abc = 'Update player SET hp =' + str(player.HP)
      abc1 = 'Update player SET dmg =' + str(player.DMG)
      abc2 = 'Update player SET lvl =' + str(player.LVL)
    
      cur.execute(abc)
      cur.execute(abc1)
      cur.execute(abc2)

    elif enemy3.HP > player.DMG and death == 0:
    
      bot.send_message(call.message.chat.id, 'Вы проиграли! Введите команду /nextstep, чтобы продолжить')
    
      player.HP = player.HP - enemy3.DMG
    
      enemy1 = Enemy()
      enemy2 = Enemy()
      enemy3 = Enemy()
      enemy4 = Enemy()
    
      abc = 'Update player SET hp =' + str(player.HP)
      abc1 = 'Update player SET dmg =' + str(player.DMG)
      abc2 = 'Update player SET lvl =' + str(player.LVL)
    
      cur.execute(abc)
      cur.execute(abc1)
      cur.execute(abc2)

  if call.data == 'en4' and oneen == 0:
  
    oneen = 1
  
    if enemy4.HP <= player.DMG and death == 0:
  
      bot.send_message(call.message.chat.id, 'Вы победили! Введите команду /nextstep, чтобы продолжить')
  
      player.HP = player.HP + 5
      player.DMG = player.DMG + 1
      player.LVL = player.LVL + 1
  
      enemy1 = Enemy()
      enemy2 = Enemy()
      enemy3 = Enemy()
      enemy4 = Enemy()
  
      abc = 'Update player SET hp =' + str(player.HP)
      abc1 = 'Update player SET dmg =' + str(player.DMG)
      abc2 = 'Update player SET lvl =' + str(player.LVL)
  
      cur.execute(abc)
      cur.execute(abc1)
      cur.execute(abc2)

    elif enemy4.HP > player.DMG and death == 0:
  
      bot.send_message(call.message.chat.id, 'Вы проиграли! Введите команду /nextstep, чтобы продолжить')
  
      player.HP = player.HP - enemy4.DMG
  
      enemy1 = Enemy()
      enemy2 = Enemy()
      enemy3 = Enemy()
      enemy4 = Enemy()
  
      abc = 'Update player SET hp =' + str(player.HP)
      abc1 = 'Update player SET dmg =' + str(player.DMG)
      abc2 = 'Update player SET lvl =' + str(player.LVL)
  
      cur.execute(abc)
      cur.execute(abc1)
      cur.execute(abc2)

  # смерть
  
  if player.HP <= 0:
    
    bot.send_message(call.message.chat.id, 'Ваши глаза закрываются и вы чувствуете, что вас поглащает тьма... Ваш путь закончен. Введите команду /restart, чтобы начать ваше путешествие заново.')
    
    cur.execute('Update player SET hp = ? WHERE id = 1', [50])
    cur.execute('Update player SET dmg = ? WHERE id = 1', [10])
    cur.execute('Update player SET lvl = ? WHERE id = 1', [1])
    
    # player = Player()
    death = 1
    
    # global player

bot.polling(none_stop=True)
