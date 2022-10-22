from flask import Flask, render_template , request,redirect
import joblib

import pandas as pd
import numpy as np
import sklearn




def create_app():
    app = Flask(__name__)
    model = joblib.load('model.pkl')
    
    @app.route('/',methods=['GET', 'POST'])
    def index():
    
      
        return render_template('index.html')
    @app.route('/predict')
    def predict():
        return render_template('model.html')


    @app.route('/predict/ans',methods=['GET', 'POST'])
    def ans():
     if request.method == 'POST':
        pred_list=[]
        gu = request.form['자치구명']
        dong = request.form['법정동명']
        floor = request.form['층']
        apart = request.form['건물용도']

        pred_list.append((gu,dong,floor,apart))
        pred_df=pd.DataFrame(pred_list,columns=['자치구명','법정동명','층','건물용도'])

        # data = [gu , dong,floor,apart]
        # data_list=np.array(data).reshape(1,-1)
        prediction=  model.predict(pred_df)

        output=prediction[0]
        return render_template('result.html', prediction_text="내가 선택한 서울의 집값 예상금액은 {} 만원입니다.".format(output))


    @app.route('/dashbord',methods=['GET', 'POST'])
    def dash(): 

        return render_template('dash.html')



        


    return app



if __name__ == '__main__':
    app =create_app()
    app.run(debug = True)