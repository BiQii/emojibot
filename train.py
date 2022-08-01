from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import emoji

bot = ChatBot("EmojiBot")
bot.storage.drop()

trainer = ChatterBotCorpusTrainer(bot)

trainer.train("C:/Users/Windows10/anaconda3/Lib/site-packages/chatterbot_corpus/data/emojibot/emojibot.yml")

response = bot.get_response("How are you?")
shorttext = ":" + str(response) + ":"
print(emoji.emojize(shorttext))