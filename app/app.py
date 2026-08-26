import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import os

st.set_page_config(page_title="ShopSmart Checkout A/B Test", layout="wide")

st.title("ShopSmart Checkout A/B Test Dashboard")
st.write("Analyzing whether a one-page checkout improves conversion, revenue, and retention.")

BASE_DIR = os.path.dirname(os.path.abspath(_file_))
df = pd.read_csv(os.path.join(BASE_DIR, "..", "data", "shopsmart_experiment.csv"))

 
control= df[df["variant"] == "control"]
treatment = df[df["variant"] == "treatment"]

col1, col2, col3 = st.columns(3)
col1.metric("Control Conversion", f"{control['completed_purchase'].mean()*100:.2f}%")
col2.metric("Treatment Conversion", f"{treatment['completed_purchase'].mean()*100:.2f}%",
            delta=f"{(treatment['completed_purchase'].mean() - control['completed_purchase'].mean())*100:.2f}%")
col3.metric("Revenue Lift", f"₹{treatment['revenue'].mean() - control['revenue'].mean():.2f}/user")

st.subheader("Retention Curve")
retention=df.groupby("variant")[["month_1_active", "month_2_active", "month_3_active"]].mean()*100
retention.columns=["Month 1", "Month 2", "Month 3"]

fig= go.Figure()
for variant in retention.index: 
    fig.add_trace(go.Scatter(x=["Month 1", "Month 2", "Month 3"], y=retention.loc[variant],
                mode="lines+markers", name=variant))
fig.update_layout(yaxis_title="% Users Active", xaxis_title="Month")
st.plotly_chart(fig,use_container_width=True)

st.subheader("Purchase Funnel")
funnel = df.groupby("variant")[["visited_site","added_to_cart","started_checkout","completed_purchase"]].mean()*100

fig2 = go.Figure()
for variant in funnel.index:
    fig2.add_trace(go.Bar(x=["Visited","Added to Cart","Started Checkout","Purchased"],
                           y=funnel.loc[variant], name=variant))
fig2.update_layout(barmode="group", yaxis_title="% of Users")
st.plotly_chart(fig2, use_container_width=True)