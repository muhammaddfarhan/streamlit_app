import streamlit as st
import plotly.graph_objects as go
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px 
st.set_page_config(page_title="Dashboard", page_icon=":bar_chart:", layout="wide")

st.markdown("<h1 style='text-align: center; color: Black; '><u>Toyota Monthly Report</u></h1>", unsafe_allow_html=True )


df = pd.read_excel('dataframe.xlsx')


fig = go.Figure(data=[go.Table(
    columnwidth = [250],
    header=dict(values=list(df.columns),
                fill_color='Light Grey',
                align='center',
                height = 40),
    cells=dict(values=df.values.T,
               fill_color='light Blue',
               align='center',
                height = 50))
])



with st.container():
    fig.update_layout(width = 1600 , height = 480)
    st.write(fig)
    
    

with st.container():
    col2 , col3, col4 , col5 = st.columns(4)
    with col2:
        st.write("<h5 style='text-align: center; color: Black;'>YEAR WISE ENGAGEMENTS</h5>", unsafe_allow_html=True)
        st.write("<p style='text-align: center; color: Black;'>33,597</p>", unsafe_allow_html=True)
    with col3:
        st.write("<h5 style='text-align: center; color: Black;'>YEAR WISE IMPRESSIONS</h5>", unsafe_allow_html=True)
        st.write("<p style='text-align: center; color: Black;'>3,273,364</p>", unsafe_allow_html=True)
    with col4:
        st.write("<h5 style='text-align: center; color: Black;'>YEAR WISE ACIIVE TEXTERS</h5>", unsafe_allow_html=True)
        st.write("<p style='text-align: center; color: Black;'>5,717</p>", unsafe_allow_html=True)
    with col5:
        st.write("<h5 style='text-align: center; color: Black;'>YEAR WISE TEXTERS</h5>", unsafe_allow_html=True)
        st.write("<p style='text-align: center; color: Black;'>17,283</p>", unsafe_allow_html=True)
    st.write('\n') 
st.markdown("<h1 style='text-align: center; color: White;background-color:Black '>OVERALL ENGAGEMENT TRENDS</h1>", unsafe_allow_html=True )

with st.container():
    st.write('\n')
    col2 , col3, col4 , col5 = st.columns(4)
    with col2:
        st.write("<h5 style='text-align: left; color: Black;'>INQUIRY:  <span style='font-weight:normal'>57</span></h5>", unsafe_allow_html=True)
    with col3:
        st.write("<h5 style='text-align: left; color: Black;'>COMPLAINTS:  <span style='font-weight:normal'>8</span></h5>", unsafe_allow_html=True)
    with col4:
        st.write("<h5 style='text-align: left; color: Black;'>SUGGESTION:  <span style='font-weight:normal'>0</span></h5>", unsafe_allow_html=True)
    with col5:
        st.write("<h5 style='text-align: left; color: Black;'>COMPLIMENT:  <span style='font-weight:normal'>0</span></h5>", unsafe_allow_html=True)

with st.container():
    st.write('\n')
    col2 , col3 = st.columns(2)
    with col2:
        st.write("<h5 style='text-align: CENTER; color: Black;'>DEALERSHIP</h5>", unsafe_allow_html=True)
        st.write('\n\n\n')
        chart_data = pd.DataFrame(
        np.random.normal(5,1,7),
        columns=["a"])
    
        st.bar_chart(chart_data)
    with col3:
        st.write("<h5 style='text-align: CENTER; color: Black;'>GENDER</h5>", unsafe_allow_html=True)
        labels = 'Male', 'Female'
        sizes = [10, 3]
        explode = (0, 0.1)  # only "explode" the 2nd slice (i.e. 'Hogs')
        
        fig1, ax1 = plt.subplots(figsize=(5, 2))
        ax1.pie(sizes, labels=labels, autopct='%1.1f%%' , shadow = True , explode=explode)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        
        st.pyplot(fig1)
with st.container():
    col2 , col3 = st.columns(2)
    with col2:
        st.write("<h5 style='text-align: CENTER; color: Black;'>CITY</h5>", unsafe_allow_html=True)
        st.write('\n\n\n')
        chart_data = pd.DataFrame(
        np.random.normal(5,1,9),
        columns=["a"])
    
        st.bar_chart(chart_data)
    with col3:
        st.write("<h5 style='text-align: CENTER; color: Black;'>VARIANT</h5>", unsafe_allow_html=True)
        st.write('\n\n\n')
        chart_data = pd.DataFrame(
        np.random.normal(5,1,6),
        columns=["a"])
    
        st.bar_chart(chart_data)
