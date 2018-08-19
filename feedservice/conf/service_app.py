from flask import Flask
from flask_restful import Api

from feedservice.service_apis.question import Question

app=False(__name__)

api=Api(app=app,prefix='/feedservice/')

api.add_resource(Question,'question')


if __name__== "__main__":

    app.run(host='localhost',port=2005,debug=True)