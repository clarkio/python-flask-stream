from flask import (Flask, escape, g, jsonify, redirect, request, session,
                   url_for)

from login_decorator import login_required

app = Flask(__name__)
app.secret_key = 'oiefjasdfasdfwfe230j23iajsdflkj@#@#$fjfi'


@app.route('/')  # localhost:5000/
def hello():
    return 'Hello from VS Online Twitch'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('hello'))
    return '''
        <form method="post">
        <div>Hello</div>
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''


@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('hello'))


@app.route('/twitch', methods=['GET'])  # localhost:5000/twitch
def show_twitch():
    return 'From Twitch with love'


@app.route('/twitch/<username>', methods=['GET', 'POST'])
@login_required
def show_twitch_user(username):
    if request.method == 'GET':
        return f'This is {username}\'s page'
    else:
        return f'Stop trying to POST stuff here. Wrong address'


@app.route('/twitch/<user1>/<user2>/<user3>')
def show_twitch_users(user1, user2, user3):
    return f'{user1} {user2} {user3}'


@app.route('/sum/<float:first>/<int:second>')
def adding_numbers(first, second):
    return f' The answer is {first + second}'


@app.route('/fakejson')
def gimme_json():
    data = {
        'name': 'Brian',
        'job': 'Twitcher',
        'location': 'Florida'
    }

    return jsonify(data)


if __name__ == '__main__':
    app.run()
