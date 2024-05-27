import pandas as pd
import numpy as np
import random

def preprocess_data(file_path):
    # Mengimpor data dari CSV
    data = pd.read_csv(file_path)
    
    # Menghapus kolom yang bukan bilangan (numerik)
    numeric_data = data.select_dtypes(include=[np.number])
    
    # Mengonversi DataFrame ke numpy array untuk memudahkan perhitungan
    return numeric_data.values

def find_nearest(record, dataset):
    # Fungsi ini untuk mencari rekord terdekat dengan rekord yang diberikan
    min_dist = float('inf')
    nearest_record = None
    for r in dataset:
        dist = np.linalg.norm(np.array(record) - np.array(r))  # Menghitung jarak Euclidean
        if dist != 0 and dist < min_dist:  # Pastikan jarak bukan nol (bukan dirinya sendiri)
            min_dist = dist
            nearest_record = r
    return nearest_record

def main():
    # Langkah 0: Import dataset.csv menjadi data dan praproses data
    data = preprocess_data('dataset.csv')

    # Langkah 1: MULAI
    # Langkah 2: Input nilai k
    k = int(input("Masukkan nilai k: "))
    
    # Langkah 3: Buat array bernama arrayK yang ukurannya sama dengan k
    arrayK = [[None] for _ in range(k)]
    
    # Langkah 4: Buat array bernama arrayB yang ukurannya sama dengan k
    arrayB = [None] * k
    
    # Langkah 5: Pilih k rekord di dalam data
    selected_records = random.sample(list(data), k)
    
    # Cetak k rekord yang terpilih
    print("Rekord yang terpilih:")
    for idx, record in enumerate(selected_records, 1):
        print(f"Rekord {idx}: {record}")
    
    # Langkah 6: For i=1 sampai k
    for i in range(1, k + 1):
        record = selected_records[i - 1]
        
        # Langkah 6.1: Rekord ke-i mencari rekord yang terdekat dengannya di dalam belantara rekord data
        nearest_record = find_nearest(record, data)
        
        # Langkah 6.2 dan 6.3
        if nearest_record is not None:
            arrayB[i - 1] = nearest_record
        else:
            arrayB[i - 1] = None
    
    # Langkah 7: Menyalin isi setiap arrayB[i-1] ke arrayK[i-1][0]
    for i in range(k):
        arrayK[i][0] = arrayB[i - 1]
    
    # Langkah 8: Cetak arrayK
    print("ArrayK:")
    for idx, record in enumerate(arrayK, 1):
        print(f"ArrayK {idx}: {record}")
    
    # Langkah 9: FINISH
    print("ArrayB:", arrayB)

if __name__ == "__main__":
    main()