with st.container():
    col2 , col3 = st.columns(2)
    with col2:
        st.write("<h5 style='text-align: CENTER; color: Black;'>INQUIRIES</h5>", unsafe_allow_html=True)
        st.write('\n\n\n')
        chart_data = pd.DataFrame(
        np.random.normal(5,1,8),
        columns=["a"])
    
        st.bar_chart(chart_data)
    with col3:
        st.write("<h5 style='text-align: CENTER; color: Black;'>COMPLAINTS</h5>", unsafe_allow_html=True)
        st.write('\n\n\n')
        chart_data = pd.DataFrame(
        np.random.normal(5,1,5),
        columns=["a"])
    
        st.bar_chart(chart_data)      
        
st.markdown("<h1 style='text-align: center; color: White;background-color:Black '>ONGOING SERVICES</h1>", unsafe_allow_html=True )
st.write('\n')
st.markdown("<h2 style='text-align: center; color: White;background-color:#094099 '>CONNECT SERVICE</h2>", unsafe_allow_html=True )

with st.container():
    st.write('\n')
    col2 , col3= st.columns(2)
    with col2:
        st.write("<h5 style='text-align: left; color: Black;'>TEXT MESSAGE SENT: <span style='font-weight:normal'>356</span></h5>", unsafe_allow_html=True)
    with col3:
        st.write("<h5 style='text-align: right; color: Black;'>CUSTOMERS ENGAGED:  <span style='font-weight:normal'>178</span></h5>", unsafe_allow_html=True)
   
with st.container():
    st.write('\n')
    st.write('\n')
    col2 , col3= st.columns(2)
    with col2:
        st.write("<h5 style='text-align: center; color: Black;'>CONNECT ACTIVATION (JULY - SEPTEMBER)</h5>", unsafe_allow_html=True)
        st.write("<p style='text-align: center; color: Black;font-size:1.5vw'>616</p>", unsafe_allow_html=True)
    with col3:
        st.write("<h5 style='text-align: center; color: Black;'>CONNECT ACTIVATION (SEPTEMBER)</h5>", unsafe_allow_html=True)
        st.write("<p style='text-align: center; color: Black;font-size:1.5vw'>178</p>", unsafe_allow_html=True)
    st.write('\n')
st.markdown("<h2 style='text-align: center; color: White;background-color:#094099 '>FIRST FREE SERVICE</h2>", unsafe_allow_html=True )

with st.container():
    st.write('\n')
    col2 , col3= st.columns(2)
    with col2:
        st.write("<h5 style='text-align: left; color: Black;'>TEXT MESSAGE SENT: <span style='font-weight:normal'>356</span></h5>", unsafe_allow_html=True)
    with col3:
        st.write("<h5 style='text-align: right; color: Black;'>CUSTOMERS ENGAGED:  <span style='font-weight:normal'>178</span></h5>", unsafe_allow_html=True)

with st.container():
    st.write('\n')
    col1 ,col2 , col3 = st.columns(3)
    with col1:
        st.write("<h5 style='text-align: CENTER; color: Black;'>AVAILED OR NOT</h5>", unsafe_allow_html=True)
        st.write('\n\n\n')
        chart_data = pd.DataFrame(
        np.random.normal(5,1,2),
        columns=["a"])
    
        st.bar_chart(chart_data)
    with col2:
        st.write("<h5 style='text-align: CENTER; color: Black;'>SERVICE EXPERIENCE</h5>", unsafe_allow_html=True)
        st.write('\n\n\n')
        chart_data = pd.DataFrame(
        np.random.normal(5,1,10),
        columns=["a"])
    
        st.bar_chart(chart_data)
    with col3:
        st.write("<h5 style='text-align: CENTER; color: Black;'>REASON FOR NOT AVAILING</h5>", unsafe_allow_html=True)
        st.write('\n\n\n')
        chart_data = pd.DataFrame(
        np.random.normal(5,1,5),
        columns=["a"])
    
        st.bar_chart(chart_data)      
    
