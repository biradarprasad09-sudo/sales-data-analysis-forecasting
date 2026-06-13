from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Image,
    PageBreak
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)

class PDFGenerator:

    def generate_pdf(
        self,
        report
    ):

        pdf = SimpleDocTemplate(
            "reports/Sales_Report.pdf"
        )

        styles = getSampleStyleSheet()

        content = []

        content.append(

            Paragraph(
                "Sales Data Analysis & Forecasting",
                styles["Title"]
            )
        )

        content.append(
            Spacer(1, 20)
        )

        content.append(

            Paragraph(
                "Professional Business Report",
                styles["Heading2"]
            )
        )

        content.append(
            Spacer(1, 30)
        )

        content.append(
            PageBreak()
        )

        content.append(

            Paragraph(
                "Sales Analysis Summary",
                styles["Heading1"]
            )
        )

        content.append(
            Spacer(1, 12)
        )

        content.append(

            Paragraph(
                report.replace(
                    "\n",
                    "<br/>"
                ),
                styles["BodyText"]
            )
        )

        content.append(
            Spacer(1, 20)
        )

        try:

            content.append(

                Paragraph(
                    "Product Sales Chart",
                    styles["Heading2"]
                )
            )

            content.append(
                Spacer(1, 10)
            )

            content.append(

                Image(
                    "charts/product_sales.png",
                    width=400,
                    height=250
                )
            )

            content.append(
                Spacer(1, 20)
            )

        except:
            pass

        try:

            content.append(

                Paragraph(
                    "Monthly Sales Trend",
                    styles["Heading2"]
                )
            )

            content.append(
                Spacer(1, 10)
            )

            content.append(

                Image(
                    "charts/monthly_trend.png",
                    width=400,
                    height=250
                )
            )

            content.append(
                Spacer(1, 20)
            )

        except:
            pass

        pdf.build(
            content
        )