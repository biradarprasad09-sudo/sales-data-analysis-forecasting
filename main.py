from src.data_processor import DataProcessor
from src.sales_analyzer import SalesAnalyzer
from src.forecast_model import ForecastModel
from src.report_generator import ReportGenerator
from src.pdf_generator import PDFGenerator
from src.database_manager import DatabaseManager

import matplotlib.pyplot as plt
import logging

logging.basicConfig(
    filename="reports/log.txt",
    level=logging.INFO
)

logging.info("Program Started")

processor = DataProcessor()

try:
    data = processor.load_data(
        "data/sales_data.csv"
    )

    data = processor.clean_data(
        data
    )

except Exception as e:

    print(
        "Dataset Error:",
        e
    )

    raise SystemExit

database = DatabaseManager()

database.create_database()
database.insert_data(
    data
)

print(
    "Records Stored:",
    database.record_count()
)

analyzer = SalesAnalyzer()

total_sales = analyzer.total_sales(
    data
)

average_sales = analyzer.average_sales(
    data
)

top_product = analyzer.top_product(
    data
)

worst_product = analyzer.worst_product(
    data
)

total_quantity = analyzer.total_quantity(
    data
)

growth_rate = analyzer.growth_rate(
    data
)

monthly_sales = analyzer.monthly_sales(
    data
)

forecast = ForecastModel()

prediction = forecast.predict_sales(
    data
)

product_predictions = forecast.product_forecast(
    data
)

report = ReportGenerator()

result = report.generate_report(
    total_sales,
    average_sales,
    top_product,
    worst_product,
    total_quantity,
    growth_rate,
    prediction
)

print(result)

print("\nPRODUCT FORECASTS")

for product, values in product_predictions.items():

    print(f"\n{product}")

    print(values)

report.save_report(
    result
)

pdf = PDFGenerator()

pdf.generate_pdf(
    result
)

product_sales = data.groupby(
    "Product"
)["Sales"].sum()

product_sales.plot(
    kind="bar"
)

plt.title(
    "Product Sales"
)

plt.savefig(
    "charts/product_sales.png"
)

plt.close()

product_sales.plot(
    kind="pie",
    autopct="%1.1f%%"
)

plt.ylabel("")

plt.savefig(
    "charts/product_pie.png"
)

plt.close()

monthly_sales.plot(
    kind="line"
)

plt.title(
    "Monthly Sales Trend"
)

plt.savefig(
    "charts/monthly_trend.png"
)

plt.close()

data.to_excel(
    "reports/sales_analysis.xlsx",
    index=False
)

logging.info(
    "Program Completed"
)

print(
    "Project Completed Successfully"
)