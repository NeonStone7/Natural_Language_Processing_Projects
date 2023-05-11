import Flask
from flask import Flask, jsonify, request
from sklearn.externals import joblib


app = Flask(__name__)

@app.route('/index')
def index():
    return flask.render_template('index.html')

@app.route('/predict',methods = ['POST'])
def predict():
    model = joblib.load('model_text_class.joblib')
    to_predict=request.form.to_dict()
    review_text = to_predict_list['review_text']
    prediction = model.predict([review_text])
    
    if prediction[0]:
        prediction = 'Not COVID-19 related'
    else:
        prediction = 'COVID-19 related'
        
    return jsonify({'prediction':prediction})
if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 8080)