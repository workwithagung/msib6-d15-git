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