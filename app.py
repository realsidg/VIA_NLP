
import os
from flask import Flask, request, render_template

from test_model import chatbot


app = Flask(__name__)
UPLOAD_FOLDER = 'down/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/home')
def hello_world():    
    return render_template('index.html', msg = "Hello")


@app.route('/recruitMe', methods=["POST"])
def recruitMe():
    file = request.files['file']
    email = request.form['Email']
    if file:
        file.save(os.path.join(UPLOAD_FOLDER, email))
    return render_template('home.html', msg = "Hello")

@app.route("/")
def home():    
    return render_template("home.html") 

@app.route("/get")
def get_bot_response():    
    bot = chatbot()
    userText = request.args.get('msg')    
    ans = str(bot.test_output(userText)) 
    print(ans)
    return ans
    
if __name__ == "__main__":    
    app.run()
