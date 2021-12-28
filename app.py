from flask import Flask, redirect, url_for, render_template, request  
from flask import session 
app = Flask(__name__)
app.secret_key = '123'


@app.route('/home')
@app.route('/')
def home_func():
    return render_template('home.html')

@app.route('/assignment9', methods=['GET', 'POST'])
def EX9_func():
    if request.method == 'GET':
        users = {'user1': {'Name': 'a', 'Email': 'a@gmail.com'},
                 'user2': {'Name': 'b', 'Email': 'b@gmail.com'},
                 'user3': {'Name': 'c', 'Email': 'c@gmail.com'},
                 'user4': {'Name': 'd', 'Email': 'd@gmail.com'},
                 'user5': {'Name': 'e', 'Email': 'e@gmail.com'}
                 }
        if 'name' in request.args: 
            name = request.args['name']
            if name != '':
                session['name'] = name  
                for i in users:
                    for j in users[i]:
                        if users[i][j] == name:
                            result = users[i]
                            session['result'] = result
                            return render_template('assignment9.html', Name=name, Result=result)  
            else:
                name = request.args['name']
                return render_template('assignment9.html', Name=name, Users=users)
    if request.method == 'POST':
        username = request.form['username'] 
        password = request.form['password']
        session['username'] = username
        return redirect(url_for('EX9_func'))
    return render_template('assignment9.html')


@app.route('/log_out')
def logout_func():
    username = ''
    session['username'] = username
    return render_template('assignment9.html', Username=username)


if __name__ == '__main__':
    app.run(debug=True)
