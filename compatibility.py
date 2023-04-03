import pandas as pd
import csv
import streamlit as st

df=pd.read_csv('./content./dataset.csv')

#dropping null values
df.dropna(how='all',axis=1,inplace=True)



#reading the user input
pettype=st.selectbox('type of pet:',list(df['PET'].unique()))
breed=st.selectbox('breed:',list(df[df['PET']==pettype]['BREED'].unique()))
age=st.selectbox('age of your pet:',list(df[df['BREED']==breed]['AGE']))
dfr=df[df['BREED']==breed][['GENDER','AGE']]
gender=st.selectbox('gender of pet:',list(dfr[dfr['AGE']==age]['GENDER'].unique()))
expense=st.slider(label='expense per month',min_value=2000,max_value=30000,step=100)

#extracting expense from the dataset 
dfr=df[df['BREED']==breed][['GENDER','EXPENSES','AGE']]
dfrr=dfr[dfr['AGE']==age][['GENDER','EXPENSES']]
exp=dfrr[dfrr['GENDER']==gender]['EXPENSES'].tolist()
expf=exp[0]
#st.text(expf)
#comparing the required expense and the amount the user has specified
def compare():
    if(expense<expf):
        amount=expf-expense
        st.text_area(label='Results: ',placeholder='You need to invest '+str(amount)+' more \n No compatibility, please allocate more responses for the maintenance of the pet')
    
    else:
        st.text_area(label='Results: ',placeholder='Compatible, you may go ahead with the adoption!')

if st.button(label='compare',type='primary',disabled=False,use_container_width=True):
    compare()


