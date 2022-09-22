from flask import Flask
app = Flask(__name__)
print(__name__)
import random
random_number = random.randint(0,9)
print(random_number)



@app.route('/')
def intro():
    return '<h1 style="color:#AD381F">Guess a number between 0 and 9:</h1>'

@app.route("/<guess_number>")
def guess(guess_number):
    guess_number = int(guess_number)
    if guess_number < random_number:
        return '<h1 style="color:red"> Too Low </h1>'\
               '<img src="https://media3.giphy.com/media/IevhwxTcTgNlaaim73/giphy.gif?cid=ecf05e47cvsn6s2xmdbz05my9ngyj8fqegglzr7bfaf2oxyn&rid=giphy.gif&ct=g">'
    elif guess_number > random_number:
        return '<h1 style="color:blue"> Too High </h1>' \
               '<img src="https://media2.giphy.com/media/l4FGvOx8nWTziDphS/200w.webp?cid=ecf05e47a6h9yut3wust1russzu7zmh4sv4xkcktu2xnytn8&rid=200w.webp&ct=g" width=600>'
    else:
        return '<h1 style="color:green"> You Gussed </h1>' \
               '<img src="https://media0.giphy.com/media/pNpONEEg3pLIQ/giphy.gif?cid=790b76112b2ed06fa789b4c0699725a4748d3a1c761dc96a&rid=giphy.gif&ct=g" width=600>'


if __name__ == "__main__":
    app.run(debug=True)
