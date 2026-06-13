import pandas as pd

class SalesAnalyzer:

    def total_sales(self, data):
        return data["Sales"].sum()

    def average_sales(self, data):
        return data["Sales"].mean()

    def top_product(self, data):
        return data.groupby("Product")["Sales"].sum().idxmax()

    def worst_product(self, data):
        return data.groupby("Product")["Sales"].sum().idxmin()

    def total_quantity(self, data):
        return data["Quantity"].sum()

    def monthly_sales(self, data):
        temp = data.copy()
        temp["Date"] = pd.to_datetime(temp["Date"])

        return temp.groupby(
            temp["Date"].dt.month
        )["Sales"].sum()

    def growth_rate(self, data):

        monthly = self.monthly_sales(data)

        if len(monthly) < 2:
            return 0

        previous = monthly.iloc[-2]
        current = monthly.iloc[-1]

        return round(
            ((current - previous) / previous) * 100,
            2
        )