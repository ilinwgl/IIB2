#Load the csv file as data frame.
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

df = pd.read_csv('./Daten/weatherAUS.csv')
print('Size of weather data frame is :',df.shape)
#Let us see how our data looks like!

# We see there are some columns with null values. 
# Before we start pre-processing, let's find out which of the columns have maximum null values
df.count().sort_values()

# Features selection: We suppose that wind doesnt contribute to precipitation, so as the location and RISK_MM, 
# since we only want to predict wether it rains tommorrow in australian. The date is not important since we already 
# have RainTomorrow as target variable
df = df.drop(columns=['WindDir9am','WindDir3pm','WindGustDir','WindGustSpeed', 'Location','RISK_MM','Date'],axis=1)
df.shape

#Let us get rid of all null values in df
df = df.dropna(how='any') #将全部项都是nan的row删除
df.shape

#its time to remove the outliers in our data - we are using Z-score to detect and remove the outliers.
from scipy import stats
z = np.abs(stats.zscore(df._get_numeric_data())) 
# _get_numeric_data 去掉不是数字的列
#z-score标准化方法适用于属性A的最大值和最小值未知的情况，或有超出取值范围的离群数据的情况
print('z: ', z)
df= df[(z < 3).all(axis=1)] 
print(df.shape)

# Change categorical cloumns yes/no to 1/0 for RainToday and RainTomorrow
df['RainToday'].replace({'No': 0, 'Yes': 1},inplace = True)
df['RainTomorrow'].replace({'No': 0, 'Yes': 1},inplace = True)

# Standardize data - using MinMaxScaler
from sklearn import preprocessing
scaler = preprocessing.MinMaxScaler()
#调用fit方法，根据已有的训练数据创建一个标准化的转换器
scaler.fit(df)
#使用上面这个转换器去转换训练数据x,调用transform方法
df = pd.DataFrame(scaler.transform(df), index=df.index, columns=df.columns)

#now that we are done with the pre-processing part, let's see which are the important features for RainTomorrow!
#Using SelectKBest to get the top features!
from sklearn.feature_selection import SelectKBest,chi2,f_classif,mutual_info_classif
X = df.loc[:,df.columns!='RainTomorrow']
y = df[['RainTomorrow']]
#计算前5位得分最高的特征。f_classif可以替换成chi2(卡方检验)或mutual_info_classif(离散类别交互信息)
selector = SelectKBest(chi2, k=10)
selector.fit(X, y)         # Run score function on (X, y) and get the appropriate features.
X_new = selector.transform(X) # Reduce X to the selected features. (numpy.ndarray)
print ('Selected Columns: ', selector.get_support(indices=True))
print('Name: ', X.columns[selector.get_support(indices=True)]) #get_support Get a mask, or integer index, of the features selected

df = df[['Rainfall', 'WindSpeed9am', 'WindSpeed3pm', 'Humidity9am', 'Humidity3pm',
         'Pressure9am', 'Pressure3pm', 'Cloud9am', 'Cloud3pm', 'RainToday','RainTomorrow']] # rearrange columns
X = df[['Rainfall', 'WindSpeed9am', 'WindSpeed3pm', 'Humidity9am', 'Humidity3pm',
         'Pressure9am', 'Pressure3pm', 'Cloud9am', 'Cloud3pm', 'RainToday']] # Trainingsets
y = df[['RainTomorrow']] # Target Variable

#Random Forest Classifier 
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import time
t0=time.time()
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.25)
clf_rf = RandomForestClassifier(n_estimators=100, max_depth=4,random_state=0)
clf_rf.fit(X_train,y_train)
y_pred = clf_rf.predict(X_test)
score = accuracy_score(y_test,y_pred)
print('Random Forest Classifier: ')
print('Accuracy :',score)
print('Time taken :' , time.time()-t0)

#Decision Tree Classifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

t0=time.time()
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.25)
clf_dt = DecisionTreeClassifier(random_state=0)
clf_dt.fit(X_train,y_train)
y_pred = clf_dt.predict(X_test)
score = accuracy_score(y_test,y_pred)
print('Decision Tree Classifier: ')
print('Accuracy :',score)
print('Time taken :' , time.time()-t0)

#GaussianNB
from sklearn.naive_bayes import BernoulliNB
from sklearn.model_selection import train_test_split

t0=time.time()
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.25)
clf_ber = BernoulliNB()
clf_ber.fit(X_train,y_train)
y_pred = clf_ber.predict(X_test)
score = accuracy_score(y_test,y_pred)
print('BernoulliNB: ')
print('Accuracy :',score)
print('Time taken :' , time.time()-t0)




