from flask import *
from flask_cors import *
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
# flask-debugtoolbar
# the toolbar is only enabled in debug mode
app.debug = True
app.config['SECRET_KEY'] = '<20986albert>'
toolbar = DebugToolbarExtension(app)
# endhere


@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route("/greet")
def greet():
    name = request.args.get("name")
    email = request.args.get("email")
    addres = request.args.get("address")
    city = request.args.get("city")
    state = request.args.get("state")
    zipcode = request.args.get("zipcode")
    country = request.args.get("country")
    return render_template("greet.html", name=name, email=email, addres=addres, city=city, state=state, zipcode=zipcode, country=country)


cors = CORS(app)


@app.route("/core")
def list_users():
    return "welcome to my website"
if __name__ == "__main__":
    app.run(debug=True)