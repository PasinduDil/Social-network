from flask import Flask, render_template, request, redirect
from database.connection import get_db
from database.queries import create_user, connect_users, get_recommendations

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create-profile', methods=['POST'])
def create_profile():
    username = request.form['username']
    name = request.form['name']
    age = request.form['age']
    create_user(username, name, age)
    return redirect('/')

@app.route('/connect-friends', methods=['POST'])
def connect_friends():
    your_username = request.form['your_username']
    friend_username = request.form['friend_username']
    connect_users(your_username, friend_username)
    return redirect('/')

@app.route('/recommendations', methods=['POST'])
def recommendations():
    username = request.form['username']
    recommendations = get_recommendations(username)
    return render_template('recommendations.html', recommendations=recommendations)

if __name__ == '__main__':
    app.run(debug=True)