st.markdown("<h2 style='text-align: center; color: White;background-color:#094099 '>WARRANTY ACTIVATION SERVICE</h2>", unsafe_allow_html=True )

with st.container():
    st.write('\n')
    col2 , col3= st.columns(2)
    with col2:
        st.write("<h5 style='text-align: left; color: Black;'>TEXT MESSAGE SENT: <span style='font-weight:normal'>238</span></h5>", unsafe_allow_html=True)
    with col3:
        st.write("<h5 style='text-align: right; color: Black;'>CUSTOMERS ENGAGED:  <span style='font-weight:normal'>98</span></h5>", unsafe_allow_html=True)
   
with st.container():
    st.write('\n')
    st.write('\n')
    col2 , col3= st.columns(2)
    with col2:
        st.write("<h5 style='text-align: center; color: Black;'>VERIFICATION</h5>", unsafe_allow_html=True)
        st.write("<p style='text-align: center; color: Black;font-size:1.5vw'>98</p>", unsafe_allow_html=True)
    with col3:
        st.write("<h5 style='text-align: center; color: Black;'>ACTIVATION</h5>", unsafe_allow_html=True)
        st.write("<p style='text-align: center; color: Black;font-size:1.5vw'>79</p>", unsafe_allow_html=True)
    st.write('\n')


st.markdown("<h2 style='text-align: center; color: White;background-color:#094099 '>VEHICLE ANNIVERSARY</h2>", unsafe_allow_html=True )

with st.container():
    st.write('\n')
    col2 , col3= st.columns(2)
    with col2:
        st.write("<h5 style='text-align: left; color: Black;'>TEXT MESSAGE SENT: <span style='font-weight:normal'>6425</span></h5>", unsafe_allow_html=True)
    with col3:
        st.write("<h5 style='text-align: right; color: Black;'>CUSTOMERS ENGAGED:  <span style='font-weight:normal'>2038</span></h5>", unsafe_allow_html=True)
   
with st.container():
    col1 ,col2  = st.columns(2)
    with col1:
        st.write("<h5 style='text-align: CENTER; color: Black;'>AVAILED OR NOT</h5>", unsafe_allow_html=True)
        st.write('\n\n\n')
        df = pd.DataFrame()
        df['total_bill'] = [20.42,13.54,25.43,22,10]
        df['day'] = ['Sun' , 'Mon' , 'Sat' , 'Fri' , 'Thurs']
        
        fig=px.bar(df,x='total_bill',y='day', orientation='h')
        st.write(fig)

    with col2:
        st.write("<h5 style='text-align: CENTER; color: Black;'>SERVICE EXPERIENCE</h5>", unsafe_allow_html=True)
        st.write('\n\n\n')
        chart_data = pd.DataFrame(
        np.random.normal(5,1,10),
        columns=["a"])
        st.bar_chart(chart_data)      

st.markdown("<h2 style='text-align: center; color: White;background-color:#094099 '>PROTECTION PLAN</h2>", unsafe_allow_html=True )

with st.container():
    st.write('\n')
    col2 , col3= st.columns(2)
    with col2:
        st.write("<h5 style='text-align: left; color: Black;'>TEXT MESSAGE SENT: <span style='font-weight:normal'>4415</span></h5>", unsafe_allow_html=True)
    with col3:
        st.write("<h5 style='text-align: right; color: Black;'>CUSTOMERS ENGAGED:  <span style='font-weight:normal'>1264</span></h5>", unsafe_allow_html=True)

st.markdown("<h2 style='text-align: center; color: #094099;background-color: '><U>INTERESTED TO BUY</U></h2>", unsafe_allow_html=True )

with st.container():
    st.write('\n')
    col2 , col3 = st.columns(2)
    with col2:
        st.write("<h5 style='text-align: CENTER; color: Black;'>INTERESTED TO BUY</h5>", unsafe_allow_html=True)
        labels = 'Yes', 'No'
        sizes = [7, 5]
        explode = (0, 0.1)  # only "explode" the 2nd slice (i.e. 'Hogs')
        
        fig1, ax1 = plt.subplots(figsize=(5, 2))
        ax1.pie(sizes, labels=labels, autopct='%1.1f%%' , shadow = True , explode=explode)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        
        st.pyplot(fig1)
        
    with col3:
        st.write("<h5 style='text-align: CENTER; color: Black;'>VARIANT</h5>", unsafe_allow_html=True)
        st.write('\n\n\n')
        chart_data = pd.DataFrame(
        np.random.normal(5,1,5),
        columns=["a"])
    
        st.bar_chart(chart_data)
    

