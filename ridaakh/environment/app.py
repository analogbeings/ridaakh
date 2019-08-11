# app.py
from ridaakh.api import Ridaakh
from DB.sample2 import new_user
# from ridaakh.forms import fields, forms, widgets
# from wtforms import Form,StringField, PasswordField, validators
# from wtforms.validators import InputRequired

app = Ridaakh()
# inpp = widgets

@app.route("/")
def home(req, resp):
    # resp.text = "Hello, this is a home page."
    name= new_user.name
    fullname= new_user.fullname
    nickname= new_user.nickname
    success= "You have successfully installed"
    welcome= "You are seeing this page because you have not configured any root.\
    Move to app.py and customize the route according to your needs.\
    To find more information visit our documentation page."
    inp= inpp.TextInput()
    resp.html = app.template("home.html",context={"title": "Awesome Framework",
     "name": name, "fullname": fullname, "nickname": nickname, "success": success, "welcome": inp, })


# class LoginForm(Form):
#     #username= StringField('username', validators= [validators.input_required()])
#     #password= PasswordField('password', validators= [validators.input_required()])
#     username= StringField('username')
#     password= PasswordField('password')
#
# @app.route("/about", methods=['GET', 'POST'])
# def about_page(req, resp):
#     form= LoginForm()
#     if (form.validate()):
#         resp.text = "successfully submitted!"
#
#     resp.html = app.template("about.html", context={"name": "zuhair", 'form': form})
#


@app.route("/{age:d}")
def tell_age(req, resp, age):
    resp.text = f"Your age is {age}"


@app.route("/{name:l}")
class GreetingHandler:
    def get(self, req, resp, name):
        resp.text = f"Hello, {name}"


@app.route("/show/template")
def handler_with_template(req, resp):
    resp.html = app.template("example.html", context={"title": "Awesome Framework", "body": "welcome to the future!"})


@app.route("/json")
def json_handler(req, resp):
    resp.json = {"this": "is JSON",}


@app.route("/custom")
def custom_response(req, resp):
    resp.body = b'any other body'
    resp.content_type = "text/plain"
