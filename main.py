from telegram import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
import logging
import xlrd
import random
import re

updater = Updater(token='*telegram bot token here*', use_context=True)
'''telegram bot token is needed'''
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
role_array = ['Science', 'Theater and Cinema', 'Business', 'Literature', 'Politics', 'Religion', 'Art']
book_array = ['Fantasy', 'Scientific literature', 'Classic', 'Drama', 'Crime']
health_array = ['A brisk 10-minute daily walk has lots of health benefits and counts towards your recommended 150 minutes of weekly exercise.', 'Whatever you hold in your mind on a consistent basis is exactly what you will experience in your life.', 'Eating vegetables provides health benefits. People who eat more vegetables and fruits as part of an overall healthy diet are likely to have a reduced risk of some chronic diseases. Vegetables provide nutrients vital for health and maintenance of your body.', 'Swimming is a good all-round activity because it keeps your heart rate up but takes some of the impact stress off your body, builds endurance, muscle strength and cardiovascular fitness, helps maintain a healthy weight, healthy heart and lungs.', 'Cardio helps burn a lot of calories, speeds up our metabolism and improves our body mass index (BMI). Performing cardio exercises regularly will help us maintain our ideal weight. It helps control blood pressure and strengthens the immune system.', 'Getting enough water every day is important for your health. Drinking water can prevent dehydration, a condition that can cause unclear thinking, result in mood change, cause your body to overheat, and lead to constipation and kidney stones.', 'Stress is key for survival, but too much stress can be detrimental. Emotional stress that stays around for weeks or months can weaken the immune system and cause high blood pressure, fatigue, depression, anxiety and even heart disease. In particular, too much epinephrine can be harmful to your heart.', 'Try hiking! Over time, your body adjusts to new fitness levels, and you can hike longer, faster, and harder without feeling as fatigued or out of breath. Hiking can also improve markers associated with cardiovascular health like blood pressure, blood sugar levels, and cholesterol.', 'Do not forget to sleep around 7-9 hours to keep your health well', 'Friends can increase your sense of belonging and purpose. Boost your happiness and reduce your stress. Improve your self-confidence and self-worth.']
challenge_array = ['Body: \nIt is known, that the daily norm for human is to do 10000 steps each day. However, it can be sometimes too hard to complete this norm for many of us. Thus, today your goal is to go out for a walk and make at least 5000 steps (you can use special tool on your phone to measure steps (e. g. Health for iPhone), or count it as about 50 minutes of brisk walking or 3 km). Then try to keep doing such short walking each day!. \n\nMind: \nKenKen and KenDoku (also known as Newdoku) are trademarked names for a style of arithmetic and logic puzzle invented in 2004 by Japanese math teacher Tetsuya Miyamoto, who intended the puzzles to be an instruction-free method of training the brain. The name derives from the Japanese word for cleverness (賢, ken, kashiko(i)). Try to solve 3*3, 4*4 and 5x5 (new puzzle — 3x3/4x4/5x5 — easy) versions. They should not be too hard, but already can improve your brain. You can set the difficulty level and play here: https://newdoku.com\n\nSpirit:\nWe usually forget to thank people we owe something. To be a thankful person is awesome idea in any case. Today you should say “thank you” at least 5 times. Of course, it makes sense to thanks only in a appropriate situations. In case such situations will be not enough for five thanks, you can try to think about thanks you forgot to say earlier or things you owe the nearest people at general.', 'Body:\nToday you should find a time for 2 short physical trainings (about 7 minutes each). Structure (30 seconds per exercise):\n1. Jumping jacks\n2. Wall sit\n3. Push-ups\n4. Abdominal crunches\n5. Step-up onto a chair\n6. Squats\n7. Triceps dip on a chair\n8. Plank\n9. High knees, running in place\n10. Alternating lunges\n11. Push-ups with rotation\n12. Side plank, each side\n\nVisualization and more information here: https://www.nytimes.com/guides/well/really-really-short-workouts\n\nMental:\nTo improve your braining skills, try chess. It is very ancient and beautiful board game. The 10 Best Benefits of Playing Chess:\nDevelops perspective.\nImproves memory.\nIncreases intelligence.\nDeepens focus.\nElevates creativity.\nBoosts planning skills.\nIncreases self-awareness.\nProtects against dementia.\nIf you are new at chess, then watch this video: https://www.youtube.com/watch?v=OCSbzArwB10 — Awesome youtuber (and chess International Master) for both beginners and advanced players in chess. Today you should find one suitable chess video on his or another chess channel and watch it. Try Chess.com for playing chess yourself.\n\nSpirit:\nIt sound a bit paradoxically, but the thing is, that to help your own spirit, you should be ready to help others. Today you should voluntarily help at least 3 persons. That means, do not ignore the requests from others and try to offer help on your own. In case this will be not enough, then just ask others if they need help in anything and try to help them in that. Be sure, helping other people will finally do better for yourself.']
wb = xlrd.open_workbook('Data/RoleModels.xls')
wb2 = xlrd.open_workbook('Data/Books.xls')
fantasy_sheet = wb2.sheet_by_index(0)
scientific_sheet = wb2.sheet_by_index(1)
classic_sheet = wb2.sheet_by_index(2)
drama_sheet = wb2.sheet_by_index(3)
crime_sheet = wb2.sheet_by_index(4)
science_sheet = wb.sheet_by_index(0)
cinema_sheet = wb.sheet_by_index(1)
business_sheet = wb.sheet_by_index(2)
literature_sheet = wb.sheet_by_index(3)
politics_sheet = wb.sheet_by_index(4)
religion_sheet = wb.sheet_by_index(5)
art_sheet = wb.sheet_by_index(6)
health_cycle = 0


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm ImproMot, I am a bot that helps you improve your motivation!")
    keyboard = [
        [
            KeyboardButton("Challenge"),
        ],
        [
            KeyboardButton("Role Models"),
            KeyboardButton("Books"),
            KeyboardButton("Health"),
        ],
        [KeyboardButton("Team")],
    ]
    markup = ReplyKeyboardMarkup(keyboard, True)

    update.message.reply_text('Please choose: ', reply_markup=markup)


