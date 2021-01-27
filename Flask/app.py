# code adapted from lesson 5.09

import pickle
import numpy as np
import pandas as pd
from flask import Flask, request, Response, render_template, jsonify

app = Flask('myApp')

# route 1: form
@app.route('/',methods=['GET'])
def home():
    # return a simple string
    return render_template('form.html')


# route 2: accept the form submission and do something fancy with it
@app.route('/submit')
def make_predictions():
    with open('grailed_model_decTree.pkl', 'rb') as file:
        model = pickle.load(file)
    with open('model_columns.pkl', 'rb') as file:
        model_columns = pickle.load(file)
    # load in the form data from the incoming request
    user_input = request.args

    cat_str = str(user_input['category'])
    category = f'category_{cat_str}'

    des_str = str(user_input['designer'])
    designer = f'designer_{des_str}'

    size_str = str(user_input['size'])
    size = f'size_{size_str}'

    col_str = str(user_input['color'])
    color = f'color_{col_str}'

    user_list = [1,1,1,1,user_input['condition'],user_input['feedback_count'],user_input['image_count']]
    user_columns =[category,designer, size,color, 'condition','feedback_count','image_count']
    query = pd.DataFrame(data = [user_list], columns=user_columns, index=[0])

    #category_Sweatshirts & Hoodies ect needed
    #data = [str(user_input['designer'])]

    #query = pd.DataFrame(user_dict ,index=[0])
    #query_df = pd.DataFrame(user_input ,index=[0])
    #query = pd.get_dummies(query_df)
    for col in model_columns:
        if col not in query.columns and col != 'condition' and col != 'feedback_count' and col !='image_count':
            query[col] = 0

    columns_model = []
    for col in model_columns:
        if 'category' in col:
            col = str(col).replace(' ','')
            columns_model.append(col)
        else:
            columns_model.append(col)

    for col in columns_model:
         if col not in columns_model:
              query[col] = 0

    query = query[model_columns]
    pred = model.predict(query)[0]

    return render_template('results.html', prediction = pred)

if __name__ == '__main__':
    app.run(debug=True)
