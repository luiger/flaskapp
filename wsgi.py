from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "Hola SIC"

if __name__ == "__main__":
    application.run()