def home(update, context):
    keyboard = [
        [
            KeyboardButton("Challenge"),
        ],
        [
            KeyboardButton("Role Models"),
            KeyboardButton("Books"),
            KeyboardButton("Health"),
        ],
        [KeyboardButton("Team")],
    ]
    markup = ReplyKeyboardMarkup(keyboard, True)

    update.message.reply_text('Please choose: ', reply_markup=markup)


def role(update, context):
    keyboard = [
        [
            KeyboardButton("Science"),
            KeyboardButton("Theater and Cinema"),
        ],
        [
            KeyboardButton("Business"),
            KeyboardButton("Literature"),
        ],
        [
            KeyboardButton("Politics"),
            KeyboardButton("Religion"),
        ],
        [
            KeyboardButton("Art"),
            KeyboardButton('Back')
        ],
    ]
    markup = ReplyKeyboardMarkup(keyboard, True)

    update.message.reply_text('Please choose role model: ', reply_markup=markup)


def book(update, context):
    keyboard = [
        [
            KeyboardButton("Fantasy"),
            KeyboardButton("Scientific literature"),
        ],
        [
            KeyboardButton("Classic"),
            KeyboardButton("Drama"),
        ],
        [
            KeyboardButton("Crime"),
            KeyboardButton("Back"),
        ],
    ]
    markup = ReplyKeyboardMarkup(keyboard, True)

    update.message.reply_text('Please choose book genre: ', reply_markup=markup)


