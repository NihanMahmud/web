from flask import Flask 
from flask import render_template
from flask import request

info={}

app=Flask(__name__)
@app.route('/')
def main():
    return render_template('Form.html')

@app.route('/NextPage',methods=['POST'])
def main2():
    username=request.form['Name'] 
    email=request.form['Email']
    username=username.replace(' ','')
    if username in info.keys() or email in info.values():
        return render_template('taken.html')
    info[username]=email
    user_name=username
    return render_template('NextPage.html',name=username)

@app.route('/login')
def main3():
    return render_template('login.html')

@app.route('/profile',methods=['POST'])
def main4():
    username=request.form['username']
    email=request.form['email']
    username=username.replace(' ','')
    if username in info.keys() and email==info.get(username):
        return render_template('profile.html', username=username,email=email)
    else:
        return render_template('Wrong.html')         
@app.route('/profile/receivedata',methods=['POST'])
def main5():
    text=request.form['text']
    username=request.form['name']
    email=request.form['email']
    with open(f'Info/{username}.txt','a') as file:
        file.write(text)
    return render_template('receivedata.html',name=username,email=email)
@app.route('/profile/readdata',methods=['POST'])
def main6():
    username=request.form['username']
    email=request.form['email']
    with open(f'Info/{username}.txt','r') as file:
        text=file.read()
    return f'Your Data :\n{text}'+render_template('readdata.html',username=username,email=email)
app.run(debug=True)