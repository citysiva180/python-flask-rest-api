# Learning python flask Rest -API
from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    pass


if __name__ == "__main__":
    app.run(debug=True)
