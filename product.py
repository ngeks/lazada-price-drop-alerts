import pandas


class Product:
    def __init__(self, data_as_csv):
        self.data_as_csv = data_as_csv
        self.init_data()

    def init_data(self):
        """Initialize file data."""
        try:
            pandas.read_csv(self.data_as_csv)
        except FileNotFoundError:
            data = pandas.DataFrame({
                'name': [],
                'price': [],
                'url': []
            })
            data.to_csv(self.data_as_csv, index=False)

    def data(self):
        """Return data as pandas data frame."""
        data = pandas.read_csv(self.data_as_csv)
        return pandas.DataFrame(data)

    def view(self):
        """Display current data."""
        data = self.data()
        print(f"\n{data}\n")

    def add(self, name, price, url):
        """Add new product data."""
        data = self.data()
        data.loc[len(data.index)] = [name, price, url]
        data.to_csv(self.data_as_csv, index=False)

    def remove(self, data_idx):
        """Remove product data."""
        data = self.data()
        data = data.drop(index=data_idx)
        data.to_csv(self.data_as_csv, index=False)
        