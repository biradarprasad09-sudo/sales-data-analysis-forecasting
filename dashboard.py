import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.linear_model import LinearRegression
import numpy as np
import sqlite3

st.set_page_config(
    page_title="Sales Analysis Dashboard",
    layout="wide"
)

st.title("📊 Sales Analysis Dashboard")

uploaded = st.file_uploader(
    "Upload CSV File",
    type="csv"
)

if uploaded is not None:

    data = pd.read_csv(uploaded)

    total_sales = data["Sales"].sum()
    average_sales = data["Sales"].mean()
    total_quantity = data["Quantity"].sum()

    top_product = data.groupby(
        "Product"
    )["Sales"].sum().idxmax()

    data["Date"] = pd.to_datetime(
        data["Date"]
    )

    monthly_sales = data.groupby(
        data["Date"].dt.month
    )["Sales"].sum()

    if len(monthly_sales) >= 2:

        previous_month = monthly_sales.iloc[-2]

        current_month = monthly_sales.iloc[-1]

        growth_rate = (
            (current_month - previous_month)
            / previous_month
        ) * 100

    else:

        growth_rate = 0

    st.subheader("📈 Business Summary")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "Total Sales",
            f"₹{total_sales:,.0f}"
        )

        st.metric(
            "Total Quantity Sold",
            total_quantity
        )

    with col2:

        st.metric(
            "Average Sales",
            f"₹{average_sales:,.0f}"
        )

        st.metric(
            "Top Product",
            top_product
        )

    with col3:

        st.metric(
            "Growth Rate",
            f"{growth_rate:.2f}%"
        )

    st.markdown("---")

    selected_product = st.selectbox(
        "Select Product",
        data["Product"].unique()
    )

    filtered_data = data[
        data["Product"] == selected_product
    ]

    st.subheader(
        "📋 Filtered Product Data"
    )

    st.write(filtered_data)

    st.markdown("---")

    st.subheader(
        "📂 Complete Dataset"
    )

    st.write(data)

    st.markdown("---")

    st.subheader(
        "📊 Product Sales"
    )

    product_sales = data.groupby(
        "Product"
    )["Sales"].sum()

    fig = px.bar(
        x=product_sales.index,
        y=product_sales.values,
        title="Product Sales",
        labels={
            "x": "Product",
            "y": "Sales"
        }
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.subheader(
        "🥧 Sales Distribution"
    )

    fig2 = px.pie(
        names=product_sales.index,
        values=product_sales.values,
        title="Sales Distribution"
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

    st.markdown("---")

    st.subheader(
        "📑 Dataset Summary"
    )

    st.write(
        data.describe()
    )

    st.markdown("---")

    try:

        forecast = pd.read_csv(
            "reports/forecast.csv"
        )

        st.subheader(
            "📈 Overall 30 Day Forecast"
        )

        st.line_chart(
            forecast["Predicted_Sales"]
        )

        st.markdown("---")

        st.subheader(
            "📈 Product Wise Forecasting"
        )

        forecast_product = st.selectbox(
            "Select Product For Forecast",
            data["Product"].unique()
        )

        product_data = data[
            data["Product"] ==
            forecast_product
        ]

        if len(product_data) > 1:

            x = np.arange(
                len(product_data)
            ).reshape(-1, 1)

            y = product_data["Sales"]

            model = LinearRegression()

            model.fit(
                x,
                y
            )

            future_sales = []

            for i in range(1, 31):

                value = model.predict(
                    [[len(product_data) + i]]
                )

                future_sales.append(
                    round(
                        float(value[0]),
                        2
                    )
                )

            forecast_df = pd.DataFrame({

                "Day": range(1, 31),

                "Predicted Sales": future_sales
            })

            st.line_chart(
                forecast_df.set_index(
                    "Day"
                )
            )

            st.write(
                forecast_df
            )

        st.markdown("---")

        st.subheader(
            "⬇️ Download Reports"
        )

        with open(
            "reports/Sales_Report.pdf",
            "rb"
        ) as pdf_file:

            st.download_button(
                label="📄 Download PDF Report",
                data=pdf_file,
                file_name="Sales_Report.pdf",
                mime="application/pdf"
            )

        with open(
            "reports/sales_analysis.xlsx",
            "rb"
        ) as excel_file:

            st.download_button(
                label="📊 Download Excel Report",
                data=excel_file,
                file_name="sales_analysis.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )

    except Exception as e:

        st.warning(
            f"Report files missing: {e}"
        )

else:

    st.info(
        "Upload sales_data.csv to start analysis."
    )