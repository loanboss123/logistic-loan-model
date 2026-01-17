import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder

def preprocess(lpd,loan_status):
   encoder=LabelEncoder()
   lpd['education']=encoder.fit_transform(lpd['education']
   lpd['self_employed']=encoder.fit_tranform(lpd['self_employed']
   lpd['loan_status']=encoder.fit_transform(lpd['loan_status']

y=lpd['loan_status']
x=lpd.drop(['loan_id'],['loan_status'],axis=1)

from sklearn.model_selection import train_test_split
train_x,test_x,train_y,test_y=train_test_split(x,y,random_state=78)

skewed_cols=['income_annum','loan_amount','residential_assets_value','commercial_assets_value',
             'luxury_assets_value','bank_asset_value']
def get_train_limits(lpd,columns):
     limits{}
     for col in columns:
     temp_log=np.log(lpd[col].clip(lower=1))
     Q1,Q3=temp_log.quantile([0.25],[0.75])
     IQR=Q3-Q1
     lower=Q1-1.5*IQR
     upper=Q3+1.5*IQR
     limits[col]={'lower':lower,'upper':upper}
   return limits

train_limits=get_train_limits(trainx,skewed_cols)

def apply preprocessing(lpd,column,limits):
  lpd_new=lpd.copy()
  for col in columns:
  lpd_new[f'{col}_log']=np.log(lpd_new[col].clip(lower=1))
  lower=limits[col]['lower']
  upper=limits[col]['upper']
  lpd_new[f'{col}_log']=lpd_new[f'{col}_log'].clip(lower=lower,upper=upper)
  lpd_new=lpd.drop(columns=[col])
return lpd_new

train_x_final=apply_preprocessing(train_x,skewed_cols,train_limits)
test_x_final=apply_preprocessing(test_x,skewed_cols,train_limits)

from sklearn.preprocessing import StandardScaler
scaler=StandardScaler()
scale_train_x_new=scaler.fit_transform(train_x_final)
scale_test_x_new=scaler.transform(test_x_final)