def models(update, context):
    user_choice = update.message.text
    rand = random.randint(0, 2)
    if user_choice == role_array[0]:
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(science_sheet.cell_value(rand, 0), 'rb'))
        button = [[InlineKeyboardButton('More Info', url=science_sheet.cell_value(rand, 1))]]
        markup = InlineKeyboardMarkup(button)
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text=science_sheet.cell_value(rand, 2) + '\n \n' + 'Date of birth: ' + science_sheet.cell_value(rand, 3),
                                 reply_markup=markup)
    elif user_choice == role_array[1]:
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(cinema_sheet.cell_value(rand, 0), 'rb'))
        button = [[InlineKeyboardButton('More Info', url=cinema_sheet.cell_value(rand, 1))]]
        markup = InlineKeyboardMarkup(button)
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text=cinema_sheet.cell_value(rand, 2) + '\n \n' + 'Date of birth: ' + cinema_sheet.cell_value(rand, 3),
                                 reply_markup=markup)
    elif user_choice == role_array[2]:
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(business_sheet.cell_value(rand, 0), 'rb'))
        button = [[InlineKeyboardButton('More Info', url=business_sheet.cell_value(rand, 1))]]
        markup = InlineKeyboardMarkup(button)
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text=business_sheet.cell_value(rand, 2) + '\n \n' + 'Date of birth: ' + business_sheet.cell_value(rand, 3),
                                 reply_markup=markup)
    elif user_choice == role_array[3]:
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(literature_sheet.cell_value(rand, 0), 'rb'))
        button = [[InlineKeyboardButton('More Info', url=literature_sheet.cell_value(rand, 1))]]
        markup = InlineKeyboardMarkup(button)
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text=literature_sheet.cell_value(rand, 2) + '\n \n' + 'Date of birth: ' + literature_sheet.cell_value(rand, 3),
                                 reply_markup=markup)
    elif user_choice == role_array[4]:
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(politics_sheet.cell_value(rand, 0), 'rb'))
        button = [[InlineKeyboardButton('More Info', url=politics_sheet.cell_value(rand, 1))]]
        markup = InlineKeyboardMarkup(button)
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text=politics_sheet.cell_value(rand, 2) + '\n \n' + 'Date of birth: ' + politics_sheet.cell_value(rand, 3),
                                 reply_markup=markup)
    elif user_choice == role_array[5]:
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(religion_sheet.cell_value(rand, 0), 'rb'))
        button = [[InlineKeyboardButton('More Info', url=religion_sheet.cell_value(rand, 1))]]
        markup = InlineKeyboardMarkup(button)
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text=religion_sheet.cell_value(rand, 2) + '\n \n' + 'Date of birth: ' + religion_sheet.cell_value(rand, 3),
                                 reply_markup=markup)
    else:
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(art_sheet.cell_value(rand, 0), 'rb'))
        button = [[InlineKeyboardButton('More Info', url=art_sheet.cell_value(rand, 1))]]
        markup = InlineKeyboardMarkup(button)
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text=art_sheet.cell_value(rand, 2) + '\n \n' + 'Date of birth: ' + art_sheet.cell_value(rand, 3),
                                 reply_markup=markup)


def books(update, context):
    user_choice = update.message.text
    rand = random.randint(0, 2)
    if user_choice == book_array[0]:
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(fantasy_sheet.cell_value(rand, 0), 'rb'))
        button = [[InlineKeyboardButton('·About·', callback_data='about1' + str(rand)),
                   InlineKeyboardButton('More similar books', callback_data='more1' + str(rand))]]
        markup = InlineKeyboardMarkup(button)
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text=fantasy_sheet.cell_value(rand, 1),
                                 reply_markup=markup)
    elif user_choice == book_array[1]:
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(scientific_sheet.cell_value(rand, 0), 'rb'))
        button = [[InlineKeyboardButton('·About·', callback_data='about2' + str(rand)),
                   InlineKeyboardButton('More similar books', callback_data='more2' + str(rand))]]
        markup = InlineKeyboardMarkup(button)
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text=scientific_sheet.cell_value(rand, 1),
                                 reply_markup=markup)
    elif user_choice == book_array[2]:
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(classic_sheet.cell_value(rand, 0), 'rb'))
        button = [[InlineKeyboardButton('·About·', callback_data='about3' + str(rand)),
                   InlineKeyboardButton('More similar books', callback_data='more3' + str(rand))]]
        markup = InlineKeyboardMarkup(button)
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text=classic_sheet.cell_value(rand, 1),
                                 reply_markup=markup)
    elif user_choice == book_array[3]:
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(drama_sheet.cell_value(rand, 0), 'rb'))
        button = [[InlineKeyboardButton('·About·', callback_data='about4' + str(rand)),
                   InlineKeyboardButton('More similar books', callback_data='more4' + str(rand))]]
        markup = InlineKeyboardMarkup(button)
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text=drama_sheet.cell_value(rand, 1),
                                 reply_markup=markup)
    else:
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(crime_sheet.cell_value(rand, 0), 'rb'))
        button = [[InlineKeyboardButton('·About·', callback_data='about5' + str(rand)),
                   InlineKeyboardButton('More similar books', callback_data='more5' + str(rand))]]
        markup = InlineKeyboardMarkup(button)
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text=crime_sheet.cell_value(rand, 1),
                                 reply_markup=markup)


