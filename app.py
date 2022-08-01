from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer


app = Flask(__name__)

emoji_bot = ChatBot("EmojiBot", storage_adapter="chatterbot.storage.SQLStorageAdapter")
emoji_bot.storage.drop()
trainer = ChatterBotCorpusTrainer(emoji_bot)
trainer.train("C:/Users/Windows10/anaconda3/Lib/site-packages/chatterbot_corpus/data/emojibot/eb_emotion.yml")



@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    response = str(emoji_bot.get_response(userText))
    return response
    

if __name__ == '__main__':
    app.run()
