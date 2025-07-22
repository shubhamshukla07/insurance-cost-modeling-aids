import numpy as np
import pandas as pd
import matplotlib.pylab as plt
import seaborn as sns
import warnings 
warnings.filterwarnings("ignore")
df=pd.read_csv("insurance.csv")

#1:EDA
print(df.shape)
print(df.head())
print(df.info())
print(df.describe())
print(df.isnull().sum())

numeric_columns=["age","bmi","children","charges"]
 for i in numeric_columns:
     sns.histplot(df[i],kde=True)
     plt.show()


#for qualatative data
sns.countplot(x=df["children"])
sns.countplot(x=df["sex"],hue=df["smoker"])
sns.countplot(x=df["smoker"])
plt.show()


#box plot
for i in numeric_columns:
    sns.boxplot(x=df[i])
    plt.show()

#for getting correlation btwn inputs and outputs
 sns.heatmap(df.corr(numeric_only=True),annot=True)
 plt.show()


#2: Data Cleaning and preprocessing
df_cleaned=df.copy()
df_cleaned.drop_duplicates(inplace=True)
print("before",df.shape,"after: ",df_cleaned.shape)
print(df_cleaned.isnull().sum())



#coverting qulatative into numbers
#1:Label Enconding
print(df_cleaned["sex"].value_counts())
df_cleaned["sex"]=df_cleaned["sex"].map({"male":0,"female":1})
df_cleaned["smoker"]=df_cleaned["smoker"].map({"yes":1,"no":0})
df_cleaned.rename(columns={"sex":"is_male","smoker":"is_smoker"},inplace=True)

#2:One Hot Encoding
print(df_cleaned["region"].value_counts())
df_cleaned=pd.get_dummies(df_cleaned,columns=["region"],drop_first=True)
df_cleaned=df_cleaned.astype(int)
print(df_cleaned.head())



#Feature Engeering and Extraction
#1.Feature Engeering
df_cleaned["bmi_category"]=pd.cut(df_cleaned["bmi"],bins=[0,18.5,24.9,29.9,float('inf')],labels=["Underweight","Normal","Overweight","Obese"])
df_cleaned=pd.get_dummies(df_cleaned,columns=["bmi_category"],drop_first=True)
df_cleaned=df_cleaned.astype(int)
print(df_cleaned.head())

#adjecting/converting large values to small 
from sklearn.preprocessing import StandardScaler
cols=["age","bmi","children"]
scaler=StandardScaler()
df_cleaned[cols]=scaler.fit_transform(df_cleaned[cols])
print(df_cleaned)

#2.Feature Extraction
sns.heatmap(df_cleaned.corr(),annot=True)
plt.show()

#checking correlation again target column(charges )
featured_selection=df_cleaned.corr()['charges'].sort_values(ascending=False)
print(featured_selection)

# for checking is the correlation correct of categorical columns which we got from df.corr()
from scipy.stats import pointbiserialr
alpha=0.05
categorial=["region_northwest","region_southwest","is_male","bmi_category_Normal","bmi_category_Overweight"]
for i in categorial:
    r, p = pointbiserialr(df_cleaned[i], df_cleaned['charges'])
    print(f"Correlation: {r:.3f}, P-value: {p:.4f}")
    if p<=alpha:
        print(i,"important")
    else:
        print(i,"remove")
        
#final data after everything
final_dataFrame=df[["age","is_male","children","is_smoker","charges","region_southeast","bmi",   "bmi_category_Normal",
    "bmi_category_Overweight",
    "bmi_category_Obese"
]]


