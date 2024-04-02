# msib6-d15-git
Repository tugas Python 5: OOP pada respository tersebut

## Dokumentasi

Paket ini memiliki 2 (dua) class yaitu `MarketingDataETL` dan `TargetedMarketingETL` yang masing-masing memiliki 3 method ETL yaitu `extract`, `transform`, dan `store`.

Selain memiliki method-method tersebut, masing-masing class bisa mengakses dataframe dengan menggungkan property `df`.

### Cara Penggunaan

import paket ke script Anda

```python
from .etl import MarketingDataETL

etl_job = MarketingDataETL()
```

Gunakan method extract untuk mengimpor data dari file csv.

```python
...

# extract data
etl_job.extract('drive/MyDrive/Colab Notebooks/marketing_data.csv')

# tampilkan dataframe
etl_job.df
```

Gunakan method transform untuk melakukan pembersihan dan transformasi sederhana

```python
...

# extract dan transform data
etl_job.extract('drive/MyDrive/Colab Notebooks/marketing_data.csv')
etl_job.transform()

...
```

Gunakan method `store` untuk menyimpan data ke format pickle pandas dataframe.

```python
...

# extract, transform, dan store data
etl_job.extract('drive/MyDrive/Colab Notebooks/marketing_data.csv')
etl_job.transform()
etl_store.store('extracted.pkl')

...
```

Anda juga bisa menggabungkan proses tersebut dengan chain method seperti berikut:

```python
...

# extract, transform, store, dan view data menggunakan
# chaini method
etl_job\
    .extract('drive/MyDrive/Colab Notebooks/marketing_data.csv')\
    .transform()\
    .store('extracted.pkl')\
    .df

```