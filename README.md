# Dashboard Analisis Data Penyewaan Sepeda 🚴‍♂️

Proyek ini bertujuan untuk menganalisis data penyewaan sepeda menggunakan dataset publik. Dashboard ini memungkinkan pengguna untuk melihat analisis jam puncak penyewaan sepeda, perbandingan antara hari kerja dan hari libur, serta pola musiman penggunaan sepeda.

## Fitur

- Visualisasi jam puncak penyewaan sepeda setiap hari dalam satu minggu
- Persentase rata-rata penyewaan antara hari libur dan hari kerja pada tahun 2012
- Pola musiman penggunaan sepeda selama tahun 2012

## Setup Environment - Anaconda
```bash
    conda create --name main-ds python=3.9
    conda activate main-ds
    pip install -r requirements.txt
```
## Setup Environment - Shell/Terminal
```bash
    mkdir proyek_analisis_data
    cd proyek_analisis_data
    pipenv install
    pipenv shell
    pip install -r requirements.txt
```
## Run Steamlit App
```bash
    streamlit run dashboard.py
```
