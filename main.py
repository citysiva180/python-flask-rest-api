# Learning python flask Rest -API
from flask import Flask
from flask_restful import Api, Resource


# Instance of a flask app  and wrapping the app in api
app = Flask(__name__)
api = Api(app)


# creation of class routes
class HelloWorld(Resource):
    def get(self):
        return{"data": "Hello World"}


api.add_resource(HelloWorld, "/helloworld")


# Check if the app is main, and start from there...
if __name__ == "__main__":
    app.run(debug=True)
