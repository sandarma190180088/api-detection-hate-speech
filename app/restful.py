from app import api,app,request
from flask_restful import Resource
import joblib

model = joblib.load('model_naive_bayes_v2.sav')
class Main(Resource):
    def get(self):
        return {'msg':'Detection Hate Speech v1','status':True},200
    def post(self):
        text = request.form['text']
        predict = model.predict([text])
        if predict[0] == 0:
            resp = 'Hate Speech'
        elif predict[0] == 1:
            resp = "Offensive Language"
        else:
            resp = "Neither"

        return {'response':resp,'status':True},200


api.add_resource(Main,'/hate-speech')
        
        





