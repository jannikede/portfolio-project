import streamlit as st
import pandas as pd
from plotly import graph_objects as go
import seaborn as sns
from matplotlib import pyplot as plt
import numpy as np


###Load Data
from pathlib import Path

data_path = Path(__file__).parent / 'data' / 'prepped_data.csv'
session_data = pd.read_csv(data_path)


st.set_page_config(layout="wide")


st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@100..900&display=swap');

/* Basis-Font für die gesamte App */
.main, .stApp {
    font-family: 'Montserrat', sans-serif !important;
}

/* Überschriften */
h1, h2, h3, h4, h5, h6 {
    font-family: 'Montserrat', sans-serif !important;
}

/* Markdown und Text */
[data-testid="stMarkdownContainer"] {
    font-family: 'Montserrat', sans-serif !important;
}
</style>
""", unsafe_allow_html=True)


st.title("Funnel Analytics Dashboard")



###Sidebar config
with st.sidebar:
    st.title("Filter")
    st.text("Adjust the KPIs and Graphs by filtering the data.")

    #Date Filter
    session_data["date"] = pd.to_datetime(session_data["date"])

    min_date = session_data["date"].min().date()
    max_date = session_data["date"].max().date()

    date_range = st.date_input("Analysis Period", (min_date, max_date), min_value=min_date, max_value=max_date)


    #Country Filter
    all_countries = sorted(session_data["geo_country"].unique())

    selected_countries = st.multiselect("Select Countries", all_countries, default=all_countries)


    ##Apply the Filters

    #(secure date range)
    if len(date_range) == 2:
        start_date, end_date = date_range
    else:
        start_date, end_date = min_date, max_date

    session_filtered = session_data[
        (session_data["date"].dt.date >= start_date) & (session_data["date"].dt.date <= end_date)
        &
        (session_data["geo_country"].isin(selected_countries))
    ].copy()

    st.markdown("---")
    with st.expander("Data Source", expanded=False):
            st.markdown("This synthetic Dataset was taken from [Hugging Face](https://huggingface.co/datasets/liniribeiro/synthetic-user-sessions/tree/main).")







#### KPIs

###Prep Customer Dataframe
session_filtered['timestamp'] = pd.to_datetime(session_filtered['timestamp'])
session_filtered['month'] = session_filtered['timestamp'].dt.to_period("M")

customer_data = session_filtered.drop(columns = ["page_name", "product_id", "device_type", "browser", "os", "geo_city", "traffic_source", "campaign", "referrer_url", "date", "time", "timestamp"])


#calculate needed metrics/variables
customer_data["order_count"] = np.where(customer_data["revenue"] > 0, 1, 0)

customer_data_grouped = customer_data.groupby(['user_id', 'month']).agg({
    'order_count': 'sum',
    'revenue': 'sum',
    'session_id': 'nunique'
}).reset_index()

customer_data_grouped.rename(columns={"session_id":"session_count"}, inplace=True)



###### Visitors that did not buy off the website

#prep Dataframe
unsuccessful_visits = customer_data_grouped.drop(columns="month").groupby("user_id").agg({"order_count": "sum", "revenue": "sum", "session_count": "sum"})
unsuccessful_visits["no_buy"] = np.where(unsuccessful_visits["revenue"] < 1, 1, 0)


unsuccessful_visits_percentage =  (unsuccessful_visits["no_buy"] == 1).sum() / len(unsuccessful_visits)




### Paying Customer Churn Rate
paying_customers = customer_data_grouped[customer_data_grouped['order_count'] > 0]
last_activity_p = paying_customers.groupby('user_id')['month'].max()

latest_month_p = paying_customers['month'].max()
churned_users_p = (last_activity_p < latest_month_p).sum()
total_users_p = len(last_activity_p)

overall_churn_rate_p = churned_users_p / total_users_p




###### Customer Lifetime Value based on paying customers

purchases_mask_2 = session_filtered["event_type"] == "purchase"
purchases_2 = session_filtered[purchases_mask_2]

#Average Purchase Value APV
APV = purchases_2["revenue"].sum() / len(purchases_2) #purchases["revenue"].mean()

#Average Purchase Frequency APF:
APF = ( len(purchases_2) / purchases_2["user_id"].nunique() )

#Average Customer Lifespan ACL
ACL = (1/ overall_churn_rate_p )

CLV = (APV * APF) * ACL

#### KPI Card Style
st.markdown("""
<style>

