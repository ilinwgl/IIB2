import warnings
warnings.filterwarnings("ignore")

import pandas as pd
orig_data = pd.read_csv("./Daten/Concrete_Data_Yeh.csv")
orig_data.head()

orig_data = orig_data.drop(columns=['superplasticizer'],axis=1)

data = orig_data.copy()
data['cement'] = data['cement']*1.1
data['water'] = data['water']*1.1
data.shape

data.info()

data.describe().T
data.head()


from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
sm = scatter_matrix(data, figsize=(15,15), diagonal = 'kde')
#Changing label rotation
[s.xaxis.label.set_rotation(45) for s in sm.reshape(-1)]
[s.yaxis.label.set_rotation(45) for s in sm.reshape(-1)]
#Changing offset for label
[s.get_yaxis().set_label_coords(-0.5,0.5) for s in sm.reshape(-1)]
#Hiding ticks
[s.set_xticks(()) for s in sm.reshape(-1)]
[s.set_yticks(()) for s in sm.reshape(-1)]
plt.show()

import seaborn as sns
sns.heatmap(data.corr().abs())
plt.show()

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(data[data.columns[:-1]],
                                                    data[[data.columns[-1]]],
                                                    test_size = 0.2,
                                                    random_state = 1)

#训练数据预处理
# Scale the features
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler().fit(X_train)
X_train_scaled = pd.DataFrame(scaler.transform(X_train),
                              columns = X_train.columns)

X_train_scaled.head()

#测试数据划分 
#We will save the model performance metrics in a DataFrame
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import KFold, cross_val_score
import numpy as np
Model = []
RMSE = []
R_sq = []
cv = KFold(5, random_state = 1)

#验证方法确定 
#Creating a Function to append the cross validation scores of the algorithms
def input_scores(name, model, x, y):
    Model.append(name)
    RMSE.append(np.sqrt((-1) * cross_val_score(model, x, y, cv=cv, 
                                               scoring='neg_mean_squared_error').mean()))
    R_sq.append(cross_val_score(model, x, y, cv=cv, scoring='r2').mean())


from sklearn.ensemble import RandomForestRegressor

names = [ 'Random Forest Regressor']
models = [ RandomForestRegressor()]

#Running all algorithms
for name, model in zip(names, models):
    input_scores(name, model, X_train_scaled, y_train)

    #评估结果    
evaluation = pd.DataFrame({'Model': Model,
                           'RMSE': RMSE,
                           'R Squared': R_sq})
print("FOLLOWING ARE THE TRAINING SCORES: ")
evaluation

#applying this model on test data
X_test_scaled = pd.DataFrame(scaler.transform(X_test),
                             columns = X_test.columns)

algorithm = RandomForestRegressor(n_estimators=460, max_depth=20, oob_score=True, 
                                min_samples_split=170)
clf = algorithm.fit(X_train_scaled, y_train)
prection = algorithm.predict(X_test)

prediction = pd.DataFrame(prection)

print(prediction[0])
print("Test RMSE: ", np.sqrt(mean_squared_error(y_test, clf.predict(X_test_scaled))))
print("Test R^2: ", r2_score(y_test, clf.predict(X_test_scaled)))