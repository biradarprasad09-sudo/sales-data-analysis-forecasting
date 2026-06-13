class SalesRecord:
    def __init__(self, date, product, quantity, sales):
        self.date = date
        self.product = product
        self.quantity = quantity
        self.sales = sales

    def display(self):
        print(self.date, self.product, self.quantity, self.sales)