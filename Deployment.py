import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import streamlit as st


option = st.sidebar.selectbox("Pick a choice:",['Home','EDA'])
if option == "Home":
    df = pd.read_csv("company_sales_data.csv")
    st.write(df.head())
elif option == "EDA":
    df = pd.read_csv("company_sales_data.csv")
    st.header("Matplotlib")
    st.subheader("Line Plot")
    fig = plt.figure(figsize=(10,5))
    plt.plot(df["month_number"] , df["total_profit"], c="r", lw= 5, marker=">", markersize=15, ls= "--")
    plt.title("Total Profit over months")
    st.pyplot(fig)


    st.subheader("Scatter Plot")
    fig = plt.figure(figsize=(10,5))
    plt.scatter(df["month_number"] , df["total_profit"])
    plt.title("Total Profit over months")
    st.pyplot(fig)
    
    st.subheader("Bar Plot")
    fig = plt.figure(figsize=(10,5))
    plt.bar(df["month_number"] , df["total_profit"])
    plt.title("Total Profit over months")
    st.pyplot(fig)
    
    
    st.header("Seaborn")
    df2 = sns.load_dataset("tips")
    st.write(df2.head())
    
    
    st.subheader("Hist plot")
    fig = plt.figure(figsize=(15,5))
    sns.histplot(df2["total_bill"], kde=True)
    st.pyplot(fig)
    
    st.subheader("Scatter Plot")
    fig = plt.figure(figsize=(15,5))
    hue_option = st.selectbox("Pick a Hue", options=["sex", "smoker"])
    sns.scatterplot(data=df2 , x="total_bill", y="tip", hue=hue_option)
    st.pyplot(fig)
    
    
    st.subheader("Box Plot")
    fig = plt.figure(figsize=(15,5))
    box_option = st.radio("Select an option:" ,options=["total_bill", "tip"])
    sns.boxplot(df2[box_option])
    st.pyplot(fig)
    
    
    st.subheader("heatmap Plot")
    fig = plt.figure(figsize=(15,5))
    numerical_df = df.select_dtypes(include= np.number)
    sns.heatmap(numerical_df.corr(), annot=True)
    st.pyplot(fig)
    
    
    
    st.header("Plotly")
    order_df = pd.read_excel("P1-SuperStoreUS-2015.xlsx", sheet_name="Orders")
    st.write(order_df.head())
    
    st.subheader("Line Chart")
    sales_over_time = order_df.groupby("Order Date")["Sales"].sum().reset_index()
    fig = px.line(sales_over_time, x="Order Date", y="Sales", title="Sales Over Time")
    st.plotly_chart(fig)
    
    st.subheader("Bar Chart")
    sales_region = order_df.groupby("Region")["Sales"].sum().reset_index()
    fig = px.bar(sales_region, x="Region", y= "Sales")
    st.plotly_chart(fig)
    
    
    st.subheader("Bar Chart")
    customer_sales = order_df.groupby("Customer Name")["Sales"].sum().reset_index().nlargest(10,"Sales")
    fig = px.bar(customer_sales, x="Customer Name", y="Sales")
    st.plotly_chart(fig)
    st.text("Top 10 Customer")
