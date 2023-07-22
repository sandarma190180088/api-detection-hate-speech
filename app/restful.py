from app import api,app,request
from keras.models import model_from_json
from keras.preprocessing.text import Tokenizer
from keras.utils import pad_sequences
import pandas as pd

from flask_restful import Resource

with open('cnn_model.json','r') as m:
    load_model = m.read()

model = model_from_json(load_model)
model.load_weights('cnn_weights.h5')

tokenizer = Tokenizer()

X_train = pd.read_csv('X_train_v1.csv')['stopwords']
tokenizer.fit_on_texts(X_train)





class Main(Resource):
    def get(self):
        return {'msg':'Detection Hate Speech v1','status':True},200
    def post(self):
        text = request.form['text']
        seq = tokenizer.texts_to_sequences(texts=[text])
        pad = pad_sequences(seq,maxlen=20)
        pred = model.predict(pad)

        pred = {'hate-speech':float(pred[0][0]),'offensive-lang':float(pred[0][1]),'neither':float(pred[0][2])}


        return {'response':pred,'status':True},200


api.add_resource(Main,'/hate-speech/')
        
        