.metric.card {
    background-color: white;
    border: 2px solid #153b5c;
    border-radius: 10px;
    padding: 20px;
    width: 100%;              
    height: 170px;        
    text-align: center;
    display: flex;
    flex-direction: column;
    justify-content: center;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.metric.card h3 {
    font-size: 16px;
    color: #153b5c;
    margin: 0 0 10px 0;
    font-weight: 600;
    line-height: 1.2;        
}

.metric.card h2 {
    font-size: 32px;
    color: #153b5c;
    margin: 0;
    font-weight: 700;
    line-height: 1.2;         
}

</style>
""", unsafe_allow_html=True)


#KPI classification rules

def kpi_threshold(kpi, thresholds, directionality):
    """
    Classify KPI metrics into categories and assign corresponding colors.

    Args:
        kpi (float|int): Value of the KPI to classify
        thresholds (list): Threshold values [good, medium, bad]
        directionality (str): "upward" (higher is better) or "downward" (lower is better)

    Returns:
        tuple: (classification: str, color: str)

    Examples:
        >>> kpi_threshold(85, [80, 60, 40], "upward")
        ('good', '#5DDE60')
        >>> kpi_threshold(15, [20, 40, 60], "downward")
        ('good', '#5DDE60')
    """

    colors = {
        "good": "#5DDE60",
        "medium": "#EBDE71",
        "bad": "#C93E3E"
    }

    good, medium, bad = thresholds

    if directionality == "upward":
        if kpi >= good:
            classification = "good"
        elif kpi >= medium:
            classification = "medium"
        else:
            classification = "bad"

    elif directionality == "downward":
        if kpi <= good:
            classification = "good"
        elif kpi <= medium:
            classification = "medium"
        else:
            classification = "bad"

    else:
        raise ValueError(f"Invalid directionality: '{directionality}'. Must be 'upward' or 'downward'.")

    return classification, colors[classification]


#Use function to set color to be used when displayed in KPI cards:

visits_color = kpi_threshold(unsuccessful_visits_percentage*100, thresholds = [20, 30, 50], directionality="downward")[1]
lifespan_color = kpi_threshold(ACL, thresholds = [12, 6, 3], directionality="upward")[1]
churn_color = kpi_threshold(overall_churn_rate_p*100, thresholds = [5, 30, 100], directionality="downward")[1]


#Create metric cards

c1, c2 = st.columns(2)

with c1:
    st.markdown(f"""
    <div class="metric card">
        <h3>Total Revenue</h3>
        <h2>{(session_filtered["revenue"].sum()):.2f}$</h2>
    </div>    
    """, unsafe_allow_html=True)

with c2:
    st.markdown(f"""
    <div class="metric card">
        <h3>Unsuccessful Visits</h3>
        <h2 style="color: {visits_color};">
            {unsuccessful_visits_percentage:.2%}
        </h2>            
    </div>    
    """, unsafe_allow_html=True)


st.markdown(f"        ")


c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown(f"""
    <div class="metric card">
            <h3>Average Customer Lifetime Value </h3>
            <h2>{CLV:.2f}$</h2>
    </div>    
    """, unsafe_allow_html=True)


with c2:
    st.markdown(f"""
    <div class="metric card">
            <h3>Average Purchase Value </h3>
            <h2>{APV:.2f}$</h2>
    </div>    
    """, unsafe_allow_html=True)

with c3:
    st.markdown(f"""
    <div class="metric card">
        <h3>Average Customer Lifespan</h3>
        <h2 style="color: {lifespan_color};">
                {ACL:.2f} Months
        </h2>                
    </div>    
    """, unsafe_allow_html=True)


with c4:
    st.markdown(f"""
    <div class="metric card">
        <h3>Churn Rate </h3>
        <h2 style="color: {churn_color};">
                {overall_churn_rate_p:.2%}
        </h2>                
    </div>    
    """, unsafe_allow_html=True)


st.markdown("---")

###Visualizations:

c1, c2 = st.columns(2)

## Revenue over the Day

hourly_purchases = purchases_2.sort_values(by = ["timestamp"]).set_index("timestamp")
hourly_purchases["time"] = pd.to_datetime(hourly_purchases["time"])
hourly_purchases["hour"] = hourly_purchases["time"].apply(lambda x: x.hour)
hourly_purchases["rolling_mean_hourly"] = hourly_purchases["revenue"].rolling(window='1h', center=True).mean()
hourly_avg = hourly_purchases.groupby("hour")["rolling_mean_hourly"].mean().reset_index()

#Interactive Plot Revenue over the Day:
with c1:

    import plotly.express as px
    fig = px.line(hourly_avg, x="hour", y="rolling_mean_hourly",
                  labels={"hour": "Time of Day", "rolling_mean_hourly": "Revenue"},
                  title="Hourly Revenue")

    # Layout
    fig.add_hline(y=hourly_purchases["revenue"].mean(), line_dash="dash", line_color="grey",
                  annotation_text="Average", annotation_position="right")
    fig.update_xaxes(tickmode='linear', tick0=0, dtick=1, range=[0, 23])
    fig.update_layout(
        xaxis=dict(
            showline=True,
            showgrid=False,
            showticklabels=True,
            linecolor='rgb(204, 204, 204)',
            # linewidth=2,
            ticks='outside',

        ),
        #plot_bgcolor='white',
        yaxis=dict(
            showgrid=False,
            zeroline=True,
            showline=True,
            showticklabels=True,
            linecolor='rgb(204, 204, 204)',
            ticksuffix="$"
        ))

    st.plotly_chart(fig)


### FUNNEL GRAPHIC

from plotly import graph_objects as go

#extract Funnel Steps
views_homepage_mask = (session_filtered["event_type"] == "view") & (session_filtered["page_name"].str.contains("home"))
views_homepage = session_filtered[views_homepage_mask]

checkout_clicks_mask = (session_filtered["event_type"] == "click") & (session_filtered["page_name"].str.contains("checkout"))
checkout_clicks = session_filtered[checkout_clicks_mask]

product_clicks_mask = (session_filtered["event_type"] == "click") & (session_filtered["page_name"].str.contains("product"))
product_clicks = session_filtered[product_clicks_mask]

add_to_cart_mask_2 = session_filtered["event_type"] == "add_to_cart"
add_to_cart_2 = session_filtered[add_to_cart_mask_2]

product_views_mask_2 = (session_filtered["event_type"] == "view") & (session_filtered["product_id"].notna())
product_views_2 = session_filtered[product_views_mask_2]


#Interactive Plot Funnel:
with c2:
    fig = go.Figure(go.Funnel(
            y = ["Views – Homepage", "Views – Product", "Click – Product", "Added to Cart", "Click – Checkout", "Purchased"],
            x = [len(views_homepage), len(product_views_2), len(product_clicks), len(add_to_cart_2), len(checkout_clicks), len(purchases_2)]
    ))
    fig.update_layout(title="Conversion Funnel")

    st.plotly_chart(fig)

st.subheader("Data")
st.markdown(f"By clicking on the three dots appearing when hovering over a column, the data can be sorted.")
st.write(session_filtered)
