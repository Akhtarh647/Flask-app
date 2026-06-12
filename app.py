import api
import requests
from flask import Flask, render_template, request, redirect, session
from Db import Database

app = Flask(__name__)
# FIX 1: Added a secret key. Flask requires this to use sessions!
app.secret_key = "super_secret_key_change_me_later"

dbo = Database()

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/register')
def hello():
    return render_template('register.html')

@app.route('/perform_registration', methods=["POST"])
def perform_registration():
    name = request.form.get('user_ka_naam')
    email = request.form.get('user_ka_email')
    password = request.form.get('user_ka_pass')

    response = dbo.insert(name, email, password)

    if response == 1:
        return render_template('login.html', message='Registration successful, Kindly login')
    else:
        return render_template('register.html', message='Email already exists')

@app.route('/perform_login', methods=["POST"])
def perform_login():
    email = request.form.get('user_ka_email')
    password = request.form.get('user_ka_pass')

    response = dbo.search(email, password)
    if response == 1:
        session['logged_in'] = True
        session['user_email'] = email # Optional: save their email in session too!
        return redirect('/profile')
    else:
        return render_template('login.html', message='Incorrect Email or Password')

@app.route('/profile')
def profile():
    # It's good practice to protect the profile route too!
    if 'logged_in' in session:
        return render_template('profile.html')
    else:
        return redirect('/')

@app.route('/Paraphrasing Tool')
def ParaphrasingTool():
    if 'logged_in' in session:
        return render_template('Paraphrasingtool.html')
    else:
        return redirect('/')


@app.route('/perform_Paraphrasing', methods=['POST'])
def perform_Paraphrasing():
    # FIX 3: Check specifically if they are logged in, not just if a session exists
    if 'logged_in' in session:
        text = request.form.get('paraphrasing_text')
        response = api.paraphrase(text)
        print(response)

        return render_template('Paraphrasingtool.html', response=response)
    else:
        return redirect('/')


# 1. The GET route: This allows you to view the page when you type the URL
@app.route('/sentimentanalysis')
def show_sentiment_page():
    if 'logged_in' in session:
        return render_template('sentimentanalysis.html')
    else:
        return redirect('/')


# 2. The POST route: This processes the text when you click Submit
@app.route('/perform_sentiment', methods=['POST'])
def perform_sentiment():
    if 'logged_in' in session:
        text = request.form.get('Sentiment_text')
        # Make sure you have an api.sentiment() function in your api.py file!
        response = api.sentiment(text)

        return render_template('sentimentanalysis.html', response=response)
    else:
        return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)