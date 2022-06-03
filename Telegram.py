from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters


#beaftifulsoup
from bs4 import BeautifulSoup
import requests
from csv import writer
url = 'https://www.linkedin.com/jobs/search/?keywords=data%20scientist&position=1&pageNum=0'
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
lists = soup.find_all('div', class_="base-card")

header = ['title', 'company', 'location', 'urls']
for list in lists:
	title = list.find('h3', class_="base-search-card__title").text.replace('\n','')
	comp = list.find('a', class_="hidden-nested-link").text.replace('\n','')
	location = list.find('span', class_="job-search-card__location").text.replace('\n','')
	urls = list.find('a', class_="base-card__full-link").attrs['href']
	info = [title, comp, location, urls]
	#print(info)
#
#print(header)


updater = Updater('5337718176:AAELMY-mXuoo_5UHz3NTnBpjtQZAyJmlXOE',
				use_context=True)


def start(update: Update, context: CallbackContext):
	update.message.reply_text(
		"Hello sir, Welcome to the Bot.Please write\
		/help to see the commands available.")

def help(update: Update, context: CallbackContext):

	update.message.reply_text("""Available Commands :-
	/Naukri - To get the Naukri Job's
	/linkedin - To get the LinkedIn Job's
	/Glassdoor - Glassdoor Job's
	Note* : Currently only linkedin is working To get the GeeksforGeeks URL""")


def linkedin(update: Update, context: CallbackContext):
	for list in lists:
		title = list.find('h3', class_="base-search-card__title").text.replace('\n','')
		comp = list.find('a', class_="hidden-nested-link").text.replace('\n','')
		location = list.find('span', class_="job-search-card__location").text.replace('\n','')
		urls = list.find('a', class_="base-card__full-link").attrs['href']
		info = [title, comp, location, urls]
		update.message.reply_text(info[0]+'\n'+info[1]+'\n'+info[2] +'\n'+ info[3])
	# 	print(i)

def unknown(update: Update, context: CallbackContext):
	update.message.reply_text(
		"Sorry '%s' is not a valid command" % update.message.text)


def unknown_text(update: Update, context: CallbackContext):
	update.message.reply_text(
		"Sorry I can't recognize you , you said '%s'" % update.message.text)


updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('linkedin', linkedin))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
updater.dispatcher.add_handler(MessageHandler(
	Filters.command, unknown)) # Filters out unknown commands

# Filters out unknown messages.
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))

updater.start_polling()
