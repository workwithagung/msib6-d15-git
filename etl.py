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

class TargetedMarketingETL(MarketingDataETL):

    def segment_customers(self, category=None, min_total=0):
        """
        Berfungsi untuk memfilter data berdasarkan category tertentu. Setelah
        data difilter, selanjutnya akan diaggregat berdasarkan customer sehingga
        menghasilkan nilai total belanja (amount_spent).

        parameters:
        - category: string : category product yang akan dipilih
        - min_total: strig
        """

        # filter berdasarkan kategori, jika ada
        if category is not None:
            self.df = self.df[self.df.product_category == category]

        # aggregate amount_spent berdasarkan customer_id
        self.df = self.df[['customer_id', 'amount_spent']].groupby('customer_id', as_index=False).sum()

        # filter berdasarkan minimal nilai itotal berdasarkan argument
        self.df = self.df[self.df.amount_spent > min_total].copy()

        return self

    def transform(self, category=None, min_total=0):
        """
        overide method parent untuk menambahkan proses segementasi customer
        """

        super().transform()
        self.segment_customers(category, min_total)

        return self
