import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, date, timedelta
from dateutil.relativedelta import relativedelta
from pandas.io import json
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV

def predict():
    sdt = "01.07.2022 0:00:00"
    edt = "01.08.2022 0:00:00"
    arg = '[{"Id":1,"Date":"2021-08-03","Hour":0},{"Id":5120,"Date":"2022-01-02","Hour":0},{"Id":5121,"Date":"2020-11-03","Hour":0},{"Id":5122,"Date":"2020-05-07","Hour":0},{"Id":5123,"Date":"2020-05-09","Hour":0},{"Id":5124,"Date":"2020-12-11","Hour":0},{"Id":5125,"Date":"2020-06-11","Hour":0},{"Id":5126,"Date":"2020-06-07","Hour":0},{"Id":5127,"Date":"2020-12-07","Hour":0},{"Id":5128,"Date":"2020-12-09","Hour":0},{"Id":5129,"Date":"2020-12-03","Hour":0},{"Id":5130,"Date":"2020-04-09","Hour":0},{"Id":5131,"Date":"2020-04-03","Hour":0},{"Id":5133,"Date":"2020-10-11","Hour":0},{"Id":5134,"Date":"2020-05-03","Hour":0},{"Id":5135,"Date":"2020-04-11","Hour":0},{"Id":5136,"Date":"2020-05-11","Hour":0},{"Id":5137,"Date":"2020-11-09","Hour":0},{"Id":5138,"Date":"2020-11-07","Hour":0},{"Id":5139,"Date":"2022-05-02","Hour":0},{"Id":5140,"Date":"2022-07-02","Hour":0},{"Id":5141,"Date":"2020-07-07","Hour":0},{"Id":5142,"Date":"2020-07-09","Hour":0},{"Id":5143,"Date":"2020-06-03","Hour":0},{"Id":5144,"Date":"2020-07-03","Hour":0},{"Id":5145,"Date":"2020-06-09","Hour":0},{"Id":5146,"Date":"2020-11-11","Hour":0},{"Id":5147,"Date":"2022-02-02","Hour":0},{"Id":5148,"Date":"2022-03-02","Hour":0},{"Id":5149,"Date":"2022-04-02","Hour":0},{"Id":5150,"Date":"2020-08-09","Hour":0},{"Id":5151,"Date":"2020-08-11","Hour":0},{"Id":5152,"Date":"2020-01-07","Hour":0},{"Id":5153,"Date":"2020-08-03","Hour":0},{"Id":5154,"Date":"2020-01-03","Hour":0},{"Id":5155,"Date":"2020-03-07","Hour":0},{"Id":5156,"Date":"2020-10-07","Hour":0},{"Id":5157,"Date":"2020-10-03","Hour":0},{"Id":5158,"Date":"2020-03-11","Hour":0},{"Id":5159,"Date":"2020-09-09","Hour":0},{"Id":5160,"Date":"2020-03-09","Hour":0},{"Id":5161,"Date":"2020-10-09","Hour":0},{"Id":5162,"Date":"2020-04-07","Hour":0},{"Id":5163,"Date":"2020-09-11","Hour":0},{"Id":5164,"Date":"2020-02-09","Hour":0},{"Id":5165,"Date":"2020-09-03","Hour":0},{"Id":5166,"Date":"2020-08-07","Hour":0},{"Id":5167,"Date":"2020-01-11","Hour":0},{"Id":5168,"Date":"2020-02-07","Hour":0},{"Id":5169,"Date":"2020-02-11","Hour":0},{"Id":5170,"Date":"2020-03-03","Hour":0},{"Id":5171,"Date":"2020-02-03","Hour":0},{"Id":5172,"Date":"2020-09-07","Hour":0},{"Id":5173,"Date":"2022-06-02","Hour":0},{"Id":5178,"Date":"2020-01-09","Hour":0},{"Id":5179,"Date":"2020-07-11","Hour":0},{"Id":5180,"Date":"2021-05-03","Hour":0},{"Id":5181,"Date":"2021-09-07","Hour":0},{"Id":5182,"Date":"2021-01-05","Hour":0},{"Id":5183,"Date":"2021-01-03","Hour":0},{"Id":5184,"Date":"2021-08-07","Hour":0},{"Id":5185,"Date":"2021-09-03","Hour":0},{"Id":5186,"Date":"2021-02-03","Hour":0},{"Id":5187,"Date":"2021-02-02","Hour":0},{"Id":5188,"Date":"2021-09-09","Hour":0},{"Id":5189,"Date":"2021-02-09","Hour":0},{"Id":5190,"Date":"2021-01-09","Hour":0},{"Id":5191,"Date":"2021-01-07","Hour":0},{"Id":5192,"Date":"2021-07-09","Hour":0},{"Id":5193,"Date":"2021-02-05","Hour":0},{"Id":5194,"Date":"2021-02-07","Hour":0},{"Id":5195,"Date":"2021-07-05","Hour":0},{"Id":5196,"Date":"2021-06-05","Hour":0},{"Id":5197,"Date":"2021-12-07","Hour":0},{"Id":5198,"Date":"2021-06-07","Hour":0},{"Id":5199,"Date":"2021-06-09","Hour":0},{"Id":5200,"Date":"2021-06-03","Hour":0},{"Id":5201,"Date":"2021-12-09","Hour":0},{"Id":5202,"Date":"2021-08-09","Hour":0},{"Id":5203,"Date":"2021-08-02","Hour":0},{"Id":5204,"Date":"2021-08-05","Hour":0},{"Id":5205,"Date":"2021-07-07","Hour":0},{"Id":5206,"Date":"2021-07-03","Hour":0},{"Id":5207,"Date":"2021-09-05","Hour":0},{"Id":5208,"Date":"2021-01-02","Hour":0},{"Id":5209,"Date":"2021-09-02","Hour":0},{"Id":5210,"Date":"2021-10-05","Hour":0},{"Id":5211,"Date":"2021-06-02","Hour":0},{"Id":5212,"Date":"2021-10-09","Hour":0},{"Id":5213,"Date":"2021-05-09","Hour":0},{"Id":5214,"Date":"2021-10-03","Hour":0},{"Id":5215,"Date":"2021-10-07","Hour":0},{"Id":5216,"Date":"2021-12-02","Hour":0},{"Id":5217,"Date":"2021-11-02","Hour":0},{"Id":5218,"Date":"2021-11-09","Hour":0},{"Id":5219,"Date":"2021-11-07","Hour":0},{"Id":5220,"Date":"2021-11-05","Hour":0},{"Id":5221,"Date":"2021-12-03","Hour":0},{"Id":5222,"Date":"2021-11-03","Hour":0},{"Id":5223,"Date":"2021-05-02","Hour":0},{"Id":5224,"Date":"2021-07-02","Hour":0},{"Id":5225,"Date":"2021-12-05","Hour":0},{"Id":5226,"Date":"2021-03-09","Hour":0},{"Id":5227,"Date":"2021-04-05","Hour":0},{"Id":5228,"Date":"2021-04-02","Hour":0},{"Id":5229,"Date":"2021-03-02","Hour":0},{"Id":5230,"Date":"2021-03-03","Hour":0},{"Id":5231,"Date":"2021-03-05","Hour":0},{"Id":5232,"Date":"2021-03-07","Hour":0},{"Id":5233,"Date":"2021-04-07","Hour":0},{"Id":5234,"Date":"2021-05-07","Hour":0},{"Id":5235,"Date":"2021-04-09","Hour":0},{"Id":5236,"Date":"2021-10-02","Hour":0},{"Id":5237,"Date":"2021-04-03","Hour":0},{"Id":5238,"Date":"2021-05-05","Hour":0}]'

    start_date, end_date = datetime.strptime(sdt, '%d.%m.%Y %H:%M:%S'), datetime.strptime(edt, '%d.%m.%Y %H:%M:%S')
    json_received = arg

    df = pd.read_json(json_received)
    X = pd.DataFrame()
    y = df['Hour'].values
    day = [] 
    month = [] 
    year = [] 
    for i, row in df.iterrows():
        row_date = row['Date'].date()
        day.append(row_date.day)
        month.append(row_date.month)
        year.append(row_date.year)
    X['day'] = day
    X['month'] = month
    X['year'] = year

    knn = KNeighborsClassifier()
    param_grid = {'n_neighbors': np.arange(3, 4)}
    knn_gscv = GridSearchCV(knn, param_grid, cv=4)
    knn_gscv.fit(X, y)
    knn.n_neighbors = knn_gscv.best_params_['n_neighbors']
    knn.fit(X.values, y)

    df_prediction = pd.DataFrame(columns=['Date','Hour','Probability'])

    unique, counts = np.unique(y, return_counts=True)

    for row in pd.date_range(start=start_date, end=end_date):
        row = row.strftime('%d.%m.%Y %H:%M:%S')
        for hour_index, proba in enumerate(knn.predict_proba([[row_date.day, row_date.month, row_date.year]])[0]):
                if proba:
                    new_row = {'Date': row,'Hour' : int(unique[hour_index]),'Probability' : proba}
                    df_prediction = df_prediction.append(new_row, ignore_index=True)

    return df_prediction.to_json(orient="records")
    return python_version()

print(predict())