def callback_about(update, context):
    rand = int(update.callback_query.data[len(update.callback_query.data) - 1])
    if re.match('about1\d', update.callback_query.data):
        button = [[InlineKeyboardButton('·About·', callback_data='about1' + str(rand)),
                   InlineKeyboardButton('More similar books', callback_data='more1' + str(rand))]]
        markup = InlineKeyboardMarkup(button)
        context.bot.editMessageText(message_id=update.callback_query.message.message_id,
                                    chat_id=update.callback_query.message.chat_id,
                                    text=fantasy_sheet.cell_value(rand, 1),
                                    reply_markup=markup)
    elif re.match('about2\d', update.callback_query.data):
        button = [[InlineKeyboardButton('·About·', callback_data='about2' + str(rand)),
                   InlineKeyboardButton('More similar books', callback_data='more2' + str(rand))]]
        markup = InlineKeyboardMarkup(button)
        context.bot.editMessageText(message_id=update.callback_query.message.message_id,
                                    chat_id=update.callback_query.message.chat_id,
                                    text=scientific_sheet.cell_value(rand, 1),
                                    reply_markup=markup)
    elif re.match('about3\d', update.callback_query.data):
        button = [[InlineKeyboardButton('·About·', callback_data='about3' + str(rand)),
                   InlineKeyboardButton('More similar books', callback_data='more3' + str(rand))]]
        markup = InlineKeyboardMarkup(button)
        context.bot.editMessageText(message_id=update.callback_query.message.message_id,
                                    chat_id=update.callback_query.message.chat_id,
                                    text=classic_sheet.cell_value(rand, 1),
                                    reply_markup=markup)
    elif re.match('about4\d', update.callback_query.data):
        button = [[InlineKeyboardButton('·About·', callback_data='about4' + str(rand)),
                   InlineKeyboardButton('More similar books', callback_data='more4' + str(rand))]]
        markup = InlineKeyboardMarkup(button)
        context.bot.editMessageText(message_id=update.callback_query.message.message_id,
                                    chat_id=update.callback_query.message.chat_id,
                                    text=drama_sheet.cell_value(rand, 1),
                                    reply_markup=markup)
    else:
        button = [[InlineKeyboardButton('·About·', callback_data='about5' + str(rand)),
                   InlineKeyboardButton('More similar books', callback_data='more5' + str(rand))]]
        markup = InlineKeyboardMarkup(button)
        context.bot.editMessageText(message_id=update.callback_query.message.message_id,
                                    chat_id=update.callback_query.message.chat_id,
                                    text=crime_sheet.cell_value(rand, 1),
                                    reply_markup=markup)


def callback_more(update, context):
    rand = int(update.callback_query.data[len(update.callback_query.data) - 1])
    if re.match('more1\d', update.callback_query.data):
        button = [[InlineKeyboardButton('About', callback_data='about1' + str(rand)),
                   InlineKeyboardButton('·More similar books·', callback_data='more1' + str(rand))]]
        markup = InlineKeyboardMarkup(button)
        context.bot.editMessageText(message_id=update.callback_query.message.message_id,
                                    chat_id=update.callback_query.message.chat_id,
                                    text=fantasy_sheet.cell_value(rand, 2),
                                    reply_markup=markup)
    elif re.match('more2\d', update.callback_query.data):
        button = [[InlineKeyboardButton('About', callback_data='about2' + str(rand)),
                   InlineKeyboardButton('·More similar books·', callback_data='more2' + str(rand))]]
        markup = InlineKeyboardMarkup(button)
        context.bot.editMessageText(message_id=update.callback_query.message.message_id,
                                    chat_id=update.callback_query.message.chat_id,
                                    text=scientific_sheet.cell_value(rand, 2),
                                    reply_markup=markup)
    elif re.match('more3\d', update.callback_query.data):
        button = [[InlineKeyboardButton('About', callback_data='about3' + str(rand)),
                   InlineKeyboardButton('·More similar books·', callback_data='more3' + str(rand))]]
        markup = InlineKeyboardMarkup(button)
        context.bot.editMessageText(message_id=update.callback_query.message.message_id,
                                    chat_id=update.callback_query.message.chat_id,
                                    text=classic_sheet.cell_value(rand, 2),
                                    reply_markup=markup)
    elif re.match('more4\d', update.callback_query.data):
        button = [[InlineKeyboardButton('About', callback_data='about4' + str(rand)),
                   InlineKeyboardButton('·More similar books·', callback_data='more4' + str(rand))]]
        markup = InlineKeyboardMarkup(button)
        context.bot.editMessageText(message_id=update.callback_query.message.message_id,
                                    chat_id=update.callback_query.message.chat_id,
                                    text=drama_sheet.cell_value(rand, 2),
                                    reply_markup=markup)
    else:
        button = [[InlineKeyboardButton('About', callback_data='about5' + str(rand)),
                   InlineKeyboardButton('·More similar books·', callback_data='more5' + str(rand))]]
        markup = InlineKeyboardMarkup(button)
        context.bot.editMessageText(message_id=update.callback_query.message.message_id,
                                    chat_id=update.callback_query.message.chat_id,
                                    text=crime_sheet.cell_value(rand, 2),
                                    reply_markup=markup)


