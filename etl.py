import pandas as pd


class MarketingDataETL():
    
    def __init__(self):
        self.df = None

    def extract(self, file_name, **kwargs):
        """
        Method ini menerima parameter file_name beserta opsi-opsi lain yang akan
        dilemparkan ke fungsi read_csv

        parameters:
        - file_name : str : nama file yang akan dibaca
        - **kwargs : any : opsi yang akan dilempar ke method read_csv pandas
        """
        self.df = pd.read_csv(file_name, **kwargs)

        return self

    def transform(self):
        """
        melakukan transformasi sederhana seperti
        - parse tanggal pembayaran
        - trim data teks (customer id, product_category)
        """

        # remove na
        self.df = self.df.dropna()

        # parsing data tanggal
        self.df['purchase_date'] = pd.to_datetime(self.df.purchase_date)

        return self

    def store(self, path):
        """
        ekspor hasil pengolahan dalam bentuk pickle ke lokasi
        yang diberikan

        parameters:
        - path : str : lokasi ekspor file
        """

        self.df.to_pickle(path)

        return self