import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Membaca data
day_df=pd.read_csv("https://raw.githubusercontent.com/chalistadiviaa10/Analisis_Data_Sepeda/main/data/day.csv")
hour_df=pd.read_csv("https://raw.githubusercontent.com/chalistadiviaa10/Analisis_Data_Sepeda/main/data/hour.csv")

# Judul
st.title('Dashboard Analisis Data Penyewaan Sepeda')

# 1. Dalam kurun waktu satu minggu, pada jam berapa penyewaan sepeda mencapai puncaknya setiap hari?
hour_df['dteday'] = pd.to_datetime(hour_df['dteday'])
hour_df['day_of_week'] = hour_df['dteday'].dt.day_name()
hour_df['hour'] = hour_df['hr']
peak_hours = hour_df.groupby(['day_of_week', 'hour'])['cnt'].sum().reset_index()
peak_hours['max_cnt'] = peak_hours.groupby('day_of_week')['cnt'].transform('max') 
peak_peak_hours = peak_hours[peak_hours['cnt'] == peak_hours['max_cnt']]
# Tampilkan hasil analisis
st.subheader("Pertanyaan 1: Dalam kurun waktu satu minggu, pada jam berapa penyewaan sepeda mencapai puncaknya setiap hari?")
st.header("Jam Puncak Penyewaan Sepeda Setiap Hari")
st.write(peak_peak_hours)
# Visualisasi
plt.figure(figsize=(12, 6)) 
plt.clf()  
sns.barplot(data=peak_peak_hours, x='hour', y='cnt', hue='day_of_week', palette='viridis')  
plt.title('Jam Puncak Penyewaan Sepeda Setiap Hari')
plt.xlabel('Jam')
plt.ylabel('Jumlah Penyewaan')
plt.xticks(rotation=45)
plt.legend(title='Hari dalam Seminggu')
plt.tight_layout()
st.pyplot(plt)

# 2. Persentase rata-rata penyewaan antara hari libur dan hari kerja pada tahun 2011
day_df['dteday'] = pd.to_datetime(day_df['dteday'])
day_df['year'] = day_df['dteday'].dt.year
day_df_2011 = day_df[day_df['year'] == 2011]
avg_rentals = day_df_2011.groupby(['holiday', 'workingday'])['cnt'].mean().reset_index()
avg_rentals.columns = ['holiday', 'workingday', 'average_cnt']
total_average = avg_rentals['average_cnt'].sum()
avg_rentals['percentage'] = (avg_rentals['average_cnt'] / total_average) * 100
# Tampilkan hasil analisis
st.subheader("Pertanyaan 2: Berapa persentase perbandingan rata-rata jumlah penyewaan sepeda antara hari libur dan hari kerja pada tahun 2011?")
st.header("Persentase Rata-rata Penyewaan antara Hari Libur dan Hari Kerja (2011)")
st.write(avg_rentals)
# Visualisasi
labels = ['Hari Kerja', 'Hari Libur']
sizes = [avg_rentals[avg_rentals['holiday'] == 0]['average_cnt'].mean(),
         avg_rentals[avg_rentals['holiday'] == 1]['average_cnt'].mean()]  
colors = ['#ff9999', '#66b3ff']
explode = (0.1, 0) 
plt.figure(figsize=(8, 6))
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)
plt.axis('equal') 
plt.title('Perbandingan Rata-rata Penyewaan Sepeda antara Hari Libur dan Hari Kerja (2011)')
st.pyplot(plt)  

# 3. Pola musiman penggunaan sepeda selama tahun 2012
day_df['dteday'] = pd.to_datetime(day_df['dteday'])
day_df_2012 = day_df[day_df['dteday'].dt.year == 2012]
seasonal_rentals = day_df_2012.groupby('season')['cnt'].mean()
st.subheader("Pertanyaan 3: Apa pola musiman dalam penggunaan sepeda selama tahun 2012 dan bagaimana faktor cuaca berpengaruh terhadap tren penggunaan tersebut?")
# Visualisasi
plt.figure(figsize=(8, 5))
seasonal_rentals.plot(kind='line', marker='o', color='purple')
plt.title('Pola Musiman Penyewaan Sepeda Selama Tahun 2012')
plt.ylabel('Rata-rata Penyewaan')
plt.xticks(ticks=[1, 2, 3, 4], labels=['Musim Semi', 'Musim Panas', 'Musim Gugur', 'Musim Dingin'], rotation=0)
plt.grid() 
plt.tight_layout() 
st.pyplot(plt)   

# Kesimpulan
st.header("Kesimpulan")
st.write("""
- Analisis waktu penyewaan sepeda menunjukkan adanya pola penggunaan yang jelas, dengan puncak penyewaan terjadi pada jam-jam sibuk, terutama pada pagi dan sore hari. Ini menunjukkan bahwa sepeda banyak digunakan untuk mobilitas sehari-hari, terutama pada hari kerja. Hari Selasa, Rabu, dan Kamis menjadi hari dengan jumlah penyewaan tertinggi, terutama setelah jam 5 sore. Oleh karena itu, perusahaan dapat memanfaatkan informasi ini untuk merencanakan penempatan sepeda di lokasi-lokasi strategis pada jam-jam sibuk, serta meningkatkan ketersediaan sepeda untuk memenuhi permintaan yang tinggi. Selain itu, pengembangan program loyalitas atau promosi khusus pada hari kerja juga dapat meningkatkan minat pengguna.
- Rata-rata penyewaan sepeda per hari menunjukkan perbedaan yang signifikan antara hari kerja dan hari libur, dengan penyewaan lebih tinggi pada hari kerja (53.2%) dibandingkan hari libur (46.8%). Hal ini mengindikasikan bahwa sepeda berfungsi sebagai alat transportasi utama untuk aktivitas sehari-hari, seperti pergi ke tempat kerja, daripada sekadar untuk rekreasi. Strategi pemasaran yang dapat diterapkan termasuk menjalin kemitraan dengan perusahaan lokal untuk menyediakan program penyewaan sepeda bagi karyawan.
- Pengelompokan berdasarkan musim menunjukkan bahwa faktor musiman memiliki pengaruh signifikan terhadap jumlah penyewaan sepeda. Penyewaan mencapai puncaknya pada musim semi dan musim panas, sementara menurun drastis pada musim gugur dan musim dingin. Ini menandakan bahwa cuaca yang lebih hangat berkontribusi besar terhadap peningkatan penggunaan sepeda. Untuk memanfaatkan tren ini, perusahaan dapat merancang kampanye promosi khusus selama musim semi dan musim panas untuk menarik lebih banyak penyewa. Selain itu, penawaran yang lebih menarik di musim gugur dan musim dingin juga dapat dipertimbangkan untuk menjaga minat pelanggan dan mendorong penggunaan sepeda di luar musim puncak.
""")