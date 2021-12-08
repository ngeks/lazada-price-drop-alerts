import pandas


class Product:
    def __init__(self, data_as_csv):
        self.data_as_csv = data_as_csv
        self.init_data()

    def init_data(self):
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
        data = pandas.read_csv(self.data_as_csv)
        return pandas.DataFrame(data)

    def view(self):
        data = self.data()
        print(f"\n{data}\n")

    def add(self, name, price, url):
        data = self.data()
        data.loc[len(data.index)] = [name, price, url]
        data.to_csv(self.data_as_csv, index=False)

    def remove(self, data_idx):
        data = self.data()
        data = data.drop(index=data_idx)
        data.to_csv(self.data_as_csv, index=False)