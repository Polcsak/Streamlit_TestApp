import streamlit as st
import pandas as pd
import numpy as np

# Static Viz
import matplotlib.pyplot as plt
import seaborn as sns


st.title("Static Visualizations in Streamlit")

df = pd.read_csv("tips.csv")
st.dataframe(df.head())

## Questions
# 1. Find number of Male and Female distribution (pie and bar charts)

st.markdown("---")
with st.container():
    st.write("1. Find number of Male and Female distribution (pie and bar charts)")
    
    value_counts = df["sex"].value_counts()
    
    # Set layout for viz

    col1,col2 = st.columns(2)

    # Draw Pie chart
    with col1:
        st.subheader("Pie Chart")
        fig,ax = plt.subplots()
        ax.pie(value_counts, 
            autopct="%0.3f%%", 
            labels=["Male", "Female"])
        st.pyplot(fig)

    # Draw bar plot
    with col2:
        st.subheader("Bar Chart")
        fig,ax = plt.subplots()
        ax.bar(value_counts.index,value_counts)
        st.pyplot(fig)
    
    # Put this in expander
    with st.expander("Click here to display value counts"):
        st.dataframe(value_counts)

# Streamlit widgets and charts
data_types = df.dtypes
cat_cols = data_types[data_types == "object"].index


st.markdown("---")
with st.container():
    feature = st.selectbox("Select the feature you want to display",
                           cat_cols
                           )
    
    value_counts = df[feature].value_counts()
    
    # Set layout for viz

    col1,col2 = st.columns(2)

    # Draw Pie chart
    with col1:
        st.subheader("Pie Chart")
        fig,ax = plt.subplots()
        ax.pie(value_counts, 
            autopct="%0.3f%%", 
            labels=value_counts.index)
        st.pyplot(fig)

    # Draw bar plot
    with col2:
        st.subheader("Bar Chart")
        fig,ax = plt.subplots()
        ax.bar(value_counts.index,value_counts)
        st.pyplot(fig)
    
    # Put this in expander
    with st.expander("Click here to display value counts"):
        st.dataframe(value_counts)


# 2. Find distribution of Male and Female spent (boxplot or kdeplot)

st.markdown("---")
with st.container():
    st.write("2. Find distribution of Male and Female spent (boxplot or kdeplot)")
    # box, violin, kdeplot, histogram
    chart = ("box", "violin", "kdeplot", "histogram")
    chart_selection = st.selectbox("Select the chart type", chart)
    fig, ax = plt.subplots()
    
    if chart_selection == "box":
        sns.boxplot(x="sex", y="total_bill", data=df, ax=ax)
    elif chart_selection == "violin":
        sns.violinplot(x="sex", y="total_bill", data=df, ax=ax)
    elif chart_selection == "kdeplot":
        sns.kdeplot(x=df["total_bill"], hue=df["sex"], ax=ax, shade=True)
    else:
        sns.histplot(x="total_bill", hue="sex", data=df, ax=ax)


    st.pyplot(fig)

st.markdown("---")
st.write("3. Find distribution of average total_bill across each day by male and female")

features_to_groupby = ["day","sex"]
feature = ["total_bill"]
selected_cols = feature + features_to_groupby

avg_total_bill = df[selected_cols].groupby(features_to_groupby).mean()
# avg_total_bill_V2 = df.groupby(features_to_groupby)[feature].mean()

# st.dataframe(avg_total_bill_V2)
# st.dataframe(avg_total_bill)



