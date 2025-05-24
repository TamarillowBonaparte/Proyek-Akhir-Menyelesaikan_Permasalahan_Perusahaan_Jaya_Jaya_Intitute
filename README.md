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

Sumber data: ....

Setup environment:
```
pip install -r requirements.txt
```

## Business Dashboard
Jelaskan tentang business dashboard yang telah dibuat. Jika ada, sertakan juga link untuk mengakses dashboard tersebut.

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

Mengatasi Tingginya Dropout di Awal Semester
Model mampu mengidentifikasi siswa dengan risiko tinggi di awal semester, memungkinkan institusi untuk memberikan perhatian lebih cepat sebelum terjadi dropout.

Membangun Sistem Peringatan Dini Berbasis Data
Dengan model prediktif yang telah dibangun, sistem dapat diterapkan sebagai early warning system untuk mendeteksi siswa berisiko sejak dini.

Mengungkap Faktor Penyebab Dropout
Proyek ini mengungkap bahwa beasiswa, status ekonomi, nilai akademik, dan performa semester awal adalah faktor penting dalam menentukan keberhasilan siswa.

Menyediakan Dasar Strategi Retensi yang Terpersonalisasi
Output model dan analisis fitur penting dapat digunakan untuk menyusun strategi intervensi spesifik, seperti program mentoring, bantuan finansial, dan pembinaan akademik.
### Rekomendasi Action Items
- Buat sistem peringatan dini untuk siswa dengan nilai semester pertama rendah.
- Berikan intervensi finansial kepada siswa yang memiliki tunggakan dan tidak mendapat beasiswa.
- Lakukan mentoring akademik pada siswa yang mengalami penurunan performa semester.
- Gunakan hasil prediksi untuk menyusun program retensi berbasis risiko.
