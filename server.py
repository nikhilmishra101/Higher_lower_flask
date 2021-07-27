from flask import Flask
import random

actual_number = random.randint(0,9)
app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Guess a Number between 0 and 9</h1>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'/>"

@app.route("/<number>")
def check_number(number):
    if(int(number) > actual_number):
        return "<h1 style = 'color:pink'>Too high,try again!</h1>" \
               "<img src = ' https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'/>"
    elif(int(number)<actual_number):
        return "<h1 style = 'color:red'>Too low,try again!</h1>" \
               "<img src = ' https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'/>"
    elif(int(number) == actual_number):
        return "<h1 style = 'color:green'>You found me!</h1>" \
               "<img src = 'https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'/>"




if __name__ == "__main__":
    app.run(debug=True)