with st.container():
    col2 , col3 = st.columns(2)
    with col2:
        st.write("<h5 style='text-align: CENTER; color: Black;'>DELARSHIP</h5>", unsafe_allow_html=True)
        st.write('\n\n\n')
        chart_data = pd.DataFrame(
        np.random.normal(5,1,8),
        columns=["a"])
    
        st.bar_chart(chart_data)
    with col3:
        st.write("<h5 style='text-align: CENTER; color: Black;'>CITY</h5>", unsafe_allow_html=True)
        st.write('\n\n\n')
        chart_data = pd.DataFrame(
        np.random.normal(5,1,5),
        columns=["a"])
    
        st.bar_chart(chart_data) 
        

st.markdown("<h2 style='text-align: center; color: #094099;background-color: '><U>INTERESTED TO OFFER</U></h2>", unsafe_allow_html=True )

with st.container():
    st.write('\n')
    col2 , col3 = st.columns(2)
    with col2:
        st.write("<h5 style='text-align: CENTER; color: Black;'>INTERESTED TO OFFER</h5>", unsafe_allow_html=True)
        labels = 'Yes', 'No'
        sizes = [8, 4]
        explode = (0, 0.1)  # only "explode" the 2nd slice (i.e. 'Hogs')
        
        fig1, ax1 = plt.subplots(figsize=(5, 2))
        ax1.pie(sizes, labels=labels, autopct='%1.1f%%' , shadow = True , explode=explode)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        
        st.pyplot(fig1)
        
    with col3:
        st.write("<h5 style='text-align: CENTER; color: Black;'>VARIANT</h5>", unsafe_allow_html=True)
        st.write('\n\n\n')
        chart_data = pd.DataFrame(
        np.random.normal(5,1,5),
        columns=["a"])
    
        st.bar_chart(chart_data)
    

with st.container():
    col2 , col3 = st.columns(2)
    with col2:
        st.write("<h5 style='text-align: CENTER; color: Black;'>DELARSHIP</h5>", unsafe_allow_html=True)
        st.write('\n\n\n')
        chart_data = pd.DataFrame(
        np.random.normal(5,1,8),
        columns=["a"])
    
        st.bar_chart(chart_data)
    with col3:
        st.write("<h5 style='text-align: CENTER; color: Black;'>CITY</h5>", unsafe_allow_html=True)
        st.write('\n\n\n')
        chart_data = pd.DataFrame(
        np.random.normal(5,1,5),
        columns=["a"])
    
        st.bar_chart(chart_data) 
        

st.markdown("<h2 style='text-align: center; color: #094099;background-color: '><U>DISINTERESTED TO BUYING</U></h2>", unsafe_allow_html=True )

with st.container():
    st.write('\n')
    col2 , col3 = st.columns(2)
    with col2:
        st.write("<h5 style='text-align: CENTER; color: Black;'>VARIANT</h5>", unsafe_allow_html=True)
        st.write('\n\n\n')
        chart_data = pd.DataFrame(
        np.random.normal(5,1,5),
        columns=["a"])
    
        st.bar_chart(chart_data)
        
    with col3:
        st.write('')
        

st.markdown("<h2 style='text-align: center; color:WHITE;background-color: #094099 '>LAUNCH OF FORTUNER 2022</h2>", unsafe_allow_html=True )
with st.container():
    st.write('\n')
    col2 , col3= st.columns(2)
    with col2:
        st.write("<h5 style='text-align: left; color: Black;'>TEXT MESSAGE SENT: <span style='font-weight:normal'>14</span></h5>", unsafe_allow_html=True)
    with col3:
        st.write("<h5 style='text-align: right; color: Black;'>CUSTOMERS ENGAGED:  <span style='font-weight:normal'>5</span></h5>", unsafe_allow_html=True)
