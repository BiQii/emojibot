from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import nltk
import emoji
from textblob import TextBlob
from textblob.np_extractors import ConllExtractor
import random

se1 = ['\U0001f619', '\U0001f496']
se2 = ['\U0001f60d', '\U0001f60a', '\U0001f495', '\U0001f60b', '\U0001f617']
se3 = ['\U0001f61b', '\U0001f600', '\U0001f603', '\U0001f60e', '\U0001f60c']
se4 = ['\U0001f609', '\U0001f61c', '\U0001f601', '\U0001f61d', '\U0001f604']
se5 = ['\U0001f606', '\U0001f606', '\U0001f602', '\U0001f62c', '\U0001f605']
se6 = ['\U0001f62f', '\U0001f625', '\U0001f635', '\U0001f61f']
se7 = ['\U0001f622', '\U0001f630', '\U0001f630', '\U0001f632']
se8 = ['\U0001f62a', '\U0001f613', '\U0001f613', '\U0001f613', '\U0001f628']
se9 = ['\U0001f62b', '\U0001f614', '\U0001f616', '\U0001f623']
se10 = ['\U0001f620', '\U0001f611', '\U0001f629', '\U0001f610', '\U0001f615']

app = Flask(__name__)

emoji_bot = ChatBot("EmojiBot", storage_adapter="chatterbot.storage.SQLStorageAdapter")
# emoji_bot.storage.drop()
trainer = ChatterBotCorpusTrainer(emoji_bot)
trainer.train("chatterbot.corpus.english")



@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    response = str(emoji_bot.get_response(userText))

    emoji_value = TextBlob(response).polarity
    emoji_last = ''

    if emoji_value > 0.7:
        emoji_last = random.choice(se1)
    elif emoji_value >= 0.602 and emoji_value < 0.7:
        emoji_last = random.choice(se2)
    elif emoji_value >= 0.48 and emoji_value < 0.602:
        emoji_last = random.choice(se3)
    elif emoji_value >= 0.41 and emoji_value < 0.48:
        emoji_last = random.choice(se4)
    elif emoji_value >= 0.15 and emoji_value < 0.41:
        emoji_last = random.choice(se5)
    elif emoji_value >= 0.04 and emoji_value < 0.15:
        emoji_last = random.choice(se6)
    elif emoji_value >= -0.07 and emoji_value < 0.04:
        emoji_last = random.choice(se7)
    elif emoji_value >= -0.14 and emoji_value < -0.07:
        emoji_last = random.choice(se8)
    elif emoji_value >= -0.28 and emoji_value < -0.14:
        emoji_last = random.choice(se9)
    elif emoji_value < 0.28:
        emoji_last = random.choice(se10)

    extractor = ConllExtractor()
    blob = TextBlob(response, np_extractor=extractor)
    word_list = blob.noun_phrases

    for word in word_list:
        emoji_word = ":" + word.lower().replace(" ", "_") + ":"
        emoji_replace = emoji.emojize(emoji_word)
        if emoji_replace is not emoji_word:
            response = response.replace(word, emoji_replace)

    token_list = nltk.word_tokenize(response)

    for token in token_list:
        emoji_word = ":" + token.lower().replace(" ", "_") + ":"
        emoji_replace = emoji.emojize(emoji_word)
        if emoji_replace is not emoji_word:
            response = response.replace(token, emoji_replace)

    return response + " " + emoji_last
    

if __name__ == '__main__':
    app.run()
