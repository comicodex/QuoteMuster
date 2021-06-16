from flask import Flask, render_template, request
from random import randint


app = Flask(__name__)
app.config["DEBUG"] = True


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload_quote", methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        name = request.form.get("name")
        quotes = [ "'Life is about making an impact, not making an income' - Kevin Kruse",
            "'Whatever the mind of man can conceive and believe, it can achieve' -  Napoleon Hill",
            "'Strive not to be a success, but rather to be of value' - Albert Einstein",
            "'Two roads diverged in a wood, and I—I took the one less traveled by, And that has made all the difference' - Robert Frost",
            "'I've missed more than 9000 shots in my career. I've lost almost 300 games. 26 times I've been trusted to take the game winning shot and missed. I've failed over and over and over again in my life. And that is why I succeed' - Michael Jordan",
            "'The most difficult thing is the decision to act, the rest is merely tenacity' - Amelia Earhart", 
            "'We become what we think about' - Earl Nightingale",
            "'Twenty years from now you will be more disappointed by the things that you didn’t do than by the ones you did do, so throw off the bowlines, sail away from safe harbor, catch the trade winds in your sails.  Explore, Dream, Discover' - Mark Twain", 
            "'Life is 10% what happens to me and 90% of how I react to it' - Charles Swindoll", 
            "'The most common way people give up their power is by thinking they don’t have any' - Alice Walker", 
            "'The mind is everything. What you think you become' - Buddha", 
            "'Your time is limited, so don’t waste it living someone else’s life' - Steve Jobs", 
            "'Winning isn’t everything, but wanting to win is' - Vince Lombardi", 
            "'I am not a product of my circumstances. I am a product of my decisions' - Stephen Covey", 
            "'Every child is an artist.  The problem is how to remain an artist once he grows up ' - Pablo Picasso",
            "'You can never cross the ocean until you have the courage to lose sight of the shore' - Christopher Columbus" ]
        randomNumber = randint(0,len(quotes)-1)
        quote = quotes[randomNumber] 
           
    return render_template("quote.html", name=name, response=quote)

if __name__ == "__main__":
    app.run()