with st.container():
    col2 , col3 = st.columns(2)
    with col2:
        st.write("<h5 style='text-align: CENTER; color: Black;'>VARIANT</h5>", unsafe_allow_html=True)
        st.write('\n\n\n')
        chart_data = pd.DataFrame(
        np.random.normal(5,1,1),
        columns=["a"])
    
        st.bar_chart(chart_data)
    with col3:
        st.write("<h5 style='text-align: CENTER; color: Black;'>DEALERSHIP</h5>", unsafe_allow_html=True)
        st.write('\n\n\n')
        chart_data = pd.DataFrame(
        np.random.normal(5,1,1),
        columns=["a"])
    
        st.bar_chart(chart_data) 

with st.container():
    st.write('\n')
    col2 , col3 = st.columns(2)
    with col2:
        st.write("<h5 style='text-align: CENTER; color: Black;'>CITY</h5>", unsafe_allow_html=True)
        st.write('\n\n\n')
        chart_data = pd.DataFrame(
        np.random.normal(5,1,1),
        columns=["a"])
    
        st.bar_chart(chart_data)
        
    with col3:
        st.write('')
        
        
        
st.markdown("<h2 style='text-align: center; color:WHITE;background-color: #094099 '>LAUNCH OF REVO 2022</h2>", unsafe_allow_html=True )
with st.container():
    st.write('\n')
    col2 , col3= st.columns(2)
    with col2:
        st.write("<h5 style='text-align: left; color: Black;'>TEXT MESSAGE SENT: <span style='font-weight:normal'>29</span></h5>", unsafe_allow_html=True)
    with col3:
        st.write("<h5 style='text-align: right; color: Black;'>CUSTOMERS ENGAGED:  <span style='font-weight:normal'>4</span></h5>", unsafe_allow_html=True)

with st.container():
    col2 , col3 = st.columns(2)
    with col2:
        st.write("<h5 style='text-align: CENTER; color: Black;'>VARIANT</h5>", unsafe_allow_html=True)
        st.write('\n\n\n')
        chart_data = pd.DataFrame(
        np.random.normal(5,1,1),
        columns=["a"])
    
        st.bar_chart(chart_data)
    with col3:
        st.write("<h5 style='text-align: CENTER; color: Black;'>DEALERSHIP</h5>", unsafe_allow_html=True)
        st.write('\n\n\n')
        chart_data = pd.DataFrame(
        np.random.normal(5,1,1),
        columns=["a"])
    
        st.bar_chart(chart_data) 

with st.container():
    st.write('\n')
    col2 , col3 = st.columns(2)
    with col2:
        st.write("<h5 style='text-align: CENTER; color: Black;'>CITY</h5>", unsafe_allow_html=True)
        st.write('\n\n\n')
        chart_data = pd.DataFrame(
        np.random.normal(5,1,1),
        columns=["a"])
    
        st.bar_chart(chart_data)
        
    with col3:
        st.write('')

st.markdown("<h1 style='text-align: center; color: White;background-color:Black '>MARKETING CAMPAIGNS</h1>", unsafe_allow_html=True )

with st.container():
    st.write('\n')
    st.write('\n')
    col2 , col3 = st.columns(2)
    with col2:
        st.write("<h5 style='text-align: left; color: Black;'>Date: 03/08/2022</h5>", unsafe_allow_html=True)
        st.write("<h5 style='text-align: CENTER; color: Black;'><u>Toyota Customer Refund</u></h5>", unsafe_allow_html=True)
        st.write('\n')
        st.write('\n')
        st.write("<p style='text-align: CENTER; color: Black;'>ENGAGEMENTS</p>", unsafe_allow_html=True)
        st.write("<p style='text-align: CENTER; color: Black;'>17</p>", unsafe_allow_html=True)
        st.write("<p style='text-align: CENTER; color: Black;'>ACTIVE TALKERS</p>", unsafe_allow_html=True)
        st.write("<p style='text-align: CENTER; color: Black;'>3</p>", unsafe_allow_html=True)
        st.write("<p style='text-align: CENTER; color: Black;'>TALKERS REACHED</p>", unsafe_allow_html=True)
        st.write("<p style='text-align: CENTER; color: Black;'>167</p>", unsafe_allow_html=True)
        st.write("<h5 style='text-align: CENTER; color: Black;'>TEXT MESSAGE SENT: <span style='font-weight:normal'>343</span></h5>", unsafe_allow_html=True)
    with col3:
        st.write('')
