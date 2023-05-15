import flask
from flask import Flask, Response
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)
parser = reqparse.RequestParser()


@app.route('/')
def home():
    return flask.render_template('html/mainpage.html')


'''
class mainpage(Resource):
    def get(self):
        return flask.render_template('D:\Projects\InternetRadio\src\html\mainpage.html')


@app.route("/music")
def streamCountry():
    def generate():
        with open("music/Yousei Teikoku - Autoscopy.mp3", "rb") as country:
            data = country.read(1024)
            while data:
                yield data
                data = country.read(1024)
    return Response(generate(), mimetype="audio/mp3")
'''

if __name__ == "__main__":
    app.run(debug=True)