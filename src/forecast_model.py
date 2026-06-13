from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd

class ForecastModel:

    def predict_sales(
        self,
        data
    ):

        x = np.arange(
            len(data)
        ).reshape(-1, 1)

        y = data["Sales"]

        model = LinearRegression()

        model.fit(
            x,
            y
        )

        predictions = []

        for i in range(1, 31):

            future = np.array(
                [[len(data) + i]]
            )

            value = model.predict(
                future
            )

            predictions.append(
                round(
                    float(value[0]),
                    2
                )
            )

        forecast_df = pd.DataFrame({

            "Day": range(1, 31),

            "Predicted_Sales": predictions
        })

        forecast_df.to_csv(
            "reports/forecast.csv",
            index=False
        )

        return predictions

    def product_forecast(
        self,
        data
    ):

        results = {}

        all_products = []

        products = data[
            "Product"
        ].unique()

        for product in products:

            product_data = data[
                data["Product"] == product
            ]

            if len(product_data) < 2:
                continue

            x = np.arange(
                len(product_data)
            ).reshape(-1, 1)

            y = product_data[
                "Sales"
            ]

            model = LinearRegression()

            model.fit(
                x,
                y
            )

            forecast = []

            for i in range(1, 31):

                value = model.predict(
                    [[len(product_data) + i]]
                )

                forecast.append(
                    round(
                        float(value[0]),
                        2
                    )
                )

                all_products.append({

                    "Product": product,

                    "Day": i,

                    "Predicted_Sales":
                    round(
                        float(value[0]),
                        2
                    )
                })

            results[
                product
            ] = forecast

        product_forecast_df = pd.DataFrame(
            all_products
        )

        product_forecast_df.to_csv(

            "reports/product_forecast.csv",

            index=False
        )

        return results