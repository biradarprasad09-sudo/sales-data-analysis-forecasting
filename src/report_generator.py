class ReportGenerator:

    def generate_report(
        self,
        total_sales,
        average_sales,
        top_product,
        worst_product,
        total_quantity,
        growth_rate,
        prediction
    ):

        forecast_average = round(
            sum(prediction) / len(prediction),
            2
        )

        report = f"""
==================================================
           SALES ANALYSIS REPORT
==================================================

1. SALES PERFORMANCE

Total Sales:
{total_sales:.2f}

Average Sales:
{average_sales:.2f}

Total Quantity Sold:
{total_quantity}

--------------------------------------------------

2. PRODUCT PERFORMANCE

Top Performing Product:
{top_product}

Lowest Performing Product:
{worst_product}

--------------------------------------------------

3. BUSINESS GROWTH

Growth Rate:
{growth_rate:.2f} %

--------------------------------------------------

4. FORECASTING RESULTS

30-Day Forecast:

{prediction}

Average Forecasted Sales:

{forecast_average}

--------------------------------------------------

5. BUSINESS INSIGHTS

• {top_product} is currently the strongest product.

• {worst_product} requires attention to improve sales.

• Current growth rate is {growth_rate:.2f}% .

• Forecast indicates future sales trends based on historical data.

--------------------------------------------------

6. RECOMMENDATIONS

• Increase inventory for top-performing products.

• Review pricing and promotion strategies for low-performing products.

• Monitor monthly growth trends regularly.

• Use forecast results for future business planning.

==================================================
END OF REPORT
==================================================
"""

        return report

    def save_report(
        self,
        report
    ):

        with open(
            "reports/report.txt",
            "w",
            encoding="utf-8"
        ) as file:

            file.write(
                report
            )