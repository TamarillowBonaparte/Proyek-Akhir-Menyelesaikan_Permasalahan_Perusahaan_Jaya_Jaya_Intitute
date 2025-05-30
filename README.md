# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech
Proyek ini bertujuan untuk membantu **Jaya Jaya Institut**, sebuah perusahaan edutech, dalam mengidentifikasi siswa yang berisiko tinggi mengalami **dropout**. Dengan menggunakan data historis siswa dan model machine learning, sistem ini memprediksi kemungkinan seorang siswa akan lulus atau dropout, serta memberikan wawasan bagi tim akademik untuk mengambil tindakan preventif.
## Business Understanding
Jaya Jaya Institut mengalami tingkat dropout siswa yang signifikan, terutama pada semester awal. Hal ini berdampak pada reputasi institusi, efisiensi sumber daya pengajaran, dan pengelolaan operasional. Proyek ini hadir untuk memberikan solusi prediktif guna membantu manajemen memahami pola-pola yang menyebabkan siswa dropout.
### Permasalahan Bisnis
1. **Tingginya Tingkat Dropout di Semester Awal**  
   Banyak siswa gagal menyelesaikan semester pertama akibat berbagai tekanan, baik akademik maupun non-akademik. Hal ini menyebabkan kerugian bagi institusi dalam bentuk biaya operasional yang sia-sia dan citra yang menurun.

2. **Minimnya Sistem Peringatan Dini Berbasis Data**  
   Saat ini, tidak ada sistem yang secara otomatis mengidentifikasi siswa dengan risiko tinggi untuk dropout. Hal ini menyulitkan pihak akademik untuk memberikan bantuan tepat waktu.

3. **Kesulitan dalam Mengidentifikasi Faktor Penyebab Dropout**  
   Faktor-faktor seperti status ekonomi, beasiswa, performa akademik, dan latar belakang keluarga sulit dievaluasi tanpa analisis menyeluruh. Tanpa pemahaman ini, strategi retensi yang diterapkan cenderung tidak efektif.

4. **Kurangnya Strategi Retensi yang Terpersonalisasi dan Berdasarkan Data**  
   Institusi belum memiliki pendekatan yang sistematis untuk menyusun intervensi berbasis data yang menyesuaikan dengan profil risiko siswa, sehingga strategi yang diterapkan masih bersifat umum dan tidak berdampak signifikan.


### Cakupan Proyek
1. Pengumpulan dan pembersihan data siswa.
2. Eksplorasi dan analisis visual terhadap faktor-faktor demografis, akademik, dan ekonomi.
3. Engineering fitur dan seleksi fitur paling relevan.
4. Pelatihan berbagai model machine learning dan tuning hyperparameter.
5. Evaluasi performa model berdasarkan metrik klasifikasi.
6. Penyimpanan model terbaik beserta scaler dan encoder untuk deployment.

### Persiapan

Sumber data: menggunakan dataset data.csv

Tools: Python >3.10, Streamlit, scikit-learn, joblib, pandas, matplotlib.

Setup environment:
Instalasi environment:
```bash
pip install -r requirements.txt
```
atau secara manual:
```bash
pip install streamlit pandas scikit-learn joblib matplotlib seaborn
```
Menjalankan Aplikasi

Jalankan aplikasi Streamlit dengan:
```bash
streamlit run app.py
```
Aplikasi akan terbuka di browser default Anda di alamat
```
http://localhost:8501
```
## Business Dashboard
Business Dashboard
Business dashboard dibuat menggunakan Metabase sebagai alat visualisasi data untuk mempermudah pemahaman terhadap pola dropout dan kelulusan siswa di Jaya Jaya Institut. Dashboard ini menyajikan insight penting yang mendukung pengambilan keputusan dalam hal pencegahan dropout.

Berikut ini adalah beberapa visualisasi utama yang ditampilkan dalam dashboard:

Distribusi Usia Berdasarkan Status (Dropout vs Graduate)
Visualisasi ini menunjukkan sebaran usia siswa saat mendaftar, dikategorikan berdasarkan status kelulusan. Hal ini berguna untuk melihat apakah usia memengaruhi kemungkinan dropout.

