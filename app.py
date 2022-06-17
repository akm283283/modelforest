from flask import Flask, request, render_template

import pickle


app = Flask(__name__)

@app.route('/')
def choose_prediction_method():
    #return render_template('main.html')
    return render_template('upr.html')


def upr_prediction(params):   
    model = pickle.load (open('models/model_RandomForestRegressor.pkl', 'rb'))
    pred = model.predict([params])
    return pred


@app.route('/upr/', methods=['POST', 'GET'])
def upr_predict():
    message = ''
    if request.method == 'POST':
        param_list = ('mn', 'plot', 'mup', 'ko', 'seg', 'tv', 'pp', 'pr', 'ps', 'yn', 'shn', 'pln')
        params = []
        for i in param_list:
            param = request.form.get(i)
            params.append(param)
        params = [float(i.replace(',', '.')) for i in params]

        message = f'Спрогнозированное значение Модуля упругости при растяжении для введенных параметров: {upr_prediction(params)} ГПа'
    return render_template('upr.html', message=message)

if __name__ == '__main__':
    app.run()