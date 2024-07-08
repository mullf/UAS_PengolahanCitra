# UAS Pengolahan Citra

| Nim  | Nama | Kelas | 
| ------------- | ------------- | ------------- |
| 312210191 | Riski Probo Sadewo | TI. 22. A2  |
| 312210224 | Johanes Mula Febrian Sihombing | TI. 22. A2  |
| 312210223 | Faiz Dzaki Ramadhani | TI. 22. A2  |

## Laporan


## Tujuan 
Mengimplementasikan algoritma K-Means untuk segmentasi gambar. 
Menampilkan hasil segmentasi gambar dengan jumlah cluster yang ditentukan. 
 
Code 
 
```
import numpy as np import matplotlib.pyplot as plt 
import cv2 
 
# Membaca gambar (gunakan path gambar yang sesuai) image = cv2.imread('monarch.jpg') 
 
# Memeriksa apakah gambar berhasil dimuat if image is None: 
    print("Error: Gambar tidak ditemukan atau tidak dapat dimuat.") else: 
    # Mengubah warna gambar menjadi RGB (dari BGR)     image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) 
     
    # Menampilkan gambar asli     plt.imshow(image)     plt.title('Original Image') 
    plt.axis('off')  # Menyembunyikan axis     plt.show() 
 
    # Mengubah bentuk gambar menjadi array 2D dari piksel dan 3 nilai warna (RGB)     pixel_vals = image.reshape((-1, 3)) 
 
    # Mengonversi ke tipe float 
    pixel_vals = np.float32(pixel_vals) 
 
    # Langkah 1: Pilih jumlah cluster yang ingin dicari yaitu k. 
    k = 4 
 
    # Langkah 2: Tetapkan titik data secara acak ke salah satu k cluster. 
    # cv2.kmeans akan menangani penetapan acak secara internal 
 
    # Menentukan kriteria untuk algoritma berhenti berjalan, yang akan terjadi setelah 100 iterasi 
    # atau epsilon (akurasi yang dibutuhkan) tercapai pada 85% 
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.85) 
 
    # Melakukan clustering k-means dengan jumlah cluster yang ditentukan sebagai k 
    # Pusat acak awalnya dipilih untuk clustering k-means 
    retval, labels, centers = cv2.kmeans(pixel_vals, k, None, criteria, 10, 
cv2.KMEANS_RANDOM_CENTERS) 
 
    # Langkah 3: Kemudian hitung pusat clusternya. 
    # (cv2.kmeans menghitung pusat awal dan memperbaruinya dalam loop) 
    # centers sekarang berisi pusat dari setiap cluster 
 
    # Langkah 4: Hitung jarak titik data dari pusat masing-masing cluster. 
    # (cv2.kmeans menangani ini secara internal dengan menghitung jarak setiap titik ke pusat) 
 
    # Langkah 5: Bergantung pada jarak setiap titik data dari klaster, tetapkan kembali titik data ke   klaster terdekat. 
    # (cv2.kmeans menetapkan kembali setiap titik ke pusat cluster terdekat) 
 
    # Langkah 6: Hitung lagi pusat cluster yang baru. 
    # (cv2.kmeans menghitung ulang pusat berdasarkan penetapan baru) 
 
    # Langkah 7: Ulangi langkah 4, 5 dan 6 hingga titik data tidak mengubah cluster, atau hingga mencapai jumlah iterasi yang ditetapkan. 
    # (cv2.kmeans mengulangi proses ini hingga konvergensi atau iterasi maksimum tercapai) 
 
    # Mengonversi data menjadi nilai 8-bit     centers = np.uint8(centers) 
    segmented_data = centers[labels.flatten()] 
 
    # Mengubah bentuk data menjadi dimensi gambar asli     segmented_image = segmented_data.reshape((image.shape)) 
 
    # Menampilkan gambar yang sudah di-segmentasi     plt.imshow(segmented_image) 
    plt.title('Segmented Image with K-Means Clustering')     plt.axis('off')  # Menyembunyikan axis     plt.show() 
 
``` 