Komposisi Status Dropout dan Graduate (Pie Chart)
Menampilkan perbandingan proporsi antara jumlah siswa yang dropout dan yang lulus. Dari grafik terlihat bahwa sekitar 39,1% siswa mengalami dropout.

Perbandingan Nilai Semester 1 dan Semester 2 Berdasarkan Status
Menggambarkan total nilai dari semester 1 dan 2 antara siswa dropout dan graduate. Visual ini menunjukkan bahwa nilai siswa dropout cenderung lebih rendah dari yang lulus.

Jumlah Dropout Berdasarkan Gender
Grafik ini menunjukkan perbedaan dropout antara laki-laki dan perempuan. Visual ini penting untuk melihat apakah ada ketimpangan gender terkait dropout.

Relasi Pendidikan Ibu dengan Status Siswa (Sankey Diagram)
Menunjukkan distribusi status kelulusan berdasarkan latar belakang pendidikan ibu. Diagram ini memberikan insight apakah pendidikan orang tua memiliki pengaruh terhadap keberhasilan studi siswa.

Relasi Pendidikan Ayah dengan Status Siswa (Sankey Diagram)
Serupa dengan pendidikan ibu, grafik ini memperlihatkan bagaimana tingkat pendidikan ayah berkorelasi dengan status kelulusan anak.

Akses Dashboard
Dashboard dapat diakses melalui alamat berikut:
Link Dashboard Metabase
(https://drive.google.com/drive/folders/1aoohoRMaQLquc_rZjxdvyaoRNXe5oU8g?usp=sharing)

Untuk login ke Metabase, gunakan kredensial berikut:

Email: root@mail.com

Password: root123

Pastikan Metabase telah dijalankan dengan benar agar dashboard dapat diakses dan divalidasi oleh evaluator atau reviewer.

## Menjalankan Sistem Machine Learning
Untuk menjalankan prototype:
1. Jalankan notebook_dani.py atau file .ipynb pada Google Colab/Jupyter Notebook.
2. Pastikan data telah disiapkan dalam format data.csv (dipisahkan oleh ;).

3. Sistem akan:
- Melakukan preprocessing dan engineering fitur
- Melatih beberapa model (Random Forest, Gradient Boosting, XGBoost, dll.)
- Menyimpan model terbaik dan semua encoder ke dalam folder model/

File hasil:

model/*.joblib → Model terlatih, scaler, dan label encoder

df_clean_processed.csv → Dataset yang telah diproses

requirements.txt → Dependensi environment

## Conclusion
erdasarkan eksperimen machine learning, proyek ini berhasil menghasilkan model prediktif dropout siswa dengan akurasi dan F1-score tinggi (lebih dari 90%). Model terbaik adalah XGBoost, dengan performa optimal setelah tuning hyperparameter. Hasil proyek ini mampu menjawab permasalahan bisnis sebagai berikut:

- Mengatasi Tingginya Dropout di Awal Semester
Model mampu mengidentifikasi siswa dengan risiko tinggi di awal semester, memungkinkan institusi untuk memberikan perhatian lebih cepat sebelum terjadi dropout.

- Membangun Sistem Peringatan Dini Berbasis Data
Dengan model prediktif yang telah dibangun, sistem dapat diterapkan sebagai early warning system untuk mendeteksi siswa berisiko sejak dini.

- Mengungkap Faktor Penyebab Dropout
Proyek ini mengungkap bahwa beasiswa, status ekonomi, nilai akademik, dan performa semester awal adalah faktor penting dalam menentukan keberhasilan siswa.

- Menyediakan Dasar Strategi Retensi yang Terpersonalisasi
Output model dan analisis fitur penting dapat digunakan untuk menyusun strategi intervensi spesifik, seperti program mentoring, bantuan finansial, dan pembinaan akademik.
### Rekomendasi Action Items
- Buat sistem peringatan dini untuk siswa dengan nilai semester pertama rendah.
- Berikan intervensi finansial kepada siswa yang memiliki tunggakan dan tidak mendapat beasiswa.
- Lakukan mentoring akademik pada siswa yang mengalami penurunan performa semester.
- Gunakan hasil prediksi untuk menyusun program retensi berbasis risiko.
