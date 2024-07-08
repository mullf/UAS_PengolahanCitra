# UAS Pengolahan Citra

| Nim  | Nama | Kelas | 
| ------------- | ------------- | ------------- |
| 312210191 | Riski Probo Sadewo | TI. 22. A2  |
| 312210224 | Johanes Mula Febrian Sihombing | TI. 22. A2  |
| 312210223 | Faiz Dzaki Ramadhani | TI. 22. A2  |

## Laporan Dan Hasil
(https://drive.google.com/file/d/1VQsqE6AFBJVNKG-q4pzhyJB5j0qeGSMr/view?usp=sharing)

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

## Penjelasan Kode dan Langkah-langkah

### Langkah 1 : Membaca Gambar
![Citra1](https://github.com/mullf/UAS_PengolahanCitra/assets/115521049/eaad4d56-d0c8-4fbb-ba33-b837259550c5)

Langkah pertama adalah membaca gambar dari file menggunakan fungsi ``cv2.imread.`` Gambar yang dibaca kemudian diubah warnanya dari BGR ke RGB menggunakan ``cv2.cvtColor`` untuk kompatibilitas dengan ``matplotlib`` 


### Langkah 2 : Mengubah Warna Gambar
![Citra2](https://github.com/mullf/UAS_PengolahanCitra/assets/115521049/a32d16cf-c98b-413b-bf7f-fbc6cfaf230d)

Gambar yang dibaca oleh OpenCV menggunakan format BGR secara default. Fungsi cv2.cvtColor digunakan untuk mengubah gambar menjadi format RGB. 


### Langkah 3 : Menampilkan Gambar Asli
![Citra3](https://github.com/mullf/UAS_PengolahanCitra/assets/115521049/15ce711d-8672-424c-8988-55fce4ffecca)

Gambar asli ditampilkan menggunakan`` matplotlib`` untuk visualisasi awal.


### Langkah 4 : Mengubah Bentuk Gambar
![Citra4](https://github.com/mullf/UAS_PengolahanCitra/assets/115521049/db624f88-83b7-44b1-80b1-194819fd975b)

Gambar diubah menjadi array 2D di mana setiap baris mewakili satu piksel dengan tiga nilai warna (RGB).

![Citra4 2](https://github.com/mullf/UAS_PengolahanCitra/assets/115521049/598cbad2-9cfc-42a3-a40d-ecdaac918201)


### Langkah 5 : Mengonversi ke Tipe Float
![Citra5](https://github.com/mullf/UAS_PengolahanCitra/assets/115521049/22d1e616-1965-4d57-93b3-b8d42caf63d7)

Array piksel dikonversi ke tipe float untuk digunakan dalam algoritma K-Means.


### Langkah 6 : Menentukan Kriteria K-Means
![Citra6](https://github.com/mullf/UAS_PengolahanCitra/assets/115521049/5adc9b58-8135-4e55-9a23-de6295a451fe)

Kriteria untuk algoritma K-Means ditentukan, yaitu berhenti setelah 100 iterasi atau mencapai akurasi 85%. 


### Langkah 7 : Menjalankan K-Means Clustering
![Citra7](https://github.com/mullf/UAS_PengolahanCitra/assets/115521049/6bd6021d-33ae-4492-ad4a-2188b100c148)

K-Means clustering dijalankan dengan jumlah cluster k yang ditentukan (dalam kasus ini, 4). Fungsi cv2.kmeans menangani proses penetapan titik data ke cluster, perhitungan pusat cluster, dan penyesuaian hingga konvergensi. 


### Langkah 8 : Mengonversi Data ke Nilai 8-Bit
![Citra8](https://github.com/mullf/UAS_PengolahanCitra/assets/115521049/7503a017-310a-4720-b685-46b07cfc69f2)

Pusat cluster dikonversi menjadi nilai 8-bit dan data gambar yang di-segmentasi dibentuk ulang menjadi dimensi gambar asli.


### Langkah 9 : Menampilkan Gambar yang sudah di Segmentasi
![Citra9](https://github.com/mullf/UAS_PengolahanCitra/assets/115521049/fcbf6fe7-352a-4e22-b08d-7b84338bdacf)

Gambar yang sudah di-segmentasi ditampilkan menggunakan matplotlib.