def health(update, context):
    global health_cycle
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=health_array[health_cycle])
    health_cycle += 1
    if health_cycle == 10:
        health_cycle = 0


def challenge(update, context):
    rand = random.randint(0, len(challenge_array) - 1)
    button = [[InlineKeyboardButton('Done', callback_data='done' + str(rand)),
               InlineKeyboardButton('Other Challenge', callback_data='other' + str(rand))]]
    markup = InlineKeyboardMarkup(button)
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=challenge_array[rand],
                             reply_markup=markup)


def callback_other(update, context):
    rand = int(update.callback_query.data[len(update.callback_query.data) - 1])
    while True:
        new_rand = random.randint(0, len(challenge_array) - 1)
        if new_rand != rand:
            break
    button = [[InlineKeyboardButton('Done', callback_data='done' + str(new_rand)),
               InlineKeyboardButton('Other Challenge', callback_data='other' + str(new_rand))]]
    markup = InlineKeyboardMarkup(button)
    context.bot.editMessageText(message_id=update.callback_query.message.message_id,
                                chat_id=update.callback_query.message.chat_id,
                                text=challenge_array[new_rand],
                                reply_markup=markup)


def callback_done(update, context):
    rand = int(update.callback_query.data[len(update.callback_query.data) - 1])
    button = [[InlineKeyboardButton('Other Challenge', callback_data='other' + str(rand))]]
    markup = InlineKeyboardMarkup(button)
    context.bot.editMessageText(message_id=update.callback_query.message.message_id,
                                chat_id=update.callback_query.message.chat_id,
                                text='Well done! You may rest for today or do some more!',
                                reply_markup=markup)


def contacts(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text='Yegor Varchenko - responsible for team management and progress control @telegrard\nTalha Keles - responsible for health and books related content\nIurii Lepesevich - responsible for contract management and improvement\nRustam Adilov - responsible for role model related content\nOleksii Avdieiev - responsible for prototype development')


start_handler = CommandHandler('start', start)
model_handler = MessageHandler(Filters.text('Role Models'), role)
book_handler = MessageHandler(Filters.text('Books'), book)
back_handler = MessageHandler(Filters.text('Back'), home)
health_handler = MessageHandler(Filters.text('Health'), health)
challenge_handler = MessageHandler(Filters.text('Challenge'), challenge)
contacts_handler = MessageHandler(Filters.text('Team'), contacts)
role_handler = MessageHandler(Filters.text(role_array), models)
genre_handler = MessageHandler(Filters.text(book_array), books)
callback_handler_about = CallbackQueryHandler(callback_about, pattern=r'about')
callback_handler_more = CallbackQueryHandler(callback_more, pattern=r'more')
callback_handler_done = CallbackQueryHandler(callback_done, pattern='done')
callback_handler_other = CallbackQueryHandler(callback_other, pattern=r'other')

dispatcher.add_handler(start_handler)
dispatcher.add_handler(model_handler)
dispatcher.add_handler(back_handler)
dispatcher.add_handler(role_handler)
dispatcher.add_handler(book_handler)
dispatcher.add_handler(genre_handler)
dispatcher.add_handler(callback_handler_about)
dispatcher.add_handler(callback_handler_more)
dispatcher.add_handler(health_handler)
dispatcher.add_handler(challenge_handler)
dispatcher.add_handler(contacts_handler)
dispatcher.add_handler(callback_handler_other)
dispatcher.add_handler(callback_handler_done)
updater.start_polling()

updater.idle()